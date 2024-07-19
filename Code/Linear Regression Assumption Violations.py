# Update to test sync
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Load the Income_Data.xlsx file in a dataframe variable called dincome.
# File name is: Income_Data.xlsx and sheet name is: Data

#path='/Users/juergniederberger/GitHubSync/Py/Data/'
path='/workspaces/Py/Data/'
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
Regressor.fit(X,Y)
# Type your code for fitting the model below this comment. Use the "Run" button on the tool bar above to run all the cell's code

# Type your code for printing the coefficients below this comment.
print("Coefficients: " + str(Regressor.coef_))
# Type your code for printing the intercept below this comment.
print("Intercept: " + str(Regressor.intercept_))

# Generate a grid of points for the surface plot
x1_range = X['Education_Years'].min(), X['Education_Years'].max()
x2_range = X['Age'].min(), X['Age'].max()
x1_values = np.linspace(x1_range[0], x1_range[1], 100)
x2_values = np.linspace(x2_range[0], x2_range[1], 100)
X1, X2 = np.meshgrid(x1_values, x2_values)
X_grid = np.column_stack((X1.ravel(), X2.ravel()))

# Predict the dependent variable for the grid of points
y_pred = Regressor.predict(X_grid)

# Create a 3D plot of the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X['Education_Years'], X['Age'], Y, c='r', marker='o')
ax.plot_surface(X1, X2, y_pred.reshape(X1.shape), alpha=0.5)
ax.set_xlabel('Education_Years')
ax.set_ylabel('Age')
ax.set_zlabel('Annual_Income')
plt.show()