import json
import os
from typing import List
from .interfaces import StorageInterface
from .models import Task

class JsonStorage(StorageInterface):
    def __init__(self, filename: str):
        self.filename = filename

    def load_tasks(self) -> List[Task]:
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Task.from_dict(t) for t in data]
        except (json.JSONDecodeError, IOError):
            return []

    def save_tasks(self, tasks: List[Task]) -> None:
        try:
            data = [t.to_dict() for t in tasks]
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Error saving: {e}")
