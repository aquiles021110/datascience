#numpy=numerical python
#library
import numpy as np
nlist=[123,43,56,131,12]
plist=[]
for i in nlist:
    plist.append(i+10)
print(plist)
#numpy
a1=np.array([123,43,56,131,12])
print(a1+10)
#effects the whole array
#more efficent for larger samples
#can still use indexing
a2=np.array([1,2,3,4,5])
print(a2)
print(a2.shape)
#.shape returns number of columns and rows
print(a2*3)
print(a2/3)

a3=np.zeros(5)
print(a3)

a4=np.ones(9)
print(a4)

a5=np.arange(1,10)
print(a5)
#ending point is n-1 
#10= ending point 9
#2d array is matrix
m1=np.array([[1,2,3],[4,5,6]])
print(m1)
#avg.
print(a5.mean())
array1=np.array([20,18,18,14,9,12,17.5])
print(array1.mean())
print(array1.max())
print(array1.min())
#to add two arrays, they must be of same shape(size)
print(a5+a4)
#number of dimensions
print(m1.ndim)
#total number of element
print(m1.size)
#total mem. used by array in bytes
print(m1.nbytes)