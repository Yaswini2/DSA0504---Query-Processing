import pandas as pd

df = pd.DataFrame({
    'Name': ['Anastasia','Dima','Katherine','James','Emily']
})

substring = 'a'

print(df['Name'].str.find(substring))
