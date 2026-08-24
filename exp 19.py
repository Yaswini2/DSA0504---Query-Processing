import pandas as pd

df = pd.read_csv("world_alcohol.csv")

print("Shape:", df.shape)

print("\nColumn Names:")
print(df.columns)
