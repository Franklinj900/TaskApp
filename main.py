from fastapi import FastAPI, HTTPException
from database import create_task, get_all_task, get_one_task_id, update_task, delete_task, create_task, get_one_task
from models import Task

app = FastAPI()

@app.get('/')
def welcome():
    return {'message': 'Welcome to my FastAPI API'}

@app.get('/api/tasks')
async def get_tasks():
    tasks = await get_all_task()
    return tasks

@app.post('/api/tasks', response_model=Task)
async def save_task(task: Task):
    task_found = await get_one_task(task.title)
    if task_found:
        raise HTTPException(409, 'Task already exists')
    
    response = await create_task(task.dict())
    if response:
        return response
    raise HTTPException(400, 'Something went wrong')

@app.get('/api/tasks/{id}')
def get_task(id: int):
    return 'single task'

@app.put('/api/tasks/{id}')
def update_task(id: int):
    return 'updating task'

@app.delete('/api/tasks/{id}')
def delete_task(id: int):
    return 'deleting task'