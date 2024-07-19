import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

x=np.array([0.01,0.019,0.04,0.07,0.14,0.27,0.52,0.53,0.55,0.6,0.65,0.66,0.7,0.715,0.8,0.85]) #ROE
y=np.array([1.79,1.82,3.2,5.31,6.75,6.8,8.86,5,5.5,8.8,8.9,6.6,9.02,9.03,9.03,9.03]) #PB Ration
x_test=np.linspace(-0.2,0.85,1000)

plt.scatter(x,y, marker='o', color='r')
plt.xlabel('ROE %')
plt.ylabel('Price/Book Ratio')

plt.show()

titles = ['d = 1 (under-fit, high bias)',
          'd = 2',
          'd = 4 (over-fit, high variance)']
degrees = [1, 2, 4]

fig = plt.figure(figsize=(9, 3.5))
fig.subplots_adjust(left=0.06, right=0.98, bottom=0.15, top=0.85, wspace=0.05)

for i, d in enumerate(degrees):
    ax = fig.add_subplot(131 + i, xticks=[], yticks=[])
    ax.scatter(x, y, marker='x', color='k', s=50)
    model = make_pipeline(PolynomialFeatures(d), LinearRegression())
    model.fit(x[:, np.newaxis], y)
    y_test = model.predict(x_test[:, np.newaxis])
    ax.plot(x_test, y_test, linewidth=2)
    ax.set_xlim(-0.2, 1.2)
    ax.set_ylim(0, 10) 
    ax.set_xlabel('ROE %')
    if i == 0:
        ax.set_ylabel('PB')
    ax.set_title(titles[i])