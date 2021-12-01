from flask import Flask,render_template,request,url_for
import model as m
import pandas as pd
#import pickle
import numpy as np
app=Flask(__name__,template_folder='templates')
#model=pickle.load(open('model.pkl','rb'))
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sub",methods=["POST"])
def pred():
    if request.method=="POST":
        pace=request.form["pace"]
        shooting=request.form["shooting"]
        passing=request.form["passing"]
        dribbling=request.form["dribbling"]
        defending=request.form["defending"]
        physic=request.form["physic"]
        international_reputation=request.form["international_reputation"]
        dat=[pace,shooting,passing,dribbling,defending,physic,international_reputation]
        #df=pd.DataFrame([dat],columns=['pace','shooting','passing','dribbling','defending','physic','international_reputation'])
        df=np.array(dat)
        df=df.reshape((1,-1))
    
        pre=m.prediction(df)
        
      
        #pre=67
        #print(pre)
    return render_template("sub.html",text=pre)
    print(pre)
if __name__=="__main__":
    app.run(debug=True)
        
 