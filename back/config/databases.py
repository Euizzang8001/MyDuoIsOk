import json
import os
from pymongo import MongoClient

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_FILE = os.path.join(BASE_DIR, 'secret.json')
secrets = json.loads(open(SECRET_FILE).read())
DB = secrets["DB"]

client = MongoClient(f"mongodb+srv://{DB['user']}:{DB['password']}@myduoisok.gercpam.mongodb.net/?retryWrites=true&w=majority") 

db = client.myduoisok





