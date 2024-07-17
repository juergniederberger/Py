import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt

# Read the data from the Excel sheet
Path = "/Users/juergniederberger/GitHubSync/Py/Data"
data = pd.read_excel(Path+'For ANOVA.xlsx')
#data = pd.read_excel('/path/to/your/excel_file.xlsx')

# Extract the dependent and independent variables
X = data[['Interest_Rate', 'Unemployment_Rate']]
y = data['Index_Price']

# Perform multiple linear regression
regression_model = LinearRegression()
regression_model.fit(X, y)

# Generate a grid of points for the surface plot
x1_range = X['Interest_Rate'].min(), X['Interest_Rate'].max()
x2_range = X['Unemployment_Rate'].min(), X['Unemployment_Rate'].max()
x1_values = np.linspace(x1_range[0], x1_range[1], 100)
x2_values = np.linspace(x2_range[0], x2_range[1], 100)
X1, X2 = np.meshgrid(x1_values, x2_values)
X_grid = np.column_stack((X1.ravel(), X2.ravel()))

# Predict the dependent variable for the grid of points
y_pred = regression_model.predict(X_grid)

# Create a 3D plot of the surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X['Interest_Rate'], X['Unemployment_Rate'], y, c='r', marker='o')
ax.plot_surface(X1, X2, y_pred.reshape(X1.shape), alpha=0.5)
ax.set_xlabel('Interest Rate')
ax.set_ylabel('Unemployment Rate')
ax.set_zlabel('Index Level')
plt.show()

# ## Import the libraries first
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import statsmodels.api as sm
# from sklearn.linear_model import LinearRegression
	
# #Read from file Inflation.xlsx.  
# Path = "/Users/juergniederberger/GitHubSync/Py/"
# df = pd.read_excel(Path+'For ANOVA.xlsx')

# #The variable df is called  a dataframe. Check columns
# #df

# #Method 1, using OLS
# X = df[['Interest_Rate','Unemployment_Rate']]
# Y = df.Index_Price
# X = sm.add_constant(X) # adding a constant
# olsresult = sm.OLS(Y, X).fit()
# olsresult.summary()

# #Method 2, using sklearn
# Regressor = LinearRegression()
# Regressor.fit(X,Y)

# # print("Coefficients: " + str(Regressor.coef_))
# # print("Intercept: " + str(Regressor.intercept_))

# #Visualization
# # x_surf, y_surf = np.meshgrid(np.linspace(X.Interest_Rate.min(), X.Interest_Rate.max(), 100),np.linspace(X.Unemployment_Rate.min(), X.Unemployment_Rate.max(), 100))
# # Xvalues = pd.DataFrame({'Interest_Rate': x_surf.ravel(), 'Unemployment_Rate': y_surf.ravel()})

# # Xvalues['const'] = 1
# # fittedY=Regressor.predict(Xvalues)
# # fittedY=np.array(fittedY)

# # fig=plt.figure(figsize=(20,10))
# # ax=fig.add_subplot(111,projection='3d')
# # ax.scatter(X.Interest_Rate,X.Unemployment_Rate,Y,c='blue',marker='o',alpha=0.5)
# # ax.plot_surface(x_surf,y_surf,fittedY.reshape(x_surf.shape),color='green',alpha=0.3)
# # ax.set_xlabel('Interest Rate')
# # ax.set_ylabel('Unemployment Rate')
# # ax.set_zlabel('Stock Index Price')
# # plt.show()

# #Visualization
# x_surf, y_surf = np.meshgrid(np.linspace(X.Interest_Rate.min(), X.Interest_Rate.max(), 100),np.linspace(X.Unemployment_Rate.min(), X.Unemployment_Rate.max(), 100))
# Xvalues = pd.DataFrame({'Interest_Rate': x_surf.ravel(), 'Unemployment_Rate': y_surf.ravel()})
 
# Xvalues['const'] = 1
# fittedY=Regressor.predict(Xvalues)
# fittedY=np.array(fittedY)
 
# fig = plt.figure(figsize=(20,10))
# ### Set figure size
# ax = fig.add_subplot(111, projection='3d')
# ax.scatter(X['Interest_Rate'],X['Unemployment_Rate'],Y['Index_Price'],c='red', marker='o', alpha=0.5)
# ax.plot_surface(x_surf,y_surf,fittedY.reshape(x_surf.shape), color='g', alpha=0.3)
# ax.set_xlabel('Interest Rate')
# ax.set_ylabel('Unemployment Rate')
# ax.set_zlabel('Index Level')
# plt.show()
