#select all the even elements from an array
import numpy as np
import random
a=np.array([1,2,3,4,5,6,7,8,9,10])
even=a[a%2==0]
print(even)
barray=a[a==5]
print(barray)
#selection by indexes
print(a[[2,4,6]])
less=a[a<5]
print(less)
l=[1,2,3,4,5,6,7,8,9,10]
for i in range(len(l)):
    l[i]+=1
print(l)
print(a+1)
m1=np.random.permutation(np.arange(16).reshape(4,4))
m2=np.random.permutation(np.arange(16).reshape(4,4))
print(m1)
print(m2)
###
#create function for numpy operation
#y=2x+3
def sol(k):
    return 2*k+3
x=np.arange(5)
y=sol(x)
print(y)