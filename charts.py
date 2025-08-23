# pie_chart.py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patheffects as path_effects

def makePieChart(data, labels=None, colors_map=None, title="Pie Chart", save_path=None, 
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
    else:
        colors = None  # matplotlib default

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
        autotext.set_path_effects([path_effects.withStroke(linewidth=2, foreground="black")])

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

def makeBarChart(data, colors_map, title, x_label, y_label, save_path=None):
    """
    Generalized function to create a bar chart.

    Parameters:
    - data: The data to plot (e.g., a pandas Series or dictionary)
    - title: Title of the chart
    - x_label: Label for the x-axis
    - y_label: Label for the y-axis
    - save_path: Optional path to save the chart image

    Returns:
    - None
    """
    data = data.sort_values(ascending=True)
    plt.figure(figsize=(10, 6))
    colors = [colors_map.get(team, '#808080') for team in data.index]  # Default to gray if not found
    bars = plt.bar(data.index, data.values, color=colors, edgecolor='none', width=0.4)

    # Add percentage labels on the bars
    for bar in bars:
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1,
                 f"{bar.get_height():.1f}%", ha='center', fontsize=6, fontweight='light')

    # Add titles and labels
    plt.title(title, fontsize=14, fontweight="bold")
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.xticks(rotation=45)

    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    # Show the plot
    plt.show()