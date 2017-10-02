#Outputs a csv file of PPG and adjusted PW by team
#I need to work on the formatting...

import csv
import FFB

with open('league_stats.csv', 'wb') as csv_file:
    writer = csv.writer(csv_file,delimiter = ":")
    for key, value in FFB.PPG_dictionary.items():
        writer.writerow([key,value])
    for key, value in FFB.adj_PW_dictionary.items():
        writer.writerow([key,value])
