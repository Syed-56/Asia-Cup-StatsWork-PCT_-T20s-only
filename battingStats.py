from data_scraping import batsmanDataT20
from charts import makePieChart, makeScatterPlot
from TeamsAnalysis import colors_map 
import pandas as pd

mostRuns = batsmanDataT20[['Player Name', 'Runs', 'Country']].sort_values(by='Runs', ascending=False).head(5)
colors = [colors_map.get(country, "#808080") for country in mostRuns['Country']]
makePieChart(
    data=mostRuns['Runs'],
    labels=mostRuns['Player Name'],
    colors=colors,
    title="Most Runs in T20 Asia Cup",
    save_path="Analysis/most_runs.png",
    number_type="count"
)

most50s = batsmanDataT20[['Player Name', 'Fifties', 'Country']].sort_values(by='Fifties', ascending=False).head(5).reset_index(drop=True)
colors = [colors_map.get(country, "#808080") for country in most50s['Country']]
makePieChart(
    data=most50s['Fifties'],
    labels=most50s['Player Name'],
    colors=colors,
    title="Most 50s in T20 Asia Cup",
    save_path="Analysis/most_50s.png",
    number_type="count"
)

mostAvg = batsmanDataT20[['Player Name', 'Batting Average', 'Country']].sort_values(by='Batting Average', ascending=False).head(5).reset_index(drop=True)
mostSR = batsmanDataT20[['Player Name', 'Strike Rate', 'Country']].sort_values(by='Strike Rate', ascending=False).head(5).reset_index(drop=True)

# Ensure numeric dtype
batsmanDataT20["Batting Average"] = pd.to_numeric(
    batsmanDataT20["Batting Average"], errors="coerce"
)
batsmanDataT20["Strike Rate"] = pd.to_numeric(
    batsmanDataT20["Strike Rate"], errors="coerce"
)
batsmanDataT20["Runs"] = pd.to_numeric(
    batsmanDataT20["Runs"], errors="coerce"
)

# Apply filter Runs > 100
filtered_data = batsmanDataT20[batsmanDataT20["Runs"] > 100]
makeScatterPlot(
    data=filtered_data,
    x_col="Strike Rate",
    y_col="Batting Average",
    label_col="Player Name",
    color_col="Country",
    colors_map=colors_map,
    title="Strike Rate vs Batting Average (T20 Asia Cup)",
    annotate_top_n=10,   # annotate top 10 by Average
    save_path="Analysis/most_Avg_Sr.png",
)

