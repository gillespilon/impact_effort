#! /usr/bin/env python3
"""
Create an impact versus effort scatter plot.

It is a grid or matrix to help in deciding which things to work on. It focuses
on the impact of doing something v. the effort required.
"""

import matplotlib.pyplot as plt
import datasense as ds


def main():
    colour1 = '#0077bb'
    colour2 = '#33bbee'
    title, subtitle, x_axis_label, y_axis_label,\
        file_name, figsize = (
            'Impact versus effort',
            'Potential controls',
            'Impact',
            'Effort',
            'impact_effort.csv',
            (8, 6)
        )
    impact_effort = ds.read_file(file_name=file_name)
    plot_scatter_annotate(
        data=impact_effort,
        figsize=figsize,
        title=title,
        subtitle=subtitle,
        x_axis_label=x_axis_label,
        y_axis_label=y_axis_label,
        colour1=colour1,
        colour2=colour2
    )


def plot_scatter_annotate(
        data,
        figsize,
        title,
        subtitle,
        x_axis_label,
        y_axis_label,
        colour1,
        colour2,
):
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    ax.plot(data['effort'], data['impact'], marker='o',
            color=colour1, linestyle='None')
    ax.set_title(
        label=title + '\n' + subtitle,
        fontweight="bold"
    )
    ax.set_ylabel(
        ylabel=y_axis_label,
        fontweight="bold"
    )
    ax.set_xlabel(
        xlabel=x_axis_label,
        fontweight="bold"
    )
    for row, text in enumerate(data['process']):
        ax.annotate(text, (data['effort'][row] + 1,
                           data['impact'][row] + 1))
    ax.set_ylim(
        left=0,
        right=100
    )
    ax.set_xlim(
        left=0,
        right=100
    )
    ax.axhline(
        y=50,
        color=colour2
    )
    ax.axvline(
        x=50,
        color=colour2
    )
    ds.despine(ax)
    fig.savefig(
        fname='impact_effort.svg',
        format='svg'
    )
    fig.savefig(
        fname='impact_effort.pdf',
        format='pdf'
    )
    fig.savefig(
        fname='impact_effort.png',
        format='png'
    )


if __name__ == '__main__':
    main()
