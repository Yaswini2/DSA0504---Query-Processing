import matplotlib.pyplot as plt
import random

x = [random.random() for i in range(50)]
y = [random.random() for i in range(50)]

plt.scatter(x, y, facecolors='none', edgecolors='blue')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot with Empty Circles")

plt.show()
