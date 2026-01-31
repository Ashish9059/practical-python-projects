import sys
from .service import TaskService

class ConsoleUI:
    def __init__(self, service: TaskService):
        self.service = service

    def print_menu(self):
        print("\n=== Professional Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Enter choice: ").strip()
            try:
                if choice == '1':
                    title = input("Task Title: ")
                    desc = input("Description: ")
                    t = self.service.add_task(title, desc)
                    print(f"Task created: [ID: {t.id}] {t.title}")
                elif choice == '2':
                    tasks = self.service.get_all_tasks()
                    for t in tasks:
                        status = "[x]" if t.status == "Completed" else "[ ]"
                        print(f"{status} {t.id}: {t.title}")
                elif choice == '3':
                    tid = int(input("Task ID to complete: "))
                    if self.service.complete_task(tid): print("Success.")
                elif choice == '4':
                    tid = int(input("Task ID to delete: "))
                    if self.service.delete_task(tid): print("Deleted.")
                elif choice == '5':
                    sys.exit()
            except Exception as e:
                print(f"Error: {e}")
