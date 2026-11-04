#matplot is a math visualistion tool
#pyplot used to create graphs
import matplotlib.pyplot as plt
days=[1,2,3,4,5,6,7]
temp=[19,20,14,17,22,25,9]
plt.figure(figsize=(8,5))
plt.plot(days,temp,color="Red",linestyle="--",marker="o",label="Tempreture",linewidth=2,markersize=8) # - for solid, -- for dash, : dotted, - . dash n dotted
plt.legend()
plt.grid(True)
plt.title("Tempreture Variation")                       # o = circle, s = square, * = star, ^ = triangle, + = cross
plt.xlabel("Days")
plt.ylabel("Tempreture")
plt.show()
###
