import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

Path = "/Users/juergniederberger/GitHubSync/Py/Data/"
dcredit = pd.read_excel(Path+'Helper_Data.xlsx',sheet_name ='Credit Profile')

Xtrain = dcredit[['Annual_Income', 'Education_Years', 'Age']]
ytrain = dcredit[['Credit_Profile']]

logreg = sm.Logit(ytrain, Xtrain).fit()
print(logreg.summary())

xdata = {'Annual_Income':[110000,42000,95000,90000,100000],
        'Education_Years':[10,10,16,20,30],
        'Age':[30,27,28,40,50]}
ydata = {'Credit_Profile':[1,0,1,1,0 ]}

xtest = pd.DataFrame(xdata)
ytest = pd.DataFrame(ydata)

# performing predictions on the test datdaset
ypredict = logreg.predict(xtest)
print (ypredict)
predictions = list(map(round, ypredict))


print('Acutal values', list(ytest.Credit_Profile))
print('Predictions :', predictions)

from sklearn.metrics import (confusion_matrix, accuracy_score)
  
# confusion matrix
cm = confusion_matrix(ytest.Credit_Profile, predictions) 
print ("Confusion Matrix : \n", cm) 
  
# accuracy score of the model
print('Test accuracy = ', accuracy_score(ytest.Credit_Profile, predictions))
