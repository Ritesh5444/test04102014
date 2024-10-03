import pymongo
client = pymongo.MongoClient("mongodb+srv://Ritesh1212:Ritesh123@cluster0.hzs0x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.test
print(db)

d = {'name':'Ritesh','Id': 'ritesh@gmail.com','surname' : 'kumar'}
d = {'name':'Ritesh','Id': 'ritesh@gmail.com','surname' : 'kumar'}
d = {'name':'Ritesh','Id': 'ritesh@gmail.com','surname' : 'kumar'}
d = {'name':'Ritesh','Id': 'ritesh@gmail.com','surname' : 'kumar'}


db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)