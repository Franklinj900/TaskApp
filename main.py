from fastapi import FastAPI, HTTPException
from database import create_task, get_all_task, get_one_task_id, update_task, delete_task, create_task, get_one_task, get_one_task_id
from models import Task, UpdateTask

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

@app.get('/api/tasks/{id}', response_model=Task)
async def get_task(id: str):
    task = await get_one_task_id(id)
    if task:
        return task
    raise HTTPException(404, f'Task not found with id: {id}')

@app.put('/api/tasks/{id}', response_model=Task)
async def put_task(id: str, task: UpdateTask):
    task = await update_task(id, task)   
    if task:
        return task
    raise HTTPException(404, f'Task not found with id: {id}')

@app.delete('/api/tasks/{id}')
async def remove_task(id: str):
    task = await delete_task(id)
    if task:
        return "successfully deleted task"
    raise HTTPException(404, f'Task not found with id: {id}')