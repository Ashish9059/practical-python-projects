from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    status: str = "Pending"
    created_at: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Task':
        return cls(
            id=data["id"],
            title=data["title"],
            description=data.get("description", ""),
            status=data.get("status", "Pending"),
            created_at=data.get("created_at")
        )
