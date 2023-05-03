# import the package or library
from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# ENDPOINT: domain/student/1
# GET
# POST
# PUT
# DELETE

# {
#     uid:{
#         "completed":True,
#         "created":March 15, 2023 at 11:45:28 PM UTC+7,
#         "description":"Message here",
#         "title":"Task"
#     },
#     uid:{
#         "completed":True,
#         "created":March 15, 2023 at 11:45:28 PM UTC+7,
#         "description":"Message here",
#         "title":"Task"
#     }
# }


tasks = {
    "6Y0To1VcSSfBOfrS4beL":{
        "completed":True,
        # "created":"March 15, 2023 at 11:45:28 PM UTC+7",
        "description":"20 duckbills",
        "title":"Buy Masks"
    },
    "DF2nFjMmjvg3Cncrdmqx":{
        "completed":False,
        # "created":"March 15, 2023 at 11:45:28 PM UTC+7",
        "description":"Anya's Room",
        "title":"Do Laundry"
    }
}



@app.get("/")
def index():
    return {"Message":"Welcome to Stephanie's To Do App"}

# domain/get-task/{uid}
# get the task based on the uid
@app.get("/get-task/{uid}")
def get_student(uid : str = Path(desciption = "uid")):
    return tasks[uid]

# domain/get-task-by-title?title=task
# get the task based on the title
@app.get("/get-task-by-title")
def get_task_by_title(*, title: Optional[str] = None):
    for uid in tasks:
        if tasks[uid]["title"] == title:
            return tasks[uid]
    return {"Error":"Task title not found"}

class Task(BaseModel):
    completed: bool
    description: str
    title:str

class UpdatedTask(BaseModel):
    completed: bool
    description: str
    title:str

# post method
# add new task
@app.post("/create-task/{uid}")
def add_task_id(uid:str, task:Task):
    if uid in tasks:
        return{"Error":"Task uid exists"}
    tasks[uid]= task
    return tasks[uid]

# put method
# update task
# @app.put("/update-task/{uid}")
# def update_task(uid:str, task:UpdatedTask):
#     if uid not in tasks:
#         return {"Error":"Student doesn't exists"}
#     if tasks[uid].completed != None:
#         tasks[uid].completed = task.completed
#         # return task.completed

#     if tasks[uid].description != None:
#         tasks[uid].description = task.description
#         # return task.description

#     if tasks[uid].title != None:
#         tasks[uid].title = task.title
#         # return task.title
    
#     return tasks[uid]

@app.get("/list-task")
def list_task():
    return tasks

# delete method
@app.delete("/delete-task/{uid}")
def delete_task(uid:str):
    del tasks[uid]
    return {"Data":"Has been deleted"}

@app.delete("/delete-task-by-title")
def delete_task_by_title(title: str = None):
    for uid in tasks:
        if tasks[uid]["title"] == title:
            del tasks[uid]
            return {"Data":"Has been deleted"}
    return {"Data":"can't be found"}
