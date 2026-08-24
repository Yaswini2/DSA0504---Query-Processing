import pandas as pd

df = pd.DataFrame({
    'school_code': ['S1','S1','S2','S2','S3'],
    'student': ['A','B','C','D','E'],
    'age': [15,16,14,15,17]
})

group = df.groupby('school_code')

print(group)
print(type(group))

for name, data in group:
    print("\nSchool:", name)
    print(data)
