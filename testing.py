import csv
import pymongo
import urllib.parse

# set up local db, just for testing, need to refine for backend
# "mongodb+srv://3170Project2:fit3170@cluster0.8wuog.mongodb.net/FIT3170?retryWrites=true&w=majority"
client = pymongo.MongoClient('mongodb://52.62.92.51:27017')
print(client.list_database_names())
