import matplotlib.pyplot as plt

languages = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

colors = ["red", "black", "green", "blue", "yellow", "cyan"]

plt.bar(languages, popularity, color=colors)

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Language")

plt.show()
