from models.manager import TaskManager
from datetime import datetime as dt
import os
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



def main_menu():
    print('1. Добавяне на нова задача')
    print('2. Преглед на всички задачи')
    print('0. Изход от програмата')

def all_tasks_menu():
    print('1. Редактиране на задача')
    print('2. Изтриване на задача')
    print('3. Сортирай задачите по приоритет')
    print('4. Сортирай задачите по статус')
    print('0. Връщане към главно меню')

def task_edit_menu():
    print('1. Маркирай като завършена')
    print('2. Редактирай описанието')
    print('3. Промени приоритета')
    print('0. Връщане към главно меню')



manager = TaskManager()

 # Отваря csv файла и чете от него

filepath = 'data/tasks.csv'

if not os.path.isfile(filepath):
    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['description', 'priority', 'status', 'due_date'])
else:
    print('\n')

with open(filepath, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    data = list(reader)

for task in data[1:]:
    description = task[0]
    priority = task[1]
    status = task[2]
    due_date = task[3]
    manager.import_task(description, priority, status, due_date)


# Изпраща имейл ако има просрочени задачи
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()
email = 'task.manager.notifications@gmail.com'
email_password = 'cihg cftd raed ruji'
smtp_object.login(email, email_password)
email_user = input('Въведете вашият имейл: ')

for task in manager.tasks:
    curr_date = str(dt.today())
    task_date = task.due_date
    if task_date < curr_date:
        task_id = str(manager.tasks.index(task) + 1)
        subject = "Просрочена задача"
        message = "Имате просрочена задача номер " + task_id + " - " + task.__str__()

        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = email_user
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain', 'utf-8'))

        smtp_object.sendmail(email, email_user, msg.as_string())

while True:
    main_menu()

    choice = int(input("Изберете опция: "))
    print('\n')

    if choice == 0: # Изход от програмата
        # Запази в csv при изход от програмата

        with open(filepath, 'w', newline='', encoding='utf-8') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['description', 'priority', 'status', 'due_date'])

            for task in manager.tasks:
                writer.writerow([task.description, task.priority, task.status, task.due_date])

        break

    elif choice == 1: # Добавяне на нова задача
        description = input('Въведи описание на задачата: ')

        while True:
            priority = input('Въведи приоритет на задачата (нисък, среден или висок): ')
            if priority == 'нисък' or priority == 'среден' or priority == 'висок':
                break
            else:
                print('Моля въведи отново валиден приоритет на задачата (нисък, среден или висок)')


        try:
            date_input = input("Въведете до кога трябва да бъде свършена задачата (във формат ЧЧ-MM ДД-MM-ГГГГ): ")
            due_date = dt.strptime(date_input, "%H-%M %d-%m-%Y")
        except ValueError:
            print("Невалиден формат. Моля въведете дата и час във формат - ЧЧ-MM ДД-MM-ГГГГ.")

        manager.add_task(description, priority, due_date)

    elif choice == 2: # Преглед на всички задачи
        manager.show_tasks()
        print('\n Меню: ')
        all_tasks_menu()

        choice = int(input("Изберете опция: "))
        print('\n')

        if choice == 0:
            pass

        elif choice == 1: #Редактиране на задача
            task_index = int(input('Въведи номера на задачата: '))
            task_index -= 1
            task_edit_menu()
            choice = int(input("Изберете опция: "))
            print('\n')

            if choice == 0:
                pass
            elif choice == 1: # Маркирай задачата като завършена
                manager.mark_completed(task_index)
            elif choice == 2: # Редактирай описанието на задачата
                manager.edit_description(task_index)
            elif choice == 3: # Промени приоритета на задачата
                manager.edit_priority(task_index)

        elif choice == 2: # Изтриване на задача
            task_index = int(input('Въведи номера на задачата: '))
            task_index -= 1
            delete_task = input('Сигурни ли сте че искате да изтриете задачата (да или не): ')
            if delete_task == 'да':
                manager.delete_task(task_index)
            else:
                pass

        elif choice == 3: # Сортирай задачите по приоритет
            manager.sort_tasks_priority()

        elif choice == 4: # Сортирай задачите по статус
            sort_by = int(input('1. По незавършени или 2. По завършени: '))
            manager.sort_tasks_status(sort_by)
