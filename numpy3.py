import numpy as np
print('Matrix addition or subtraction?')
op=str(input())
rows=int(input('Number of rows:\n'))
columns=int(input('Number of columns:\n'))
matrixa=[]
for i in range(rows):
    row=input('Input elements in row:\n').split()
    for j in range(columns):
        row[j]=int(row[j])
    matrixa.append(row)
print('###  Matrix B  ###')
matrixb=[]
for i in range(rows):
    row=input('Input elements in row:\n').split()
    for j in range(columns):
        row[j]=int(row[j])
    matrixb.append(row)
a=np.array(matrixa)
b=np.array(matrixb)
if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
else:
    print('unkown operator')