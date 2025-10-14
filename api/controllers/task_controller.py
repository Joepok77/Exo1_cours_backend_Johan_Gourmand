from typing import List, Optional
from models.task import Task, TaskStatus


class TaskController:

    def __init__(self):
        self.tasks: List[Task] = []

    def create_task(self, title: str, description: str = "") -> Task:
        task = Task(title, description)
        self.tasks.append(task)
        return task

    def get_all_tasks(self) -> List[Task]:
        return self.tasks

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        task = self.get_task_by_id(task_id)
        if task:
            task.update_info(title, description)
            return True
        return False

    def update_task_status(self, task_id: int, status: TaskStatus) -> bool:
        task = self.get_task_by_id(task_id)
        if task:
            task.update_status(status)
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False

    def get_tasks_by_status(self, status: TaskStatus) -> List[Task]:
        return [task for task in self.tasks if task.status == status]

    def get_task_count(self) -> int:
        return len(self.tasks)
