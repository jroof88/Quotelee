import os
import time
import datetime
from pytz import timezone
from pymongo import MongoClient

def get_mongo_conn():
    user = os.environ['MLAB_USER']
    password = os.environ['MLAB_PASSWORD']
    mlab_url = os.environ['MLAB_URL']
    return MongoClient("mongodb://"+user+":"+password+"@"+mlab_url+"/quotelee")

def get_collection(db, collection):
    client = get_mongo_conn()
    return client[db][collection]

def get_documents(db, collection):
    collection = get_collection(db, collection)
    return collection.find()

def load_result(returned_quote, number, input_text):
    collection = get_collection("quotelee", "results")
    #currDateTime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    currDateTime = datetime.now(timezone('US/Pacific')).strftime('%m-%d-%Y %H:%M')
    collection.insert({
        "input": input_text,
        "quote": returned_quote,
        "number": number,
        "datetime": currDateTime
    })
