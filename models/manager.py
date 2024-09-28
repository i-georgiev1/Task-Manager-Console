from models.task import Task
import os
from datetime import datetime
import csv


def chosen_task():
    try:
        choice = int(input(''))
        choice -= 1
        return choice
    except ValueError:
        print("Моля въведи правилен номер")
        return None




class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, priority, due_date):
        task = Task(description, priority,status=False, due_date=due_date)
        self.tasks.append(task)

    def import_task(self, description, priority, status, due_date):
        task = Task(description, priority, status, due_date)
        self.tasks.append(task)


    def show_tasks(self):
        return [print(str(self.tasks.index(task) + 1) + '. ', task) for task in self.tasks]

    def sort_tasks(self):
        pass

    def show_completed_tasks(self):
        return [print(task) for task in self.tasks if task.status]

    def show_pending_tasks(self):
        return [print(task) for task in self.tasks if not task.status]

    def sort_tasks_priority(self):
        pass

    def sort_tasks_status(self, sort_by):
        pass


    def mark_completed(self, index):
        task = self.tasks[index]
        task.status = True
        self.tasks[index] = task

    def edit_description(self, index):
        task = self.tasks[index]
        new_description = input('Въведи редактираното описание: ')
        task.description = new_description
        self.tasks[index] = task

    def edit_priority(self, index):
        task = self.tasks[index]
        new_priority = input('Въведи новия приоритет: ')
        task.priority = new_priority
        self.tasks[index] = task

    def delete_task(self, index):
        self.tasks.pop(index)


    def __str__(self):
        is_completed = "Завършена" if self.status == True else "Незавършена"
        return f"Задача: {self.description} с приоритет {self.priority} е {is_completed} (Срок: {self.due_date})"