import pandas as pd

df = pd.DataFrame({
    'school_code': ['S1','S1','S2','S2','S3','S3'],
    'age': [15,16,14,15,17,18]
})

result = df.groupby('school_code')['age'].agg(['mean','min','max'])

print(result)
