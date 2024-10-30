import os

class TaskManager:
    def __init__(self, username, tasks_file='tasks.txt'):
        self.username = username
        self.tasks_file = tasks_file
        if not os.path.exists(self.tasks_file):
            open(self.tasks_file, 'w').close()  # Create file if it doesn't exist

    def add_task(self, task_description):
        task_id = self.get_next_task_id()
        with open(self.tasks_file, 'a') as f:
            f.write(f"{self.username},{task_id},{task_description},Pending\n")
        print(f"Task '{task_description}' added successfully!")

    def view_tasks(self):
        tasks = self._load_tasks()
        if tasks:
            for task in tasks:
                print(f"ID: {task['id']}, Description: {task['description']}, Status: {task['status']}")
        else:
            print("No tasks found.")

    def mark_task_completed(self, task_id):
        tasks = self._load_tasks()
        updated = False
        with open(self.tasks_file, 'w') as f:
            for task in tasks:
                if task['id'] == task_id:
                    task['status'] = 'Completed'
                    updated = True
                f.write(f"{task['username']},{task['id']},{task['description']},{task['status']}\n")
        if updated:
            print(f"Task {task_id} marked as completed.")
        else:
            print(f"Task with ID {task_id} not found.")

    def delete_task(self, task_id):
        tasks = self._load_tasks()
        tasks_to_keep = [task for task in tasks if task['id'] != task_id]
        if len(tasks) == len(tasks_to_keep):
            print(f"Task with ID {task_id} not found.")
            return
        with open(self.tasks_file, 'w') as f:
            for task in tasks_to_keep:
                f.write(f"{task['username']},{task['id']},{task['description']},{task['status']}\n")
        print(f"Task {task_id} deleted successfully.")

    def get_next_task_id(self):
        tasks = self._load_tasks()
        if tasks:
            last_task_id = int(tasks[-1]['id'])
            return last_task_id + 1
        return 1

    def _load_tasks(self):
        tasks = []
        with open(self.tasks_file, 'r') as f:
            for line in f:
                username, task_id, description, status = line.strip().split(',')
                if username == self.username:
                    tasks.append({'username': username, 'id': task_id, 'description': description, 'status': status})
        return tasks
