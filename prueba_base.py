from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://osegutierrez1607:Fr38850172@franklin.ic65u.mongodb.net/?retryWrites=true&w=majority&appName=Franklin"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
db = client.get_database('taskdatabase')
collection = db.get_collection('tasks')