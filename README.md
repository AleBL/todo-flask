# 📝 TODO List App

## ⚙️ Setup

### 📦 Install Dependencies
To install the necessary dependencies, run the following commands:

```sh
sudo apt-get install sqlite3 libsqlite3-dev
pip install flask
pip install python-dotenv
pip install pysqlite3
pip install gunicorn
```

Alternatively, you can run the setup script on Linux:

```sh
./setup.sh
```

### 💻 Environment Versions

- **Python:** 3.13.0
- **Flask:** 3.1.0
- **python-dotenv:** 1.0.1
- **pysqlite3:** 0.5.4
- **gunicorn:** 23.0.0

## 🗄️ Database
The `database.db` file contains the database schema and data. The schema is defined as follows:

```sqlite
CREATE TABLE "tasks" (
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
  "name" TEXT NOT NULL,
  "status" TEXT
);
```

## 🚀 Run the Server
To set up and run the server, follow these steps:

1. Start the Flask server:
   ```sh
   gunicorn --bind 0.0.0.0:5000 app:app
   ```

2. Open [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the application in the browser.

## 🔄 Postman Collection

To easily test the API using Postman, you can import the collection using the following link:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/8243464-d8fafa27-eb2a-4d77-b5e8-4d5dd5940651?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D8243464-d8fafa27-eb2a-4d77-b5e8-4d5dd5940651%26entityType%3Dcollection%26workspaceId%3Daa682c41-5450-4149-beca-ae2a45c19f0d)

Feel free to reach out if you need further assistance! 😊