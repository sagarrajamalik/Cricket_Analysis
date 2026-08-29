import os
import json
import csv
import datetime


venue_stats={}
matches_count={}
folder="inputData/CSA20Data"
target_file="CSA20_avg_scores.csv"
for i in os.listdir(folder):
    with open(os.path.join(folder, i), "r") as f:
        data=json.load(f)
    if datetime.datetime.strptime(data["info"]["dates"][0], "%Y-%m-%d") >= datetime.datetime(2020, 1, 1) and data["innings"][-1]["overs"]==20:
        pass
    else:
        continue
    venue=data["info"]["venue"]
    matches_count[venue]=matches_count.get(venue, 0)+1

    try:
        first_inn_score=data["innings"][-1]["target"]["runs"]-1
    except KeyError:
        continue

    try:
        venue_stats[venue][0]+=first_inn_score
        venue_stats[venue][1]+=1
    except KeyError:
        venue_stats[venue]=[first_inn_score, 1]
    

with open("avg_scores/"+target_file, "w", newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["Venue", "Average Score"])
        for entries in venue_stats.items():
            venue, stats=entries
            avg_score=int(stats[0]/stats[1])
            writer.writerow([venue, avg_score]) 
