from data_scraping import matches
from charts import makePieChart

winCounts = matches[matches['Result']=="Win"]
winCounts = winCounts['Team'].value_counts()
makePieChart(
    data=winCounts, 
    colors_map={'Pakistan':'#90ee90','Bangladesh':'#006400','Sri Lanka':'#ffa500','India':'#add8e6','Afghanistan':'#00008B'},
    title="T20 Asia Cup Matches Wins by Team",
    save_path="Analysis/asia_cup_wins.png",
    number_type="count"
)

