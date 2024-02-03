import pandas as pd
import csv



roys = pd.read_csv("roys.csv")
roys = roys[["Player", "Year", "Pts Won", "Pts Max", "Share"]]
# Getting rid of duplicate columns in ROY Data that we didn't need, what we did need
# was Yearm player, share, pts won and pts max
playersss = pd.read_csv("Playerstatistics.csv")
del playersss["Rk"]
del playersss["Unnamed: 0"]
# Delete uneeded columns in the playerstatistics file
playersss["Player"] = playersss["Player"].str.replace("*"," ", regex = False)
Final_data = playersss.merge(roys, how="outer", on= ["Player", "Year"])
Final_data[["Pts Won", "Pts Max", "Share"]] = Final_data[["Pts Won", "Pts Max", "Share"]].fillna(0)
# Combine player statistics and roy statistics into one file-- Final_data
Final_data.to_csv("stats.csv")



