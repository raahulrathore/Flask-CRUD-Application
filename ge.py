import pymongo
import requests
import json, bson
import random
from flask import Flask, jsonify, request, make_response
from flask_pymongo import PyMongo
from flask_cors import CORS
from pymongo import MongoClient
from flask_mongoengine import MongoEngine
from bson import json_util

client = MongoClient("mongodb+srv://GDuser:GDuser@cluster0.fifzk.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = client.get_database('data1')
records = db.products
app = Flask(__name__)
CORS(app)   # This will enable CORS for all routes

app.config['MONGO_DBNAME'] = 'data1' # Name of database on mongo
app.config["MONGO_URI"] = "mongodb+srv://GDuser:GDuser@cluster0.fifzk.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority" #URI to Atlas cluster  + Auth Credentials

mongo = PyMongo(app)
db = MongoEngine()
db.init_app(app)
allow_inheritance = False 

class Product(db.Document):
    name=db.StringField()
    brand_name=db.StringField()
    regular_price_value=db.IntField()
    offer_price_value=db.IntField()
    currency=db.StringField()
    classification_l1=db.StringField()
    classification_l2=db.StringField()
    classification_l3=db.StringField()
    classification_l4=db.StringField()
    image_url=db.StringField()
   
    def to_json(self):
       return{
    "name" : self.name,
    "brand_name":self.brand_name,
    "regular_price_value":self.regular_price_value,
    "offer_price_value":self.offer_price_value,
    "currency":self.currency,
    "classification_l1":self.classification_l1,
    "classification_l2":self.classification_l2,
    "classification_l3":self.classification_l3,
    "classification_l4":self.classification_l4,
    "image_url":self.image_url
       }

@app.route('/') 
def hello(): 
    return "Connection to the Server Made Sucessfully!!"

@app.route('/putdata/', methods=['GET','POST'])  # Put the data in my collection
def db_popu():
    product1 = [{'name' :'Rahul','brand_name':'Rathore','regular_price_value':'10','offer_price_value':5,
    'currency':"Dollor",
    'classification_l1':"rEAL",
    'classification_l2':"hP",
    'classification_l3':"rEDMI",
    'classification_l4':"aMAZON",
    'image_url':"DAKS.COM"}]
    
    records.insert_many(product1)
    return make_response("VALUE INSERTED SUCESSFULLY!!",200)
    
@app.route('/getdata/', methods=['GET'])  # Find all data in my collection
def get_all_data():
    output = []
    for z in records.find():   
        output.append({'Name':z['name'],'Brand Name' : z['brand_name'],'Currency':z['currency'],'Regular Price':z['regular_price_value'],'Offer Value':z['offer_price_value'], 'Category': z['classification_l1']})
    return jsonify({'The Products are ':output})

@app.route('/update/', methods= ['GET','POST'])
def data_update():
    student_update = {'name' : 'Santosh'}
    records.update_one({'brand_name':'Rathore'},{'$set':student_update})
                                      
    return make_response("Value Updated Sucessfully!!", 200)
        
@app.route('/delete/',methods =['GET','POST','DELETE'])  
def data_delete():
    records.delete_one({'name':'Santosh'})
    return make_response("Product Entry Deleted",200)
    
if __name__ == '__main__':
    app.run(host ='0.0.0.0',debug=True,port= 5001)