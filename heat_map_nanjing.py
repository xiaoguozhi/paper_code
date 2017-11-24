
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
%pylab inline

week = pd.read_excel('dat_month1_12_T.xlsx', index_col=0)

# Normalize data columns
#nba_norm = (nba - nba.mean()) / (nba.max() - nba.min())

# Sort data according to Points, lowest to highest
# This was just a design choice made by Yau
# inplace=False (default) ->thanks SO user d1337
#nba_sort = nba_norm.sort('PTS', ascending=True)

#nba_sort['PTS'].head(10)

# Plot it out
fig, ax = plt.subplots()
heatmap = ax.pcolor(week, cmap=plt.cm.Blues)

# Format
fig = plt.gcf()
fig.set_size_inches(8, 4)

# turn off the frame
ax.set_frame_on(False)

# put the major ticks at the middle of each cell
ax.set_yticks(np.arange(week.shape[0]) + 0.5, minor=False)
ax.set_xticks(np.arange(week.shape[1]) + 0.5, minor=False)

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()

# Set the labels

# label source:https://en.wikipedia.org/wiki/Basketball_statistics
labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# note I could have used nba_sort.columns but made "labels" instead
ax.set_xticklabels(labels, minor=False)
ax.set_yticklabels(week.index, minor=False)

# rotate the
#plt.xticks(rotation=90)

ax.grid(False)

# Turn off all the ticks
ax = plt.gca()

for t in ax.xaxis.get_major_ticks():
    t.tick1On = False
    t.tick2On = False
for t in ax.yaxis.get_major_ticks():
    t.tick1On = False
    t.tick2On = False

















