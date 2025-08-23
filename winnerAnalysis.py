from data_scraping import matches
import matplotlib.pyplot as plt
import numpy as np

def makePieChart(winCounts):
    team_colors = {
        'Pakistan': '#90ee90',      # light green
        'Bangladesh': '#006400',    # dark green
        'Sri Lanka': '#ffa500',     # orange
        'India': '#add8e6',         # light blue
        'Afghanistan': "#c75d42",   # dark blue
    }
    colors = [team_colors.get(team, '#808080') for team in winCounts.index]  # gray if not found

    plt.figure(figsize=(7,7))
    wedges, texts, autotexts = plt.pie(
        winCounts, 
        autopct=lambda pct: str(int(round(pct*sum(winCounts)/100))),
        startangle=140, 
        shadow=False, 
        colors=colors,
        wedgeprops={'edgecolor':'white', 'linewidth':2, 'linestyle':'-'},
        textprops={'fontsize':14},
        pctdistance=0.6,      # distance of number inside wedge
        )
    label_radius = 1.2
    arrow_radius = 0.9  # arrow stops before number

    for i, wedge in enumerate(wedges):
        angle = (wedge.theta2 + wedge.theta1)/2.0
        x_arrow = np.cos(np.deg2rad(angle)) * arrow_radius
        y_arrow = np.sin(np.deg2rad(angle)) * arrow_radius
        x_text = np.cos(np.deg2rad(angle)) * label_radius
        y_text = np.sin(np.deg2rad(angle)) * label_radius
        plt.annotate(
            winCounts.index[i],
            xy=(x_arrow, y_arrow),
            xytext=(x_text, y_text),
            ha='center', va='center',
            arrowprops=dict(arrowstyle='-', color='black', linewidth=1.2),
            fontsize=12
        )

    plt.title("T20 Asia Cup Matches Wins by Team", fontsize=18, pad=20)
    plt.savefig("Analysis/asia_cup_wins.png", dpi=300, bbox_inches="tight")


winCounts = matches[matches['Result']=="Win"]
winCounts = winCounts['Team'].value_counts()
makePieChart(winCounts)
