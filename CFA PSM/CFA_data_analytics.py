import statistics as st
import numpy as np
from numpy import average as av
import pandas as pd
import matplotlib.pyplot as plt
path = "C:\\Users\\juni\\Desktop\\"
data2 = pd.read_excel(path + "test.xlsx", sheet_name="Sheet1")
path3= "C:\\Users\\juni\\OneDrive - The Niederberger Net\\Ausbildung\\CFA\\Data Science\\"
data3= pd.read_excel(path3 + "Course 1 Module 4.xlsx", sheet_name="Histogram")
data4= pd.read_excel(path3 + "Course 1 Module 4.xlsx", sheet_name="Bar Chart")
data5= pd.read_excel(path3 + "Course 1 Module 4.xlsx", sheet_name="Pie Chart")
a=st.harmonic_mean(data2['data'])
b=av(data2['data'],weights=data2['weight'])
x=st.mean(data2['data'])
y=st.median(data2['data'])
z=st.mode(data2['data'])
#print("The weighted average is {}, the harmonic mean is {}, the mean is {}, the median is {}, and the mode is {}".format(b,round(a,2),round(x,1),y,z))
plt.hist(data3['Index Return'],bins=20)
#plt.show()
sector=data4['Sector']
frequency=data4['Freq']
plt.bar(sector,frequency,color=['blue','green','red','purple','orange','yellow','black','pink','brown','grey'])
#plt.show()
labels=data5['Sector']
sizes=data5['Freq']
colors=['blue','green','red','purple','orange','yellow','black','pink','brown','grey']
plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%',startangle=140)
circle=plt.Circle((0,0),0.7,color='white')
plt.gca().add_artist(circle)
plt.show()