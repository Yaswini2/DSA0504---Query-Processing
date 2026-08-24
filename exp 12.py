import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(10,4),
    columns=['A','B','C','D']
)

def style_dataframe(value):
    return 'background-color: black; color: yellow'

print(df.style.map(style_dataframe))
