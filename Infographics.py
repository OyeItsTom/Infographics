#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  5 19:26:31 2023

@author: tomthomas
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import seaborn as sns

#Reading the data
df_matches = pd.read_csv('Fifa_WC_2022_Match_data.csv',encoding='ISO-8859-1')
df_winners = pd.read_csv('FIFA Winners.csv')

#mathmatic realtion
df_matches.describe()

# Create a GridSpec object
fig = plt.figure(figsize = (24, 12), dpi = 300, facecolor = 'aliceblue')
grid = GridSpec(nrows = 2, ncols=4, figure=fig, hspace=0.5, wspace=0.5)
title_props = dict(boxstyle='round', facecolor='white', alpha=0.1)
fig.suptitle('FIFA Worldcup 2022 and All Winners (1930 - 2022) --- Tom Thomas  22008590', 
             fontsize = 26, fontweight = 'bold', color = 'White', 
             fontname = 'Times New Roman',
             bbox = title_props, y = .96, x = 0.5)

# creating the first plot
ax1 = plt.subplot(grid[0:2,0])
teams = pd.concat([df_matches['1'], df_matches['2']])
matches_played = pd.concat([df_matches['1'], df_matches['2']]).value_counts()
teams_sorted = matches_played.sort_values(ascending=False).index
sns.countplot(y = teams, order=teams_sorted, palette='gist_heat')
plt.title('Number of Matches Played by Each Team in 2022',fontsize=20, color = 'Snow')
plt.xlabel('Count',fontsize=12)
plt.ylabel('Team',fontsize=12)


# creating the second plot
ax2 = plt.subplot(grid[0,1:3])
plt.scatter(df_matches['date'], df_matches['attendance'], s=30)
# Set the axis labels and title
plt.xlabel('Date')
plt.ylabel('Attendance')
plt.title('Attendance at FIFA 2022 stadium',fontsize=20, color = 'Snow')
plt.xticks(rotation=90)



#Filtring data
arg_data = df_matches.loc[(df_matches['1'] == 'ARGENTINA') | (df_matches['2'] == 'ARGENTINA'), 
                  ['1', '2', '1_attempts', '1_conceded', '2_attempts', '2_conceded','date']]
# select the attempts and conceded columns based on which team Argentina is in
arg_data.loc[arg_data['1'] == 'ARGENTINA', 'attempts'] = arg_data['1_attempts']
arg_data.loc[arg_data['1'] == 'ARGENTINA', 'conceded'] = arg_data['1_conceded']
arg_data.loc[arg_data['2'] == 'ARGENTINA', 'attempts'] = arg_data['2_attempts']
arg_data.loc[arg_data['2'] == 'ARGENTINA', 'conceded'] = arg_data['2_conceded']
# drop the original attempts and conceded columns, and team1/team2 columns
arg_data = arg_data.reset_index()
arg_data.drop(['1', '2', '1_attempts', '1_conceded', '2_attempts', '2_conceded', 'index'], axis=1, inplace=True)

# creating the third plot
ax3 = plt.subplot(grid[1,1])
plt.plot(arg_data['date'], arg_data['attempts'], label='Attempts')
plt.plot(arg_data['date'], arg_data['conceded'], label='Conceded')
plt.xlabel('Date')
plt.ylabel('Number of goals')
plt.title('Argentina Football Team Goal in 2022', fontsize=20,color = 'Snow')
plt.xticks(rotation=90)
plt.legend()

# creating the fourth plot
ax4 = plt.subplot(grid[0, 3])
df_counts = df_winners.groupby(['Winners'])['Year'].count().reset_index()
plt.pie(df_counts['Year'], colors=['Skyblue', 'Yellow', 'Orangered', 'Wheat', 'Dimgray', 'Olive', 'Palegreen', 'Goldenrod', 'Slategrey'],
        autopct=lambda pct: "{:.1f}%\n({:d})".format(pct, int(round(pct/100*len(df_winners),0))), textprops={'fontsize': 12})
        #autopct='%1.1f%%')
plt.title('FIFA Winners (1930 - 2022)',fontsize=20,color = 'Snow')
plt.legend(labels=df_counts['Winners'], title='Winners', loc='center left', bbox_to_anchor=(0.9, 0.2))

# adding textbox
ax5=fig.add_subplot(grid[1,3])
ax5.axis('off')
txt='Brief Description:\nThis informational graph shows the summer\n timetable for the 2022 FIFA World Cup.\n The first graph shows how many games each side played in 2022.\n Argentina, France, Morocco, and Croatia\n are the teams that have played the most\n games, therefore it stands to reason that these are\n the teams that made it to the finals \nand semifinals.The scatter plot demonstrates that attendance at\n the stadium for the game corresponded to the date.\n Now we can see Argentinas \nefforts and goals in each game from the line plot.\n Argentina is one of the biggest drawers of fans to the stadium,\n according to a comparison of both of \nthese plots with dates.The pie chart shows \nall of Fifa champions from 1930 to 2022,\n with Brazil taking first place with five victories and Argentina placing \nsecond with three championships, including the 2022 World Cup.'
props = dict(boxstyle = 'round', facecolor = 'wheat')
ax5.text(0.5, 0.5, txt, fontsize = 16, bbox = props,ha = 'center', va = 'center_baseline')
plt.subplots_adjust(hspace=0.4)
fig.patch.set_facecolor('Indianred')
fig.tight_layout()
# Save the plot as a PNG file
plt.savefig('22008590.png',dpi=300)













