from data_scraping import matches
from charts import makePieChart, makeBarChart, makeLineChart, makeStackedBarChart

colors_map={'Pakistan':'#90ee90','Bangladesh':'#006400','Sri Lanka':'#ffa500','India':'#add8e6','Hong Kong':"#FC1D1D",'UAE':"#8B0068",'Afghanistan':'#00008B'}

winCounts = matches[matches['Result']=="Win"]
winCounts = winCounts['Team'].value_counts()
makePieChart(
    data=winCounts, 
    colors_map=colors_map,
    title="T20 Asia Cup Matches Wins by Team",
    save_path="Analysis/asia_cup_wins.png",
    number_type="count"
)



totalMatches = matches['Team'].value_counts()
tossWins = matches[matches['Toss']=='Win']['Team'].value_counts()
tossWinPercent = (tossWins/totalMatches)*100
makeBarChart(
    data=tossWinPercent,
    colors_map=colors_map,
    title="Toss Win Percentage by Team (Asia Cup T20s)",
    xlabel="Teams",
    ylabel="Toss Win %",
    save_path="Analysis/toss_win_percentage.png",
    orientation = 'vertical'

)

avgTeamRR = matches.groupby('Team')['Run Rate'].mean().sort_values(ascending=False)
makeBarChart(
    data=avgTeamRR,
    colors_map=colors_map,
    title="Average Run Rate per Team in T20 Asia Cup",
    xlabel="Team",
    ylabel="Average Run Rate",
    save_path="Analysis/avg_run_rate_per_team.png",
    orientation = 'horizontal'
)

matches['Overs Faced by Opponent'] = matches['Run Scored'] / matches['Run Rate']
matches['Economy Rate'] = matches['Run Scored'] / matches['Overs Faced by Opponent']
avg_team_eco = matches.groupby('Opponent')['Economy Rate'].mean().sort_values(ascending=True)
makeBarChart(
    data=avg_team_eco,
    colors_map=colors_map,
    title="Average Economy Rate per Team in T20 Asia Cup",
    xlabel="Team",
    ylabel="Average Economy Rate",
    save_path="Analysis/avg_econ_rate.png",
    orientation = 'vertical'
)

boundaries = matches.groupby('Team')[['Fours', 'Sixes']].sum()
colors_map2 = {'Fours': '#90ee90', 'Sixes': '#ffa500', 'Extras': '#add8e6'}

# Call the function to create a stacked bar chart for boundaries and extras
makeStackedBarChart(
    data=boundaries,  # The summed data for each team
    title="Boundaries (Fours + Sixes) by Each Team",
    xlabel="Team",
    ylabel="Total Boundaries (Fours + Sixes)",
    colors_map=colors_map2,  # Color mapping for each category
    save_path="Analysis/boundaries.png"  # Optional path to save the image
)

avgWickets = matches.groupby('Team')['Wicket Taken'].sum().astype(int)
makeBarChart(
    data=avgWickets,
    colors_map=colors_map,
    title="Wickets per Team in T20 Asia Cup",
    xlabel="Team",
    ylabel="Wickets",   
    #save_path="Analysis/wickets_per_team.png",
    orientation = 'vertical'
)