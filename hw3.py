import matplotlib.pyplot as plt
print('Part 1')
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]
plt.plot(x,y,color='Red',marker='o')
plt.grid(True)
plt.title("f(x)=y")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
print('Part 2')
subjects = [1, 2, 3, 4, 5]
student_A = [80, 75, 90, 85, 95]
student_B = [70, 85, 80, 90, 88]
plt.plot(subjects,student_A)
plt.plot(subjects,student_B)
plt.show()