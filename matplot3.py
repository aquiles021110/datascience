import matplotlib.pyplot as plt
import pandas as pd
f=pd.read_csv('titanic.csv')
#ex
x=[1,3,5,7]
y=[2,4,6,8]
plt.bar(x,y,color='b')
plt.show()
###
y1=f['Pclass'].value_counts().sort_index()
plt.bar(y1.index,y1,color='red')
plt.xticks([1,2,3])
plt.show()
###
t=f['Survived'].value_counts()
plt.bar(t.index,t)
plt.xticks([0,1])
plt.show()
###
ages=[21,21,30,40,18,15,16,16,17,19,20,20,19,14,15,25,22,23,22,24,22,20,19,18]
bins=[14,16,18,20,22,24,26,28,30,32,34,36,38,40]
plt.hist(ages,bins,histtype="bar",rwidth=0.8)
plt.xlabel('Bins')
plt.ylabel('Freq.')
plt.title('Histogram')
plt.show()
### scatterplot
x=[1,2,6,4,12,22,19,18,16,17]
y=[0,1,0,1,0,1,0,1,0,1]
plt.scatter(x,y,color='red')
plt.show()
### piechart (a-c)
slices=[19.7,44.6,12.4,5.2,12]
activites=['Sleeping','School','Eating','Homework','Free time']
colours=['b','m','r','c','g']
plt.pie(slices,labels=activites,colors=colours,startangle=90)
plt.show()
