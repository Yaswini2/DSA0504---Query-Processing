import pandas as pd

df = pd.DataFrame({
    'school_code': ['S1','S1','S1','S2','S2','S3'],
    'class': [10,10,11,10,11,12],
    'student': ['A','B','C','D','E','F']
})

group = df.groupby(['school_code','class'])

for name, data in group:
    print("\nGroup:", name)
    print(data)
