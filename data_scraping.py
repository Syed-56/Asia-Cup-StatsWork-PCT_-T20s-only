import kagglehub
import pandas as pd
path = kagglehub.dataset_download("hasibalmuzdadid/asia-cup-cricket-1984-to-2022")

matches = pd.read_csv(f"{path}/asiacup.csv")
matches = matches[matches["Format"]=="T20I"]
champions = pd.read_csv(f"{path}/champion.csv")
champions = champions[champions["Year"].isin([2016,2022])]
batsmanDataT20 = pd.read_csv(f"{path}/batsman data t20i.csv")
bowlerDataT20 = pd.read_csv(f"{path}/bowler data t20i.csv")
wkpDataT20 = pd.read_csv(f"{path}/wicketkeeper data t20i.csv")

for df in [matches, champions, batsmanDataT20, bowlerDataT20, wkpDataT20]:
    df.reset_index(drop=True, inplace=True)

if __name__ == "__main__":
    print(matches.head())