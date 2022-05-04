from flask import Flask , jsonify
import json
from flask_pymongo import PyMongo

app=Flask(__name__)
app.config["MONGO_URI"]="mongodb://localhost:27017/person"
mongo=PyMongo(app)



def h():
  a=[]
  c= list(mongo.db.collection.find({},{"_id":0}))


   

  return c






