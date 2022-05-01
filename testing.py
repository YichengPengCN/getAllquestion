import csv
import pymongo
import urllib.parse

# set up local db, just for testing, need to refine for backend
# "mongodb+srv://3170Project2:fit3170@cluster0.8wuog.mongodb.net/FIT3170?retryWrites=true&w=majority"
client = pymongo.MongoClient()
db = client["FIT3170"]
collection = db["TagInfo"]

for document in collection.find():
    print (document)
