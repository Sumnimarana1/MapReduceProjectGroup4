#opens MAPPED.txt in read mode
readfile = open("MAPPED.txt", "r")
#opens REDUCED.txt in write mode
writefile = open("REDUCED.txt","w")

#minimum number of rooms you need, you can change the number here
minRooms = 11
#minimum number of bathrooms you want, you can change the number here
minBathrooms = 8

#count number of houses that meet your requirement
countHouses = 0
#number of houses that don't meet your requirement
excludedHouses = 0
#total number of houses
totalHouses = 0

for line in readfile:
    data = line.strip().split("\t")
    if len(data) == 2:
        bathrooms, rooms = data
        if(bathrooms != "BATHRM") and (rooms != "ROOMS"):
            bathrooms = int(bathrooms)
            rooms = int(rooms)
            totalHouses += 1
            if (bathrooms >= minBathrooms) and (rooms >= minRooms):
                countHouses += 1

excludedHouses = totalHouses - countHouses
writefile.write("Total houses being searched: {0}\n".format(totalHouses))
writefile.write("Search Criteria => Minimum number of rooms: {0}, Minimum number of full bathrooms: {1}\n".format(minRooms, minBathrooms))
writefile.write("Number of houses that meet your requirement: {0}\n".format(countHouses))
writefile.write("Number of houses that DON'T meet your requirement: {0}\n".format(excludedHouses))
readfile.close()
writefile.close()
