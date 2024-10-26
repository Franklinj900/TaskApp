from fastapi import FastAPI
from routes.task import task
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

app = FastAPI()

origins = [
    config('FRONTEND_URL')  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Ajusta esto según sea necesario
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def welcome():
    return {'message': 'Welcome to my FastAPI API'}

app.include_router(task)