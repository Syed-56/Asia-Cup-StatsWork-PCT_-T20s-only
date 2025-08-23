import pandas as pd
from TeamsAnalysis import winCounts, avgTeamRR, avg_team_eco, boundaries, avgWickets, colors_map
from charts import makeBarChart

boundaries['Boundaries'] = boundaries['Fours'] + boundaries['Sixes']
boundaries = boundaries['Boundaries']
print(type(boundaries))

team_stats = pd.DataFrame({
    'Run Rate': avgTeamRR,
    'Boundaries': boundaries,
    'Wickets': avgWickets,
    'Economy Rate': avg_team_eco,
    'Wins': winCounts
})

team_stats_scaled = team_stats.copy()
for column in team_stats.columns:
    team_stats_scaled[column] = (team_stats[column] - team_stats[column].min()) / (team_stats[column].max() - team_stats[column].min())

weights = {
    'Run Rate': 0.2,
    'Boundaries': 0.1,
    'Wickets': 0.2,
    'Economy Rate': 0.2,
    'Wins': 0.3
}

team_stats_scaled['Overall Strength'] = (
    team_stats_scaled['Run Rate'] * weights['Run Rate'] +
    team_stats_scaled['Boundaries'] * weights['Boundaries'] +
    team_stats_scaled['Wickets'] * weights['Wickets'] +
    team_stats_scaled['Economy Rate'] * weights['Economy Rate'] +
    team_stats_scaled['Wins'] * weights['Wins']
)

team_stats_scaled['Overall Strength'] = team_stats_scaled['Overall Strength'] * 100
team_stats_scaled = team_stats_scaled.sort_values(by='Overall Strength', ascending=False)
for strength in team_stats_scaled:
     team_stats_scaled[strength] = team_stats_scaled[strength].fillna(0)

team_stats_scaled[strength] = pd.to_numeric(team_stats_scaled[strength], errors='coerce')
team_stats_scaled[strength] = team_stats_scaled[strength].apply(lambda x: x + 5.5 if x < 50 else x)

print(team_stats_scaled[['Overall Strength']])
makeBarChart(
    data=team_stats_scaled['Overall Strength'],
    colors_map=colors_map,
    title="Team's Strength (Asia Cup T20s)",
    xlabel="Teams",
    ylabel="Strength%",
    save_path="Analysis/Team_strength_percentage.png",
    orientation = 'horizontal'
)