import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

db=client['11am']
user_col=db['emp']
user_col.update_one({'eid':1},{'$set':{'name':'Rahul Gandhi'}})
client.close()