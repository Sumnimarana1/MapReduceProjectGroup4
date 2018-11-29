#opens MAPPED.txt in read mode
readfile2 = open("SORTED.txt", "r")
#opens REDUCED.txt in write mode
writefile2 = open("REDUCED.txt","w")
lines = readfile2.readlines()

oldKey = None
counter = 0
sumOfBathrooms = 0

writefile2.write("{0}\t{1}\n".format("number_of_rooms","average_num_of_bathrooms"))

for line in lines:
    data = line.strip().split("\t")
    if len(data) == 2:
        rooms, bathrooms = data
        #numOfBath = bathrooms
        #if (bathrooms != "BATHRM") and (rooms != "ROOMS"):
        #    continue
        if counter == 0:
            oldKey = rooms
            counter = 1
            sumOfBathrooms = sumOfBathrooms + int(bathrooms)
            continue
        if oldKey != rooms:
            writefile2.write("{0}\t{1}\n".format(oldKey, round(sumOfBathrooms/float(counter), 2)))
            counter = 1
            sumOfBathrooms = int(bathrooms)
            oldKey = rooms
            continue
        counter = counter + 1
        sumOfBathrooms = sumOfBathrooms + int(bathrooms)
writefile2.write("{0}\t{1}\n".format(oldKey, round(sumOfBathrooms/float(counter), 2)))
writefile2.close()
readfile2.close()
