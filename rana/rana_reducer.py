import sys
#initializing all variables
    salesTotal = 0
    count = 0
    oldKey = None

    #for each line in file
    for line in sys.stdin:
        #split the line at tab delimeter
        data =line.strip().split("\t")
        #if data doesnot have length of two continues;
        if len(data) != 2:
            continue
        
        #stores the value
        thisKey, thisSale = data
            
        #check for the old key
        if oldKey and oldKey != thisKey:
            print "{0}\t{1}".format(oldKey, salesTotal/count) #prints the key and average pairs
            count = 0 #rechanges the count to zero
            salesTotal = 0 #rechanges the total to zero
        
        oldKey = thisKey #makes the old key as new key
        count += 1
        salesTotal += float(thisSale)
    print "{0}\t{1}".format(oldkey,salesTotal) #prints the end key value pair
