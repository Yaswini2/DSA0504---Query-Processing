import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Random Scatter Plot")

plt.show()
