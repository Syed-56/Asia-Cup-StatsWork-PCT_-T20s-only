# pie_chart.py
import numpy as np
import matplotlib.pyplot as plt
from adjustText import adjust_text
import pandas as pd

def makePieChart(data, labels=None, colors_map=None, colors=None, title="Pie Chart", save_path=None, 
                 number_type="count", figsize=(7,7), text_color="white"):
    """
    General Pie Chart maker with arrows pointing to labels.
    
    Parameters:
    -----------
    data : list/Series/array
        Values for each category.
    labels : list/Series (optional)
        Category names (default = indices if Series).
    colors_map : dict (optional)
        Mapping of category -> color.
    title : str
        Title of the chart.
    save_path : str (optional)
        File path to save chart (e.g., "output.png").
    number_type : str ("count" | "percent" | "both")
        What to display inside wedges.
    figsize : tuple
        Figure size.
    text_color : str
        Color of text inside wedges.
    """
    # If pandas Series passed, extract
    if hasattr(data, "values"):
        values = data.values
        if labels is None:
            labels = data.index
    else:
        values = np.array(data)
        if labels is None:
            labels = [f"Label {i}" for i in range(len(values))]

    # Assign colors
    if colors_map:
        colors = [colors_map.get(lbl, "#808080") for lbl in labels]
        if colors is None and colors_map:
            colors = [colors_map.get(lbl, "#808080") for lbl in labels]
    else:
        colors=None

    # Define number format
    def format_autopct(pct):
        total = sum(values)
        count = int(round(pct*total/100))
        if number_type == "count":
            return str(count)
        elif number_type == "percent":
            return f"{pct:.1f}%"
        elif number_type == "both":
            return f"{count}\n({pct:.1f}%)"
        return ""

    # Plot
    plt.figure(figsize=figsize)
    wedges, texts, autotexts = plt.pie(
        values,
        autopct=format_autopct,
        startangle=140,
        colors=colors,
        wedgeprops={'edgecolor':'white', 'linewidth':2},
        pctdistance=0.6,
        textprops={'fontsize':12, 'color':text_color}
    )

    # White text with black border
    for autotext in autotexts:
        autotext.set_color(text_color)

    # Arrows for labels
    label_radius = 1.2
    arrow_radius = 0.9
    for i, wedge in enumerate(wedges):
        angle = (wedge.theta2 + wedge.theta1)/2.0
        x_arrow = np.cos(np.deg2rad(angle)) * arrow_radius
        y_arrow = np.sin(np.deg2rad(angle)) * arrow_radius
        x_text = np.cos(np.deg2rad(angle)) * label_radius
        y_text = np.sin(np.deg2rad(angle)) * label_radius
        plt.annotate(
            labels[i],
            xy=(x_arrow, y_arrow),
            xytext=(x_text, y_text),
            ha="center", va="center",
            arrowprops=dict(arrowstyle="-", color="black", linewidth=1.2),
            fontsize=12
        )

    plt.title(title, fontsize=16, pad=25)

    # Save or show
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
    else:
        plt.show()

def makeBarChart(data, title, xlabel, ylabel, colors_map, save_path=None, line_style='-', figsize=(10, 6), orientation='vertical'):
    """
    Function to plot a bar chart with customizable parameters, supporting both vertical and horizontal bar charts.

    Parameters:
    - data: A pandas DataFrame or Series with x and y values.
    - title: Title of the chart.
    - xlabel: Label for the x-axis.
    - ylabel: Label for the y-axis.
    - colors_map: Dictionary mapping categories to colors.
    - save_path: Path to save the figure (optional).
    - line_style: Style of the line (default is solid line '-').
    - figsize: Tuple for the figure size (default is (10, 6)).
    - orientation: 'vertical' or 'horizontal' to control bar chart orientation.
    """
    plt.figure(figsize=figsize)

    if orientation == 'vertical':
        # Plot vertical bars
        bars = plt.bar(data.index, data, color=[colors_map.get(team, '#808080') for team in data.index])
        
        # Add values above each bar
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, height + 0.1, 
                     f'{height:.2f}', ha='center', va='bottom', fontsize=9)
        
        plt.xlabel(xlabel, fontsize=14)
        plt.ylabel(ylabel, fontsize=14)

    elif orientation == 'horizontal':
        # Plot horizontal bars
        bars = plt.barh(data.index, data, color=[colors_map.get(team, '#808080') for team in data.index])

        # Add values beside each bar
        for bar in bars:
            width = bar.get_width()
            plt.text(width + 0.1, bar.get_y() + bar.get_height() / 2, 
                     f'{width:.2f}', va='center', fontsize=9)
        
        plt.ylabel(xlabel, fontsize=14)
        plt.xlabel(ylabel, fontsize=14)

    plt.title(title, fontsize=16, pad=20)

    # Adjust layout to avoid clipping
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, bbox_inches="tight", dpi=300)
    else:
        plt.show()

def makeStackedBarChart(data, title, xlabel, ylabel, colors_map, save_path=None, figsize=(10, 6)):
    """
    Function to plot a stacked bar chart with customizable parameters.

    Parameters:
    - data: A pandas DataFrame with categories as columns and teams as index.
    - title: Title of the chart.
    - xlabel: Label for the x-axis.
    - ylabel: Label for the y-axis.
    - colors_map: Dictionary mapping categories to colors.
    - save_path: Path to save the figure (optional).
    - figsize: Tuple for the figure size (default is (10, 6)).
    """
    # Create a stacked bar chart
    ax = data.plot(kind='bar', stacked=True, figsize=figsize, color=[colors_map.get(col, '#808080') for col in data.columns])

    # Set chart title and labels
    plt.title(title, fontsize=16)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)

    # Add color legend
    plt.legend(title="Boundary Type", loc="upper left", bbox_to_anchor=(1.05, 1))

    # Add grid for better readability
    plt.grid(True, which='minor', linestyle='--', linewidth=0.5)

    # Adjust layout to prevent clipping
    plt.tight_layout()

    # Save or display the plot
    if save_path:
        plt.savefig(save_path, bbox_inches="tight", dpi=300)
    else:
        plt.show()

def makeLineChart(data, title, xlabel, ylabel, colors_map, save_path=None, line_style='-', figsize=(10, 6)):
    """
    Function to plot a line chart with customizable parameters.

    Parameters:
    - data: A pandas DataFrame or Series with x and y values.
    - title: Title of the chart.
    - xlabel: Label for the x-axis.
    - ylabel: Label for the y-axis.
    - colors_map: Dictionary mapping categories to colors.
    - save_path: Path to save the figure (optional).
    - line_style: Style of the line (default is solid line '-').
    - figsize: Tuple for the figure size (default is (10, 6)).
    """
    plt.figure(figsize=figsize)

    # Ensure data is a Series if it's a DataFrame
    if isinstance(data, pd.DataFrame):
        data = data.squeeze()  # Convert DataFrame to Series

    # Plot each team's line
    for team, color in colors_map.items():
        if team in data.index:  # Check if team exists in the index of the data
            plt.plot(data.index, data[team], label=team, color=color, linestyle=line_style, linewidth=2)

    # Set chart title and labels
    plt.title(title, fontsize=16, pad=20)
    plt.xlabel(xlabel, fontsize=14)
    plt.ylabel(ylabel, fontsize=14)

    # Adjust legend position (add more space on the right)
    plt.legend(
        title="Teams", 
        loc="upper left", 
        bbox_to_anchor=(0.8, 1),  # Add more space to the right of the plot
        borderaxespad=0.2,         # Adds some padding between the legend and the plot
        handlelength=1.5, 
        handleheight=1.5
    )

    plt.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Save or display the plot
    if save_path:
        plt.savefig(save_path, bbox_inches="tight", dpi=300)
    else:
        plt.show()

def makeScatterPlot(
    data, 
    x_col, 
    y_col, 
    label_col=None, 
    color_col=None, 
    colors_map=None,
    title="Scatterplot", 
    xlabel=None, 
    ylabel=None, 
    figsize=(10,6), 
    point_size=80,
    annotate_top_n=0,
    save_path=None
):
    """
    General Scatter Plot maker.

    Parameters:
    -----------
    data : DataFrame
        Pandas DataFrame with data.
    x_col : str
        Column for X-axis.
    y_col : str
        Column for Y-axis.
    label_col : str (optional)
        Column to use for annotating points (e.g., player names).
    color_col : str (optional)
        Column to determine point colors (e.g., country).
    colors_map : dict (optional)
        Mapping of category -> color.
    title : str
        Title of the chart.
    xlabel, ylabel : str
        Custom axis labels (default = column names).
    figsize : tuple
        Size of figure.
    point_size : int
        Size of scatter points.
    annotate_top_n : int
        If > 0, annotate top N by y_col.
    """

    plt.figure(figsize=figsize)

    # Assign colors
    if color_col and colors_map:
        colors = data[color_col].map(lambda c: colors_map.get(c, "#808080"))
    else:
        colors = "blue"


    # Annotations (rank by combined score = x_col * y_col)
    if label_col:

        ann = data.copy()
        ann["_x"] = pd.to_numeric(ann[x_col], errors="coerce")
        ann["_y"] = pd.to_numeric(ann[y_col], errors="coerce")
        ann["_score"] = ann["_x"] * ann["_y"]
        ann = ann.dropna(subset=["_x", "_y", "_score"])

        # choose which rows to annotate
        if annotate_top_n and annotate_top_n > 0:
            ann = ann.nlargest(annotate_top_n, "_score")
        plt.scatter(ann[x_col], ann[y_col], alpha=0.7)

        texts = []
        for _, row in ann.iterrows():
            texts.append(
                plt.text(row["_x"], row["_y"], str(row[label_col]), fontsize=9)
            )

        adjust_text(texts, arrowprops=dict(arrowstyle="->", color="gray", lw=0.5))

    # Labels & title
    plt.xlabel(xlabel if xlabel else x_col)
    plt.ylabel(ylabel if ylabel else y_col)
    plt.title(title)
    plt.grid(True)
    if save_path:
        plt.savefig(save_path, bbox_inches="tight", dpi=300)
    else:
        plt.show()