import numpy as np
array=np.array([6,3,12,35,75,1,999,72,13,69,54,9])
print(array[0:5])
#[0,1,2,3]
print(array[:-5])
print(array[::3])
print(array[::-1])
####
m=np.arange(49).reshape(7,7)
middle3=m[2:5,2:5]
row1=m[0,:]
col7=m[:,-1]
print('Middle 3x3: \n',middle3)
print('First row: ',row1)
print('Last column: ',col7)