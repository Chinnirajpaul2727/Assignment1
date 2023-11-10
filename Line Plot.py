# -*- coding: utf-8 -*-
"""
Spyder Editor
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('/content/healthcare_dataset.xlsx')
df.info()
# Ensuring the 'Date of Admission' column is in datetime format
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])

# Sorting the data by the 'Date of Admission' for a meaningful line plot
df = df.sort_values(by='Date of Admission')

plt.figure(figsize=(15, 6))
plt.plot(df['Date of Admission'], df['Billing Amount'], label='Billing Amount')
plt.xlabel('Date of Admission')
plt.ylabel('Billing Amount')
plt.title('Billing Amount Over Time')
plt.legend()
plt.grid(True)

# Displaying the plot
plt.show()