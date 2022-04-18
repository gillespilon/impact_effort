#! /usr/bin/env python3
"""
Create an impact versus effort scatter plot.

It is a grid or matrix to help in deciding which things to work on. It focuses
on the impact of doing something v. the effort required.
"""

from typing import Tuple

import matplotlib.pyplot as plt
import datasense as ds
import pandas as pd


def main():
    subtitle = "Potential controls"
    title = "Impact versus effort"
    x_axis_label = "Impact"
    y_axis_label = "Effort"
    colour1 = "#0077bb"
    colour2 = "#33bbee"
    figsize = (8, 6)
    ds.style_graph()
    impact_effort = pd.DataFrame(
        {
            "process": [
                "column1", "column2", "column3", "column4", "column5",
                "column6", "column7", "column8",
            ],
            "effort": [25, 35, 15, 30, 70, 90, 75, 85],
            "impact": [70, 60, 30, 20, 80, 65, 40, 30],
        }
    )
    plot_scatter_annotate(
        data=impact_effort, figsize=figsize, title=title, subtitle=subtitle,
        x_axis_label=x_axis_label, y_axis_label=y_axis_label, colour1=colour1,
        colour2=colour2,
    )


def plot_scatter_annotate(
    data: pd.DataFrame,
    figsize: Tuple[float, float],
    title: str,
    subtitle: str,
    x_axis_label: str,
    y_axis_label: str,
    colour1: str,
    colour2: str,
) -> None:
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111)
    ax.plot(data["effort"], data["impact"], marker="o", linestyle="None")
    ax.set_title(label=title + "\n" + subtitle)
    ax.set_ylabel(ylabel=y_axis_label)
    ax.set_xlabel(xlabel=x_axis_label)
    for row, text in enumerate(data["process"]):
        ax.annotate(text, (data["effort"][row] + 1, data["impact"][row] + 1))
    ax.set_ylim(bottom=0, top=100)
    ax.set_xlim(left=0, right=100)
    ax.axhline(y=50, color=colour2)
    ax.axvline(x=50, color=colour2)
    ds.despine(ax=ax)
    fig.savefig(fname="impact_effort.svg", format="svg")


if __name__ == "__main__":
    main()
