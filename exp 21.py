import pandas as pd

data = {'Name': ['Alice', 'BOB', 'Charlie', 'DAVID']}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df['Name'] = df['Name'].str.swapcase()

print("\nAfter swapping cases:")
print(df)
