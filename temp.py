# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import sklearn as sk
import numpy as np
import pandas as pd

df = pd.read_excel (r'C:\Users\USER\Desktop\currentnbaplayerslist.xlsx')
print (df)

df2 = df["Weight"].mean()
print(df2)
df7=df["Height"].mean(skipna=True)
print(df7)

df4=df["Team"].value_counts()
print(df4)

df5=df["Salary"].mean(skipna=True)
print(df5)

df6=df["Position"].value_counts()
print(df6)

df3=df["Age"].mean()
print(df3)

df1=df["College"].value_counts()
print(df1)

df['College'] = df['College'].fillna("Kentucky")
df['Salary'] = df['Salary'].fillna(8813695)
df["Team"] = df["Team"].fillna("Brooklyn Nets")










