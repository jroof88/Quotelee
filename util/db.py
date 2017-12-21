import time
import datetime
from pymongo import MongoClient

def get_mongo_conn():
    return MongoClient("mongodb://jawnroof:88orange88@ds131826.mlab.com:31826/quotelee")

def get_collection(db, collection):
    client = get_mongo_conn()
    return client[db][collection]

def get_documents(db, collection):
    collection = get_collection(db, collection)
    return collection.find()

def load_result(returned_quote, number, input_text):
    collection = get_collection("quotelee", "results")
    currTime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    collection.insert({
        "input": input_text,
        "quote": returned_quote,
        "number": number,
        "datetime": currTime
    })
