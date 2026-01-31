from typing import List, Optional
from .models import Task
from .interfaces import StorageInterface

class TaskService:
    def __init__(self, storage: StorageInterface):
        self.storage = storage
        self.tasks: List[Task] = self.storage.load_tasks()

    def add_task(self, title: str, description: str = "") -> Task:
        new_id = self._generate_id()
        task = Task(id=new_id, title=title, description=description)
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        return task

    def get_all_tasks(self) -> List[Task]:
        return sorted(self.tasks, key=lambda t: t.status == "Completed")

    def complete_task(self, task_id: int) -> bool:
        task = self._find_task(task_id)
        if task:
            task.status = "Completed"
            self.storage.save_tasks(self.tasks)
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        task = self._find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.storage.save_tasks(self.tasks)
            return True
        return False

    def _find_task(self, task_id: int) -> Optional[Task]:
        for t in self.tasks:
            if t.id == task_id: return t
        return None

    def _generate_id(self) -> int:
        return max([t.id for t in self.tasks], default=0) + 1
