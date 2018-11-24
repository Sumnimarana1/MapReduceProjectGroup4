#this is to actually sum the cost for each store
inputFile3 = open("Sortoutput.txt", "r")
outputFile3 = open("ReducerOutput(avgbyMonth).txt", "w")
line1 = inputFile3.readline()
data1 = line1.strip().split("\t")

actualstore = 1
actualstoresum = 0
newcount =0
for eachline in inputFile3:
    data2 = eachline.strip().split("\t")
    if len(data2) == 2:
        store3, cost3 = data2
        cost3 = float(cost3.strip())
        if(int(actualstore) == int(store3.strip())):
            actualstoresum  += cost3
            newcount +=1
            continue


        print(("{0}\t{1}\n".format(int(actualstore),actualstoresum/newcount)))
        outputFile3.write("{0}\t{1}\n".format(int(actualstore),actualstoresum/newcount))

        actualstore = store3
        actualstoresum = cost3
        newcount =0
print(("{0}\t{1}\n".format(int(actualstore),actualstoresum/newcount)))
outputFile3.write("{0}\t{1}\n".format(int(actualstore),actualstoresum/newcount))
inputFile3.close()
outputFile3.close()
