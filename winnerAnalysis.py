from data_scraping import matches
from charts import makePieChart, makeBarChart

# winCounts = matches[matches['Result']=="Win"]
# winCounts = winCounts['Team'].value_counts()
# makePieChart(
#     data=winCounts, 
#     colors_map={'Pakistan':'#90ee90','Bangladesh':'#006400','Sri Lanka':'#ffa500','India':'#add8e6','Afghanistan':'#00008B'},
#     title="T20 Asia Cup Matches Wins by Team",
#     save_path="Analysis/asia_cup_wins.png",
#     number_type="count"
# )



totalMatches = matches['Team'].value_counts()
tossWins = matches[matches['Toss']=='Win']['Team'].value_counts()
tossWinPercent = (tossWins/totalMatches)*100
makeBarChart(
    data=tossWinPercent,
    colors_map={'Pakistan':'#90ee90','Bangladesh':'#006400','Sri Lanka':'#ffa500','India':'#add8e6','Hong Kong':"#FC1D1D",'UAE':"#8B0068",'Afghanistan':'#00008B'},
    title="Toss Win Percentage by Team (Asia Cup T20s)",
    x_label="Teams",
    y_label="Toss Win %",
    save_path="Analysis/toss_win_percentage.png"
)