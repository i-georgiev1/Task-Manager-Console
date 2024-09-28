from models.task import Task
import os
import logging
from functools import wraps


log_file_path = os.path.join(os.path.dirname(__file__), '../data/app.log')
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
    ]
)
logger = logging.getLogger(__name__)

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Executing {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned {result}")
        return result
    return wrapper



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

    @log
    def add_task(self, description, priority, due_date):
        task = Task(description, priority,status=False, due_date=due_date)
        self.tasks.append(task)


    def import_task(self, description, priority, status, due_date):
        task = Task(description, priority, status, due_date)
        self.tasks.append(task)


    def show_tasks(self):
        return [print(str(self.tasks.index(task) + 1) + '. ', task) for task in self.tasks]

    @log
    def sort_tasks(self):
        pass

    @log
    def show_completed_tasks(self):
        return [print(task) for task in self.tasks if task.status]

    @log
    def show_pending_tasks(self):
        return [print(task) for task in self.tasks if not task.status]

    @log
    def sort_tasks_priority(self):
        pass

    @log
    def sort_tasks_status(self, sort_by):
        pass

    @log
    def mark_completed(self, index):
        task = self.tasks[index]
        task.status = True
        self.tasks[index] = task

    @log
    def edit_description(self, index):
        task = self.tasks[index]
        new_description = input('Въведи редактираното описание: ')
        task.description = new_description
        self.tasks[index] = task

    @log
    def edit_priority(self, index):
        task = self.tasks[index]
        new_priority = input('Въведи новия приоритет: ')
        task.priority = new_priority
        self.tasks[index] = task

    @log
    def delete_task(self, index):
        self.tasks.pop(index)


    def __str__(self):
        is_completed = "Завършена" if self.status == True else "Незавършена"
        return f"Задача: {self.description} с приоритет {self.priority} е {is_completed} (Срок: {self.due_date})"