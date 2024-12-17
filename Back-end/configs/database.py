# -*- coding: utf-8 -*-
import certifi
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://nth280102:7OdtNBPIPnYhVFW0@laptrinhmang.ettscrh.mongodb.net/?retryWrites=true&w=majority&appName=LapTrinhMang"
client = MongoClient(
    uri,
    tlsCAFile=certifi.where()
)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client.LapTrinhMang

user_collection = db["Users"]
message_collection = db["Messages"]
dialog_collection = db["Dialogs"]
call_collection = db["Calls"]
