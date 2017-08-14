#! /usr/bin/env python3

# # Impact v. effort scatter plot

# ## In brevi
#
# It is a grid or matrix to help in deciding which things to work on. It focuses on the impact of doing something v. the effort required.

# ## Data
#
# Download the data file:
#
# - [Impact v. Effort](https://drive.google.com/open?id=0BzrdQfHR2I5DMFZVVG1TMnhWOFU)

# ## Methodology
#
# An impact v. effort grid is drawn using a scatter plot with pandas.DataFrame.plot.scatter. Points are annotated with matplotlib.axes.Axes.annotate. The 'grid' is created with matplotlib.axes.Axes.axvline and matplotlib.axes.Axes.avhline.

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt

impact_effort = pd.read_csv('impact_effort.csv')

title = 'Impact v. Effort'
subtitle = 'Symphony Processes'
yaxislabel = 'Impact'
xaxislabel = 'Effort'

ax = impact_effort.plot.scatter(x='effort', y='impact', marker='o', legend=False)
for spine in 'right', 'top':
    ax.spines[spine].set_color('none')

ax.set_title(title + '\n' + subtitle, fontweight="bold")
ax.set_ylabel(yaxislabel)
ax.set_xlabel(xaxislabel)

for i, txt in enumerate( impact_effort.process ):
    ax.annotate( txt, ( impact_effort.effort[i] + 1, impact_effort.impact[i] + 1 ) )

ax.set_ylim(0, 100)
ax.set_xlim(0, 100)
# Plot horizontal reference line
ax.axhline(y=50, color='r')
# Plot vertical reference line
ax.axvline(x=50, color='r')
ax.figure.savefig('impact_effort.svg', format='svg')
ax.figure.savefig('impact_effort.pdf', format='pdf')
ax.figure.savefig('impact_effort.png', format='png')


# ## References
#
# American Society for Quality. "Impact Effort Matrix." [(http://asq.org/healthcare-use/why-quality/impact-effort.html)](http://asq.org/healthcare-use/why-quality/impact-effort.html). Accessed 2017-08-08.
#
# Health Quality Ontario. "Impact/Effort Decision Making Grid." [(http://www.hqontario.ca/Portals/0/documents/qi/learningcommunity/pc-impact-effort-decision-making-criteria-chronic-disease-roadmap-resource-en.pdf)](http://www.hqontario.ca/Portals/0/documents/qi/learningcommunity/pc-impact-effort-decision-making-criteria-chronic-disease-roadmap-resource-en.pdf). Accessed 2017-08-08.
