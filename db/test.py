import pymongo

mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

db = mongo_client['wjj']  # use wjj

table = db.test  #  db.test

table.insert_many([{'name':'zy','age':'70'},{'name':'wjj','age':'18'}])

print(table.find_one({'age':'18'})) 