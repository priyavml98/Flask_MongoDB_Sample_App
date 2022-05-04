
from trial import *

s=h()

def addon(name,age,gender):
    d={}
    d['name']=name
    d['age']=age
    d['gender']=gender

    mongo.db.collection.insert_one(d)
    print(d)
    return 'success' 