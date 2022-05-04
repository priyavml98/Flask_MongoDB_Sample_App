

from flask import Flask, jsonify, render_template ,request
from trial import *
from showone import *
from add import *

app=Flask(__name__)
s=h()

@app.route('/')
def hello():
    
    return render_template("index.html")
@app.route('/function')
def func():
    
    return render_template("trial.html",s=s)

@app.route('/trial')

def trial():
    
    
    return render_template("json.html",s=s)

@app.route('/findone')
def findone():
    name=request.args.get('one')
    d=showone(name)
    
    return render_template("findone.html",d=d)
@app.route('/add')
def add():
    
    
    return render_template("adddata.html")
@app.route('/addone')
def addone():
    name=request.args.get('one')
    age=request.args.get('two')
    gender=request.args.get('three')
    ok=addon(name,age,gender)
    

    return render_template("adddata.html")



if __name__=='__main__':
    app.run()
    