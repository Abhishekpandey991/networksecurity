from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://abhishekpandey76840_db_user:<password>@cluster0.4pyoank.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri, server_api=ServerApi("1"))

try:
    client.admin.command("ping")
    print("Connected successfully!")
except Exception as e:
    print(e)