# author - Krishna Veni Karri
# reducer code to find sentiment count of tweets

import csv
# open mapper output for reducer input
mapper_output = open("tweety.txt", "r")

positive_counter = 0
negative_counter = 0
neutral_counter = 0

# for each line in teh file check the first value which is sentiment and increment respective counter
for line in mapper_output:
    data = line.strip().split(',')
    if len(data) != 2:
        continue
    sentiment, text = data
    if sentiment == "negative":
        negative_counter = negative_counter + 1
    if sentiment == "positive":
        positive_counter = positive_counter + 1
    if sentiment == "neutral":
        neutral_counter = neutral_counter + 1

# open file senti.csv

csvFile = open("senti.csv", "w")
csvWriter = csv.writer(csvFile)

# write the the values in csv file

csvWriter.writerow(["Number of positive tweets ", positive_counter])
csvWriter.writerow(["Number of negative tweets ", negative_counter])
csvWriter.writerow(["Number of neutral tweets ", neutral_counter])

print("REDUCER JOB - SUCCESS!!\nPLEASE SEE THE RESULTS IN Senti.csv FILE")
csvFile.close()
