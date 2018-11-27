import sys

#minimum number of rooms you need, you can change the number here
minRooms = 10
#minimum number of bathrooms you want, you can change the number here
minBathrooms = 7

#count number of houses that meet your requirement
countHouses = 0
#number of houses that don't meet your requirement
excludedHouses = 0
#total number of houses
totalHouses = 0

for line in sys.stdin:
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
print("\nTotal houses being searched: {0}\n".format(totalHouses))
print("Search Criteria => Minimum number of rooms: {0}, Minimum number of full bathrooms: {1}\n".format(minRooms, minBathrooms))
print("Number of houses that meet your requirement: {0}\n".format(countHouses))
print("Number of houses that DON'T meet your requirement: {0}\n".format(excludedHouses))
