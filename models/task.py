from datetime import datetime


class Task:
    def __init__(self, description='', priority='', status=False, due_date=None):
        self.description = description
        self.priority = priority
        self.status = status
        self.due_date = due_date

    def __str__(self):
        return f"Задача: {self.description} с приоритет {self.priority} е {self.status} (Срок: {self.due_date})"
