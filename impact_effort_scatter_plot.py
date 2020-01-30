#! /usr/bin/env python3


'''
Impact v. effort scatter plot
It is a grid or matrix to help in deciding which things to work on. It focuses
on the impact of doing something v. the effort required.

Download the data file:

- https://drive.google.com/open?id=0BzrdQfHR2I5DMFZVVG1TMnhWOFU

An impact v. effort grid is drawn using a scatter plot with
pandas.DataFrame.plot.scatter. Points are annotated with
matplotlib.axes.Axes.annotate. The 'grid' is created with
matplotlib.axes.Axes.axvline and matplotlib.axes.Axes.avhline.
'''


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm


c = cm.Paired.colors


def main():
    title, subtitle, x_axis_label, y_axis_label, file_name = (
        'Impact versus effort',
        'Potential controls',
        'Impact',
        'Effort',
        'impact_effort.csv'
    )
    impact_effort = read_data_file(file_name)
    ax = impact_effort.plot.scatter(x='effort', y='impact', marker='o',
                                    color=c[0], legend=False)
    for spine in 'right', 'top':
        ax.spines[spine].set_visible(False)
    ax.set_title(title + '\n' + subtitle, fontweight="bold")
    ax.set_ylabel(y_axis_label, fontweight="bold")
    ax.set_xlabel(x_axis_label, fontweight="bold")
    for i, txt in enumerate(impact_effort.process):
        ax.annotate(txt, (impact_effort.effort[i] + 1,
                          impact_effort.impact[i] + 1))
    ax.set_ylim(0, 100)
    ax.set_xlim(0, 100)
    ax.axhline(y=50, color=c[1])
    ax.axvline(x=50, color=c[1])
    ax.figure.savefig('impact_effort.svg', format='svg')
    ax.figure.savefig('impact_effort.pdf', format='pdf')
    ax.figure.savefig('impact_effort.png', format='png')


def read_data_file(file_name):
    '''
    The data file has three columns:
    - process - text
    - effort - integer
    - impact - integer
    '''
    data_file = pd.read_csv(file_name)
    return data_file


if __name__ == '__main__':
    main()
