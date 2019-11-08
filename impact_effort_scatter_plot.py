#! /usr/bin/env python3

# coding: utf-8

# # Impact v. effort scatter plot

# # Document information

# <table align="left">
#     <tr>
#         <th class="text-align:left">Title</th>
#         <td class="text-align:left">Impact v. effort scatter plot</td>
#     </tr>
#     <tr>
#         <th class="text-align:left">Last modified</th>
#         <td class="text-align:left">2018-06-27</td>
#     </tr>
#     <tr>
#         <th class="text-align:left">Author</th>
#         <td class="text-align:left">Gilles Pilon <gillespilon13@gmail.com></td>
#     </tr>
#     <tr>
#         <th class="text-align:left">Status</th>
#         <td class="text-align:left">Active</td>
#     </tr>
#     <tr>
#         <th class="text-align:left">Type</th>
#         <td class="text-align:left">Jupyter notebook</td>
#     </tr>
#     <tr>
#         <th class="text-align:left">Created</th>
#         <td class="text-align:left">2017-07-31</td>
#     </tr>
#     <tr>
#         <th class="text-align:left">File name</th>
#         <td class="text-align:left">impact_effort_scatter_plot.ipynb</td>
#     </tr>
#     <tr>
#         <th class="text-align:left">Other files required</th>
#         <td class="text-align:left">impact_effort.csv</td>
#     </tr>
# </table>

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

# Import the required librairies and magics.
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm


# Read the data.
impact_effort = pd.read_csv('impact_effort.csv')

# Set the labels.
title = 'Impact versus effort'
subtitle = 'Potential controls'
yaxislabel = 'Impact'
xaxislabel = 'Effort'

# Use a colour-blind friendly colormap, "Paired".
c = cm.Paired.colors
# c[0] c[1] ... c[11]
# See "paired" in "qualitative colormaps"
# https://matplotlib.org/tutorials/colors/colormaps.html

# Plot the scatter plot.
ax = impact_effort.plot.scatter(x='effort', y='impact', marker='o',\
                                color=c[0], legend=False)
for spine in 'right', 'top':
    ax.spines[spine].set_visible(False)
ax.set_title(title + '\n' + subtitle, fontweight="bold")
ax.set_ylabel(yaxislabel, fontweight="bold")
ax.set_xlabel(xaxislabel, fontweight="bold")
for i, txt in enumerate( impact_effort.process ):
    ax.annotate( txt, ( impact_effort.effort[i] + 1,\
                        impact_effort.impact[i] + 1 ) )
# Set the limits of the axes.

ax.set_ylim(0, 100)
ax.set_xlim(0, 100)
# Plot horizontal reference line
ax.axhline(y=50, color=c[1])
# Plot vertical reference line
ax.axvline(x=50, color=c[1])
# Save the graphs in svg, pdf, and png formats.
ax.figure.savefig('impact_effort.svg', format='svg')
ax.figure.savefig('impact_effort.pdf', format='pdf')
ax.figure.savefig('impact_effort.png', format='png')

# ## References
#
# American Society for Quality. "Impact Effort Matrix." [(http://asq.org/healthcare-use/why-quality/impact-effort.html)](http://asq.org/healthcare-use/why-quality/impact-effort.html). Accessed 2017-08-08.
#
# Health Quality Ontario. "Impact/Effort Decision Making Grid." [(http://www.hqontario.ca/Portals/0/documents/qi/learningcommunity/pc-impact-effort-decision-making-criteria-chronic-disease-roadmap-resource-en.pdf)](http://www.hqontario.ca/Portals/0/documents/qi/learningcommunity/pc-impact-effort-decision-making-criteria-chronic-disease-roadmap-resource-en.pdf). Accessed 2017-08-08.

