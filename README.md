# TODO LIST APP

# Setup

## Install Dependencies
### `pip install flask`

# Database
Inside the `database.db` file are the database data and code:
```sqlite
  CREATE TABLE "tasks" (
    "id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "name"	TEXT NOT NULL,
    "status"	TEXT
  );
```

## Run the server
### `set FLASK_APP=app.py`
### `flask run`
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) to view it in the browser.