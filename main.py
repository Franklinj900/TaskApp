from fastapi import FastAPI
from database import create_task, get_all_task, get_one_task_id, update_task, delete_task, create_task
from models import Task

app = FastAPI()

@app.get('/')
def welcome():
    return {'message': 'Welcome to my FastAPI API'}

@app.get('/api/tasks')
async def get_tasks():
    tasks = await get_all_task()
    return tasks

@app.post('/api/tasks')
async def create_task(task: Task):
    print(task)
    return 'Created Task'
    

@app.get('/api/tasks/{id}')
def get_task(id: int):
    return 'single task'

@app.put('/api/tasks/{id}')
def update_task(id: int):
    return 'updating task'

@app.delete('/api/tasks/{id}')
def delete_task(id: int):
    return 'deleting task'