readfile = open("SORTED.txt", "r")
writefile = open("REDUCED.txt", "w")

oldKey = None
counter = 0
sumOfRooms = 0

writefile.write("{0}\t{1}\n".format("number_of_rooms","average_num_of_bathrooms"))

for line in readfile:
	data = line.strip().split("\t")
	if len(data) == 2:
        	bathrooms, rooms = data
        	if (bathrooms != "BATHRM") and (rooms != "ROOMS"):
            		continue
        	if (bathrooms == 0) or (rooms == 0):
            		continue
		if oldKey and oldKey != bathrooms:
			print "{0}\t{1}".format(oldKey, sumOfRooms/counter)
			counter = 0
			sumOfRooms = 0
		oldKey = bathrooms
		counter += 1
		sumOfRooms += rooms

writefile.write("{0}\t{1}\n".format(numOfBath, sumOfRooms/counter)
writefile.close()
readfile.close()
