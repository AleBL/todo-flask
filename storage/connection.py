import sqlite3
from util.util_json import convertJSON

DATABASE_PATH = 'storage/database.db'
NOTSTARTED = 'Not Started'

CONNECTION = sqlite3.connect(DATABASE_PATH, check_same_thread=False)
CURSOR = CONNECTION.cursor()

def add_task(task):
    try:
        CURSOR.execute('insert into tasks(name, status) values(?,?)', (task, NOTSTARTED))
        CONNECTION.commit()

        data = { 
            "id": CURSOR.lastrowid,
            "name": task, 
            "status": NOTSTARTED 
        }

        return convertJSON(data)
    except Exception as e:
        print('Error: ', e)
        return None

def all_tasks():
    try:
        CURSOR.execute('select * from tasks')
        all_tasks = CURSOR.fetchall()

        all_tasks_json = []

        for task in all_tasks:
            task_iter = iter(task)
            all_tasks_json += [{
                "id": next(task_iter),
                "name": next(task_iter),
                "status": next(task_iter)
            }]
        
        data = { 
            "total_tasks": len(all_tasks), 
            "tasks": all_tasks_json 
        }

        return convertJSON(data)
    except Exception as e:
        print('Error: ', e)
        return None
