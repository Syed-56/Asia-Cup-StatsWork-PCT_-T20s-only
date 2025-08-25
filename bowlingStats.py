from data_scraping import bowlerDataT20
from charts import makePieChart, makeScatterPlot, makeBarChart
from TeamsAnalysis import colors_map 
import pandas as pd

# Top 5 wickets
mostWickets = bowlerDataT20[['Player Name', 'Wickets', 'Country']].sort_values(by='Wickets', ascending=False).head(5)
colors = [colors_map.get(country, "#808080") for country in mostWickets['Country']]
makePieChart(
    data=mostWickets['Wickets'],
    labels=mostWickets['Player Name'],   
    colors=colors,
    title="Most Wickets in T20 Asia Cup",
    save_path="Analysis/most_wickets.png",
    number_type="count"
)

# Best Avg
mostWickets = bowlerDataT20[['Player Name', 'Bowling Average', 'Country']].sort_values(by='Bowling Average', ascending=True).head(5)
colors = [colors_map.get(country, "#808080") for country in mostWickets['Country']]
makeBarChart(
    data = mostWickets.set_index('Player Name')['Bowling Average'],
    colors_map = colors_map,
    title = "Best Bowl Avg in T20 Asia Cup",
    xlabel = "Player",
    ylabel = "Bowling Average",  
    save_path="Analysis/best_Avg.png",
)

# Economy vs wickets
bowlerDataT20["Economy Rate"] = pd.to_numeric(bowlerDataT20["Economy Rate"], errors="coerce")
bowlerDataT20["Wickets"] = pd.to_numeric(bowlerDataT20["Wickets"], errors="coerce")
bowlerDataT20["Overs"] = pd.to_numeric(bowlerDataT20["Overs"], errors="coerce")

# Apply filter overs > 12
filtered_data = bowlerDataT20[bowlerDataT20["Overs"] > 12]  
makeScatterPlot(
    data=filtered_data,
    x_col="Economy Rate",
    y_col="Wickets",
    label_col="Player Name",
    color_col="Country",
    colors_map=colors_map,
    title="Economy vs Wickets (T20 Asia Cup)",
    annotate_top_n=10,
    save_path="Analysis/most_eco_wkt.png",
)
