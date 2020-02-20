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
