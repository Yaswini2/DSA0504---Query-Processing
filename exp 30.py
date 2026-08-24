import matplotlib.pyplot as plt
import numpy as np

groups = ['Group 1','Group 2','Group 3','Group 4','Group 5']

men = [22,30,35,35,26]
women = [25,32,30,35,29]

x = np.arange(len(groups))
width = 0.35

plt.bar(x - width/2, men, width, label='Men')
plt.bar(x + width/2, women, width, label='Women')

plt.xticks(x, groups)
plt.xlabel("Groups")
plt.ylabel("Scores")
plt.title("Scores by Group and Gender")

plt.legend()
plt.show()
