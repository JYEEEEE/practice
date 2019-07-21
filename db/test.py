import pymongo

mongo_client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

db = mongo_client['wjj']  # use wjj
print(db)
table = db.test  #  db.test
#
table.insert_many([{'name':'zy','age':'70'},{'name':'wjj','age':'18'}])
# print(table.insert_one({'name':'zy','age':'70'}))
result = table.find_one({'age':'18'})
print(result, type(result))

# if not result:
#     # result : None, 0, False, [], {}
#     print('no')

# if result is None:
#     # result : None
#     print('no 2')
