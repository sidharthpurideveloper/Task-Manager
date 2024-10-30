from user_authentication import UserAuthentication
from task_manager import TaskManager

# Main application loop
class TaskManagerApp:
    def __init__(self):
        self.auth = UserAuthentication()
        self.task_manager = None
        self.logged_in_user = None

    def main_menu(self):
        while True:
            print("\n--- Main Menu ---")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.register_user()
            elif choice == '2':
                self.login_user()
            elif choice == '3':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def register_user(self):
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        self.auth.register(username, password)

    def login_user(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if self.auth.login(username, password):
            self.logged_in_user = username
            self.task_manager = TaskManager(self.logged_in_user)
            self.task_menu()

    def task_menu(self):
        while True:
            print("\n--- Task Menu ---")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Mark Task as Completed")
            print("4. Delete Task")
            print("5. Logout")
            choice = input("Choose an option: ")

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.mark_task_completed()
            elif choice == '4':
                self.delete_task()
            elif choice == '5':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please try again.")

    def add_task(self):
        task_description = input("Enter task description: ")
        self.task_manager.add_task(task_description)

    def view_tasks(self):
        self.task_manager.view_tasks()

    def mark_task_completed(self):
        task_id = input("Enter the task ID to mark as completed: ")
        self.task_manager.mark_task_completed(task_id)

    def delete_task(self):
        task_id = input("Enter the task ID to delete: ")
        self.task_manager.delete_task(task_id)

if __name__ == "__main__":
    app = TaskManagerApp()
    app.main_menu()
