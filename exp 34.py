import matplotlib.pyplot as plt
import random

x = [random.random() for i in range(50)]
y = [random.random() for i in range(50)]

sizes = [random.randint(20, 500) for i in range(50)]

plt.scatter(x, y, s=sizes, alpha=0.5)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot with Different Ball Sizes")

plt.show()
