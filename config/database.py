from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')

db = client.cat_db

collection_name = db['cats_collection']