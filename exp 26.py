import matplotlib.pyplot as plt

x = [1,2,3,4,5]

plt.subplot(2,2,1)
plt.plot(x, [1,2,3,4,5])
plt.title("Plot 1")

plt.subplot(2,2,2)
plt.bar(x, [5,4,3,2,1])
plt.title("Plot 2")

plt.subplot(2,2,3)
plt.scatter(x, [2,4,1,5,3])
plt.title("Plot 3")

plt.subplot(2,2,4)
plt.plot(x, [5,3,4,2,1])
plt.title("Plot 4")

plt.tight_layout()
plt.show()
