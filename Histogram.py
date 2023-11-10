# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 23:31:22 2023
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('/content/healthcare_dataset.xlsx')
df.info()
# Ensuring the 'Date of Admission' column is in datetime format
df['Date of Admission'] = pd.to_datetime(df['Date of Admission'])

plt.figure(figsize=(12, 6))
plt.hist(df['Billing Amount'], bins=30, edgecolor='k', alpha=0.7)
plt.xlabel('Billing Amount')
plt.ylabel('Frequency')
plt.title('Billing Amount Distribution')
plt.grid(True)

# Displaying the plot
plt.show()