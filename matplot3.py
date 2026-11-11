import matplotlib.pyplot as plt
import pandas as pd
f=pd.read_csv('titanic.csv')
#ex
x=[1,3,5,7]
y=[2,4,6,8]
plt.bar(x,y,color='b')
plt.show()
###
x=f['Pclass']
print(x)