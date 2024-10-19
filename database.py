from motor.motor_asyncio import AsyncIOMotorClient
from models import Task


client = AsyncIOMotorClient('mongodb+srv://osegutierrez1607:Fr38850172@cluster0.ic65u.mongodb.net/')
database = client.taskdatabase
collection = database.tasks


async def get_one_task_id(id):
    task = await collection.find_one({"_id": id})
    return task



async def get_one_task(title):
    task = await collection.find_one({"title": title})
    return task

async def get_all_task():
    tasks = []
    cursor = collection.find({})
    async for document in cursor:
        tasks.append(Task(**document))
    return tasks


async def create_task(task):
    new_task = await collection.insert_one(task)
    created_task = await collection.find_one({"_id": new_task.inserted_id})
    return created_task

async def update_task(id:str, task):
    await collection.update_one({'_id': id}, {'$set': task})
    updated_task = await collection.find_one({"_id": id})
    return updated_task

async def delete_task(id:str):
    await collection.delete_one({"_id": id})
    return True



