# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 21:01:15 2023
"""
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('/content/healthcare_dataset.xlsx')
df.info()

medical_condition_totals = df.groupby('Medical Condition')['Billing Amount'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.bar(medical_condition_totals['Medical Condition'], medical_condition_totals['Billing Amount'])
plt.xlabel('Medical Condition')
plt.ylabel('Total Billing Amount')
plt.title('Total Billing Amount by Medical Condition')
plt.xticks(rotation=90)
# Displaying the plot
plt.show()