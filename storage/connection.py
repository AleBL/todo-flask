import sqlite3
from util import turple
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
        
        all_tasks_json = list(map(lambda task : turple.to_task_DICT(task), all_tasks))
        
        data = { 
            "total_tasks": len(all_tasks), 
            "tasks": all_tasks_json 
        }

        return convertJSON(data)
    except Exception as e:
        print('Error: ', e)
        return None

def get_task(id):
    try:
        CURSOR.execute("select * from tasks where id=%i" % id)
        task = CURSOR.fetchone()

        task = turple.to_task_DICT(task)

        return convertJSON(task)
    except Exception as e:
        print('Error: ', e)
        return None
