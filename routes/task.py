from fastapi import APIRouter, HTTPException
from models import Task, UpdateTask
from database import get_all_task, get_one_task, get_one_task_id, create_task, update_task, delete_task,delete_all_task


task = APIRouter()

@task.get('/api/tasks')
async def get_tasks():
    tasks = await get_all_task()
    return tasks

@task.post('/api/tasks', response_model=Task)
async def save_task(task: Task):
    task_found = await get_one_task(task.title)
    if task_found:
        raise HTTPException(409, 'Task already exists')
    
    response = await create_task(task.dict())
    if response:
        return response
    raise HTTPException(400, 'Something went wrong')


@task.get('/api/tasks/{id}', response_model=Task)
async def get_task(id: str):
    task = await get_one_task_id(id)
    if task:
        return task
    raise HTTPException(404, f'Task not found with id: {id}')

@task.put('/api/tasks/{id}', response_model=Task)
async def put_task(id: str, task: UpdateTask):
    task = await update_task(id, task)   
    if task:
        return task
    raise HTTPException(404, f'Task not found with id: {id}')

@task.delete('/api/tasks/{id}')
async def remove_task(id: str):
    task = await delete_task(id)
    if task:
        return "successfully deleted task"
    raise HTTPException(404, f'Task not found with id: {id}')

@task.delete('/api/tasks')
async def remove_all_task():
    task = await delete_all_task()
    if task:
        return "successfully deleted all tasks"
    raise HTTPException(404, f'Task not found')