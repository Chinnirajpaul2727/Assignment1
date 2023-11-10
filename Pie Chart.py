# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 23:34:57 2023
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('/content/healthcare_dataset.xlsx')
df.info()

blood_type_counts = df['Blood Type'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(blood_type_counts, labels=blood_type_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Blood Type Distribution')

# Displaying the plot
plt.show()