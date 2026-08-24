import pandas as pd
import matplotlib.pyplot as plt
data = {
'Date': ['2023-01-02', '2023-01-03', '2023-01-04',
'2023-01-05', '2023-01-06'],
'Volume': [18000000, 21000000, 19500000, 22000000, 20500000]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
plt.figure(figsize=(8,5))
plt.bar(df['Date'].dt.strftime('%Y-%m-%d'), df['Volume'], color='blue')
plt.title('Trading Volume of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Trading Volume')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
