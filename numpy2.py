import numpy as np
def create_m(row,column):
    matrix=[]
    print('Matrix')
    for i in range(row):
        rowl=[]
        for i in range(column):
            element=int(input('Enter element:'))
            rowl.append(element)
        matrix.append(rowl)
    return matrix
print('#1')
m1r=int(input('Input number of rows:\n'))
m1c=int(input('Input number of columns:\n'))
m1=create_m(m1r,m1c)
print('#2')
m2=create_m(m1r,m1c)
op=str(input('Enter operation:\n'))
if op=='+':
    matrixres=[]
    for i in range(len(m1)):
        rowlist=[]
        for j in range(len(m1[0])):
            rowlist.append(m1[i][j]+m2[i][j])
        matrixres.append(rowlist)
    print(matrixres)    
elif op=='-':
    matrixres=[]
    for i in range(len(m1)):
        rowlist=[]
        for j in range(len(m1[0])):
            rowlist.append(m1[i][j]-m2[i][j])
        matrixres.append(rowlist)
    print(matrixres)    
else:
    print('unkown operator')
