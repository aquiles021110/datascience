import numpy as np
m1=np.array([[12,34,13],[5,776,86]])
m2=np.array([[64,352,897],[123,44,7]])
op=str(input('enter operation:\n'))
if op=='+':
    print(m1+m2)
elif op=='-':
    print(m1-m2)
else:
    print('unkown operator')
###
print('###')
a1=np.arange(16)
print(a1)
print(a1[a1<8],f'Values:{len(a1[a1<8])}')
print(a1[a1>=10],f'Values:{len(a1[a1>=10])}')
print(a1[a1%2!=0],f'Values:{len(a1[a1%2!=0])}')
print('###')
###
m3=np.arange(1,10).reshape(3,3)
m4=np.arange(10,19).reshape(3,3)
print(m3)
print(m4)
p=m3*m4
matrixmul=m3@m4
print(p)
print(matrixmul)
###
mat1=np.array([[1,1],[1,1]])
mat2=np.arange(1,5).reshape(2,2)
print(mat1@mat2)
print(mat1*mat2)
