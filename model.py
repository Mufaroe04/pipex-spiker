import pandas as pd 
import numpy as np
import pandas as pd
from pandas import read_csv
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing  import Imputer
#import pickle
def prediction(dat):
    soccer=pd.read_csv('players_20.csv')
    X=soccer[['pace','shooting','passing','dribbling','defending','physic','international_reputation']]
    y=soccer['overall']
    
    imputer =Imputer(strategy="median")
    
    X.median()
    imputer.fit(X) # its learning the median calculation
    
    X=imputer.transform(X)
    
    
# creating a new data frame with no missing values
    X_non=pd.DataFrame(X,columns=['pace','shooting','passing','dribbling','defending','physic','international_reputation'])
    scale=MinMaxScaler()
    prop=scale.fit_transform(dat)
    Xx=scale.fit_transform(X_non)
    Xtrain,Xtest,Ytrain,Ytest=train_test_split(Xx,y,train_size=0.2,random_state=42)
    tree_reg = DecisionTreeRegressor()
    tree_reg.fit(Xtrain, Ytrain)
    tree_reg.predict(prop)
    #pickle.dump(tree_reg,open('model.pkl','wb'))
    #model=pickle.load(open('model.pkl','rb'))
    #print(model.predict(prop))
    
    
   

