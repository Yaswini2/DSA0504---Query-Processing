import matplotlib.pyplot as plt
import numpy as np

groups = ['G1','G2','G3','G4','G5']

men = np.array([22,30,35,35,26])
women = np.array([25,32,30,35,29])

men_sd = [4,3,4,1,5]
women_sd = [3,5,2,3,3]

x = np.arange(len(groups))

plt.bar(x, men, yerr=men_sd, label='Men')
plt.bar(x, women, bottom=men, yerr=women_sd, label='Women')

plt.xticks(x, groups)
plt.xlabel("Groups")
plt.ylabel("Scores")
plt.title("Stacked Bar Plot")

plt.legend()
plt.show()
