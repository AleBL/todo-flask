from storage import connection
from flask import Flask, request, Response
from util.util_json import convertJSON

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/")
def index():
   return "Running"

@app.route("/task", methods = ["POST"])
def add_task():
   request_data = request.get_json()
   task = request_data["name"]
   
   new_task = connection.add_task(task)

   if new_task is None:
      data = { "Error": "Item not added" }
      return Response(convertJSON(data), status=422 , mimetype="application/json")
   
   return Response(new_task, status=200, mimetype="application/json")

@app.route("/tasks", methods = ["GET"])
def get_all_tasks():
   all_tasks = connection.all_tasks()
   return Response(all_tasks, status=200, mimetype="application/json")

@app.route("/task", methods=["GET"])
def get_task():
   task_id = request.args.get("id")

   try:
      task_id = int(task_id)
   except Exception:
      data = { "Error": "parameter '" + task_id + "' not is a number" }
      return Response(convertJSON(data), status=422 , mimetype="application/json")

   task = connection.get_task(task_id)
   
   if task is None:
      data = { "Error": "Task with id = %i not found" % task_id }
      return Response(convertJSON(data), status=404 , mimetype="application/json")

   return Response(task, status=200, mimetype="application/json")
