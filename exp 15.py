import pandas as pd
import numpy as np

df = pd.DataFrame({
    'A': [1, np.nan, np.nan, 4],
    'B': [np.nan, np.nan, 7, 8],
    'C': [np.nan, 10, np.nan, 12]
})

result = df[df.isna().sum(axis=1) >= 2]

print(result)
