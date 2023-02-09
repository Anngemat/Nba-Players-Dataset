# -*- coding: utf-8 -*-
"""
Created on Mon May 30 01:37:00 2022

@author: USER
"""

#Get Excel file with pandas 
import pandas as pd
from matplotlib import pyplot as plt


#Get the data from the excel file
df = pd.read_excel(r'C:\Users\USER\Desktop\currentnbaplayerslist.xlsx')



uniqeTeams = df['Team'].unique()

#How much player in the teams
teamplayerList = []
for team in uniqeTeams:
    teamplayerList.append(df[df['Team'] == team].shape[0])

print(teamplayerList)

# make piechart for the teams
fig = plt.figure(figsize =(10, 7))
plt.pie(teamplayerList, labels = uniqeTeams)
# show plot
plt.show()
#Get Excel file with pandas 
import pandas as pd
from matplotlib import pyplot as plt


#Get the data from the excel file
df = pd.read_excel(r'C:\Users\USER\Desktop\currentnbaplayerslist.xlsx')



uniqeTeams = df['College'].unique()

#How much player in the teams
teamplayerList = []
for team in uniqeTeams:
    teamplayerList.append(df[df['College'] == team].shape[0])

print(teamplayerList)

# make piechart for the teams
fig = plt.figure(figsize =(10, 7))
plt.pie(teamplayerList, labels = uniqeTeams)
plt.legend()

# show plot
plt.show()
# add legend