

from flask import Flask, jsonify, render_template ,request
from trial import *
from showone import *

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
if __name__=='__main__':
    app.run()
    