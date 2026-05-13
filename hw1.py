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