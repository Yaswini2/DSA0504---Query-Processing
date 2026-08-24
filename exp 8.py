import pandas as pd
data = {
    'Item': ['Laptop', 'Laptop', 'Mouse', 'Mouse', 'Keyboard', 'Keyboard'],
    'Region': ['East', 'West', 'East', 'West', 'East', 'West'],
    'Units_Sold': [15, 20, 35, 30, 25, 18]
}
sales_data = pd.DataFrame(data)
pivot = pd.pivot_table(
    sales_data,
    values='Units_Sold',
    index='Item',
    aggfunc='sum'
)
print("Item-wise Units Sold:")
print(pivot)
