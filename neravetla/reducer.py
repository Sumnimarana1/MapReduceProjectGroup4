'''
Reads output from sort.py and reduces it rooms and average number of bathrooms
'''


import sys

oldKey = None #variable to keep track of key changes
counter = 0 #variable to keep track of number of bathrooms
sumOfBathrooms = 0 #variable to sum the bathrooms for calcuating average

print("\n{0}\t{1}\n".format("number_of_rooms","average_num_of_bathrooms"))#prints to standard output

for line in sys.stdin:
    data = line.strip().split("\t")#turns input into a list
    if len(data) == 2:
        rooms, bathrooms = data
        if counter == 0:#makes sure after reading first record, counter is assigned 1, or else it won't divide to get the average
            oldKey = rooms
            counter = 1
            sumOfBathrooms = sumOfBathrooms + int(bathrooms)
            continue
        if oldKey != rooms: #if key changes, flush the data to disk, then change the variables
            print("{0}\t{1}\n".format(oldKey, round(sumOfBathrooms/float(counter), 2)))
            counter = 1
            sumOfBathrooms = int(bathrooms)
            oldKey = rooms
            continue
        counter = counter + 1
        sumOfBathrooms = sumOfBathrooms + int(bathrooms) #calculates average number of bathrooms per number of rooms of a house
print("{0}\t{1}\n".format(oldKey, round(sumOfBathrooms/float(counter), 2))) #prints to standard output
