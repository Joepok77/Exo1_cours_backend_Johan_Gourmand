from datetime import datetime


class Task:
    _id_counter = 1

    def __init__(self, title: str, description: str = ""):
        self.id = Task._id_counter
        Task._id_counter += 1
        self.title = title
        self.description = description
        self.created_at = datetime.now()

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    def __str__(self) -> str:
        return f"[{self.id}] {self.title}"

    def __repr__(self) -> str:
        return f"Task(id={self.id}, title='{self.title}')"
