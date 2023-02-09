# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 07:31:49 2022

@author: USER
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

var = pd.read_excel("C:\Program Files\currentnbaplayerslist.xlsx")
print(var)

x = list(var['Weight'])
y = list(var['Height'])

plt.figure(figsize=(25,25))
plt.style.use('ggplot')
plt.scatter(x,y,marker="o",s=80,edgecolors="white",c="purple")
plt.title("NBA players' height/weight")
plt.xlabel("Weight (lbs)")
plt.ylabel("Height (cm)")
plt.xticks(np.arange(min(x), max(x), 10.0))
plt.yticks(np.arange(min(y)-2.8, max(y)+1, 2.0))

plt.gcf().autofmt_xdate()
plt.show()