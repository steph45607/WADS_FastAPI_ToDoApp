# WADS_FastAPI_ToDoApp
ToDo App exercise - REST API with FastAPI

## /index
**Method:** GET

**Desc:** Display welcome message

**Request Body:** -

**Response Body:**
```json
{
  "Message": "Welcome to Stephanie's To Do App"
}
```
---
## /get-task/{uid}

**Method:** GET

**Desc:** Display searched task based on their uid

**Request Body:** -

**Fail message:**
```json
{"Error":"Task title not found"}
```

**Response Body:**
```json
{
  "completed": true,
  "description": "20 duckbills",
  "title": "Buy Masks"
}
```
---
## /get-task-by-title?title={taskTitle}

**Method:** GET

**Desc:** Display searched task based on their task title

**Request Body:** -

**Fail message:**
```json
{"Error":"Task title not found"}
```

**Response Body:**
```json
{
  "completed": true,
  "description": "20 duckbills",
  "title": "Buy Masks"
}
```
---
## /list-tasks

**Method:** GET

**Desc:** Display all tasks

**Request Body:** -

**Response Body:**
```json
{
  "6Y0To1VcSSfBOfrS4beL": {
    "completed": true,
    "description": "20 duckbills",
    "title": "Buy Masks"
  },
  "DF2nFjMmjvg3Cncrdmqx": {
    "completed": false,
    "description": "Anya's Room",
    "title": "Do Laundry"
  }
}
```
---
## /create-task/{uid}

**Method:** POST

**Desc:** Create new task

**Request Body:** 
```json
{
  "completed": false,
  "description": "this is new task",
  "title": "new task"
}
```

**Fail message:**
```json
{"Error":"Task uid already exists"}
```

**Response Body:**
```json
{
  "completed": false,
  "description": "this is new task",
  "title": "new task"
}
```
---
## /update-task/{uid}

**Method:** PUT

**Desc:** Update existing task

**Request Body:** 
```json
{
  "description": "new description"
}
```

**Fail message:**
```json
{"Error":"Task doesn't exists"}
```

**Response Body:**
```json
{
  "completed": true,
  "description": "new description",
  "title": "Do Laundry"
}
```
---
## /delete-task/{uid}

**Method:** DELETE

**Desc:** Delete a task based on it's uid

**Request Body:** -

**Fail message:**
```json
{"Data":"UID doesn't exists"}
```

**Response Body:**
```json
{
  "Data": "Has been deleted"
}
```
---
## /delete-task-by-title?title={taskTitle}

**Method:** DELETE

**Desc:** Delete a task based on it's title

**Request Body:** -

**Fail message:**
```json
{"Data":"Task title not found"}
```

**Response Body:**
```json
{
  "Data": "Has been deleted"
}
```