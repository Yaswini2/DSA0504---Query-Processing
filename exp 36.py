import matplotlib.pyplot as plt

height1 = [150,155,160,165,170]
weight1 = [45,50,55,60,65]

height2 = [150,155,160,165,170]
weight2 = [50,55,60,65,70]

height3 = [150,155,160,165,170]
weight3 = [55,60,65,70,75]

plt.scatter(height1, weight1, label='Group 1')
plt.scatter(height2, weight2, label='Group 2')
plt.scatter(height3, weight3, label='Group 3')

plt.xlabel("Height")
plt.ylabel("Weight")
plt.title("Height vs Weight")

plt.legend()
plt.show()
