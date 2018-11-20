salesTotal = 0
    count = 0
    oldKey = None

    for line in sys.stdin:
        data =line.strip().split("\t")

        if len(data) != 2:
            continue
        
        thisKey, thisSale = data

        if oldKey and oldKey != thisKey:
            print "{0}\t{1}".format(oldKey, salesTotal/count)
            count = 0
            salesTotal = 0

        oldKey = thisKey
        count += 1
        salesTotal += float(thisSale)

print "{0}\t{1}".format(oldkey,salesTotal)
