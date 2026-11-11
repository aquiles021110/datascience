import matplotlib.pyplot as plt
import numpy as np
a=np.arange(0,10,0.2)
print(a)
y1=a**2
y2=a**3
plt.plot(a,y1,color='Green')
plt.plot(a,y2,color='Red')
plt.show()
m=float(input('Input m:'))
c=float(input('Input c:'))
y3=m*a+c
plt.plot(a,y3)
plt.show()