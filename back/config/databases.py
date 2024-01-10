import json
import os
from pymongo import MongoClient
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

DB = os.environ["DB"]

client = MongoClient(f"mongodb+srv://{DB['user']}:{DB['password']}@myduoisok.gercpam.mongodb.net/?retryWrites=true&w=majority") 

db = client.myduoisok





