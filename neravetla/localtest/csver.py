import sys

inputfile = open("REDUCED.txt", "r")
writefile = open("CSVREDUCED.csv", "w")

for line in inputfile:
    data = line.strip().split("\t")
    room,bathroom = data
    if len(data) == 2:
        writefile.write("{0},{1}\n".format(room, bathroom))
inputfile.close()
writefile.close()
