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
      data = { "error": "Item not added" }
      return Response(convertJSON(data), status=422 , mimetype="application/json")
   
   return Response(new_task, status=200, mimetype="application/json")
