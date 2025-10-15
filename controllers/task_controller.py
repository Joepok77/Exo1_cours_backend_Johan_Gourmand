from typing import List
from models.task import Task


class TaskController:

    def __init__(self):
        self.tasks: List[Task] = []

    def create_task(self, title: str, description: str = "") -> Task:
        task = Task(title, description)
        self.tasks.append(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    def delete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False

    def get_task_count(self) -> int:
        return len(self.tasks)
