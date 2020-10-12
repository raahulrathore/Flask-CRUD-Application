#importing dataset first in python
import json
#opening and looking
with open('D:/4th Year/GREENDECK/data.json') as d:
    data = json.load(d)
#printing the data to chec sucessful fetch
print((data))
#importing mongoclient to work with mongo
from pymongo import MongoClient
#establishing cnxxtn
client = MongoClient('mongodb+srv://GDuser:GDuser@cluster0.fifzk.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority')
#naming the database as data1
db = client.data1
#creating collection named products in db
products =db.products
#insrting the data imported to collection 
products.insert_many(data)

