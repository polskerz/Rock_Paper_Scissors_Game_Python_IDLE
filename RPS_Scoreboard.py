import csv

f1 = open("RPS_Scoreboard.csv", 'w', newline="")
a1 = csv.writer(f1)
list1 = ["Username", "Total Wins", "Total Losses", "Total Ties", "Total Attempts", "Win Ratio"]
a1.writerow(list1)
f1.close()
