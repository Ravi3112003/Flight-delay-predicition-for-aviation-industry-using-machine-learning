#Importing Liabraries

from flask import Flask,render_template,request

import pickle
import numpy as np

model = pickle.load(open('flight.pkl','rb')
                    
app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")


@app.route('/prediction',methods =['post'])
def predict():
    name = request.form['name']
    month = request.form['month']
    dayofmonth = request.form['dayofmonth']
    dayofweek = request.form['dayofweek']
    origin = request.form['origin']
    if(origin == "msp"):
        origin1,origin2,origin3,origin4,origin5 = 0,0,0,0,1
    if(origin =="dtw"):
        origin1,origin2,origin3,origin4,origin5 = 1,0,0,0,0
    if(origin =="jfk"):
        origin1,origin2,origin3,origin4,origin5 = 0,0,1,0,0
    if(origin =="sea"):
        origin1,origin2,origin3,origin4,origin5 = 0,1.0,0,0
    if(origin =="alt"):
        origin1,origin2,origin3,origin4,origin5 = 0,0,0,1,0
        
    destination = request.forrm['destination']
    if(destinatio == "msp"):
        destinatio1,destinatio2,destinatio3,destinatio4,destinatio5 = 0,0,0,0,1
    if(destination =="dtw"):
        destinatio1,destinatio2,destinatio3,destinatio4,destinatio5 = 1,0,0,0,0
    if(destination =="jfk"):
        destinatio1,destinatio2,destinatio3,destinatio4,destinatio5 = 0,0,1,0,0
    if(destination =="sea"):
        destinatio1,destinatio2,destinatio3,destinatio4,destinatio5 = 0,1,0,0,0
    if(destination =="alt"):
        destinatio1,destinatio2,destinatio3,destinatio4,destinatio5 = 0,0,0,1,0
    dept = request.form['dept']
    arrtime = request.form['arrtime']
    actdept = request.form['actdept']
    dept15=int(dept)-int(actdept)
    total = [[name, month,dayofmonth,dayofweek,origin1,origin2,origin3,origin4,origin,destinatio1,destinatio2,destinatio3,destinatio4,destinatio5]]
    #print(total)
    y_pred = model.predict(total)
    
    print(y_pred)
    
    if(y_pred==[0.]):
        ans="The Flight will be on time"
    else:
        ans="The Flight will be on delayed"
    return render_template("index.html",showcase = ans)

if__name__ = '__main__':
   app.run(debug = False) 