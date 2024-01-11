import json
import os
from pymongo import MongoClient
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

DB_USER=os.environ["DB_USER"]
DB_PASSWORD=os.environ["DB_PASSWORD"]
DB_HOST=os.environ["DB_HOST"]
DB_PORT=os.environ["DB_PORT"]
DB_DATABASE=os.environ["DB_DATABASE"]

client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@myduoisok.gercpam.mongodb.net/?retryWrites=true&w=majority") 

db = client.myduoisok





