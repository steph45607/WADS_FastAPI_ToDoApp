from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = ["https://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

todos = {
    0:{
        "title":"this is title",
        "desc" : "this is desc",
        "completed":False,
        "created":"timestamp"
    }
}

@app.get("/")
def index():
    return {"msg":"Welcome"}

@app.get("/get-todos")
def get_todos():
    return todos