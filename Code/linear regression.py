## Import the libraries first
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
    
#Read from file Inflation.xlsx.  
Path = "/Users/juergniederberger/GitHubSync/Py/Data"
df = pd.read_excel(Path+'Inflation.xlsx',sheet_name ='Inflation')

#The variable df is called  a dataframe. Check columns
df
#Assign X and Y from columns in the dataframe
X=df.Money_Supply
Y=df.Inflation
m, b = np.polyfit(X, Y, 1)
print("Slope: " + str(round(m,3)))
print("Constant: " + str(round(b,3)))
plt.plot(X, Y, 'o')
plt.plot(X,m*X+b,'red')
plt.xlabel('Money Supply %')
plt.ylabel('Inflation %')
#plt.show()

#Method 2, using OLS
X = df.Money_Supply
Y = df.Inflation
corr = X.corr(Y) 
print("Correlation is: "+ str(round(corr,3)))
rsquared = corr*corr
print("R-squared is: "+ str(round(rsquared,3)))

X = sm.add_constant(X) # adding a constant

model = sm.OLS(Y, X).fit()
model.summary()