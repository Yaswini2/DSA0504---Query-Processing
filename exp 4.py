import pandas as pd
import matplotlib.pyplot as plt
data = {
'Date': ['2023-01-02', '2023-01-03', '2023-01-04',
'2023-01-05', '2023-01-06'],
'Close': [89.70, 91.45, 90.85, 92.60, 93.20]
}
df = pd.DataFrame(data)
df['Date'] = pd.to_datetime(df['Date'])
start_date = '2023-01-03'
end_date = '2023-01-06'
filtered = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]
plt.figure(figsize=(8,5))
plt.plot(filtered['Date'], filtered['Close'], marker='o', color='blue')
plt.title('Historical Stock Prices of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
