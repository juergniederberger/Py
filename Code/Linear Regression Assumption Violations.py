import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the Income_Data.xlsx file in a dataframe variable called dincome.
# File name is: Income_Data.xlsx and sheet name is: Data

path='/Users/juergniederberger/GitHubSync/Py/Data/'
dincome=pd.read_excel(path+'Income_Data.xlsx',sheet_name='Data')
dincome

# Building on the previous example of loading a dataframe, assign independent and dependent variables,
# create a linear regressor, then fit the model.
# Finally, print the coefficients and intercept.
# Note that coefficient term is referred to by: coef_
# Note that intercept term is referred to as intercept_

# The first steps are done for you; your work is to write the code statements to fit the model and print the coefficients and intercept

# Assign independent variables, Education_Years and Age columns to variable X
X=dincome[['Education_Years', 'Age']]
# Assign dependent variable, Annual_Income to Y
Y=dincome[['Annual_Income']]
# Call a regressor
Regressor = LinearRegression()
## You have called the Regressor, now fit the model (or train it) using the Regressor function
## If in doubt, check illustrative code used in this lesson
## Syntax is Regressor.fit(Independent_Variable,Dependent_Variable)

# Type your code for fitting the model below this comment. Use the "Run" button on the tool bar above to run all the cell's code

# Type your code for printing the coefficients below this comment.

# Type your code for printing the intercept below this comment.
