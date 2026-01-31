#!/usr/bin/env python3
from task_manager.storage import JsonStorage
from task_manager.service import TaskService
from task_manager.ui import ConsoleUI

def main():
    storage_file = "tasks.json"
    storage = JsonStorage(storage_file)
    service = TaskService(storage)
    ui = ConsoleUI(service)
    ui.run()

if __name__ == "__main__":
    main()
