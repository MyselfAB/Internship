import pandas as pd

# Example dataset
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
data = pd.read_csv(url)
print(data.head())

print("                ",end=" \n \n \n " )

import numpy as np

# Filtering data
filtered_data = data[data['total_bill'] > 20]

# Grouping and Aggregating
grouped_data = data.groupby('day').agg({'total_bill': ['mean', 'sum'], 'tip': 'mean'})

print(grouped_data)



import matplotlib.pyplot as plt
import seaborn as sns

# Basic visualization
sns.scatterplot(x='total_bill', y='tip', data=data)
plt.title('Total Bill vs Tip')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.show()
