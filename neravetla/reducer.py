import sys


oldKey = None
counter = 0
sumOfBathrooms = 0

print("\n{0}\t{1}\n".format("number_of_rooms","average_num_of_bathrooms"))

for line in sys.stdin:
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
            print("{0}\t{1}\n".format(oldKey, round(sumOfBathrooms/float(counter), 2)))
            counter = 1
            sumOfBathrooms = int(bathrooms)
            oldKey = rooms
            continue
        counter = counter + 1
        sumOfBathrooms = sumOfBathrooms + int(bathrooms)
print("{0}\t{1}\n".format(oldKey, round(sumOfBathrooms/float(counter), 2)))
