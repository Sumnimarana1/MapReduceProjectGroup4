#this is to open the text files to read
inputFile3 = open("Sortoutput.txt", "r")
#this is to open the file to write the output to
outputFile3 = open("ReducerOutput(avgbyMonth).txt", "w")

# defining a variable
actualstore = 1
actualstoresum = 0
newcount =0

#start the for loop and goes through each line in the file
for eachline in inputFile3:
    # splits the date with tab-delimiter
    data2 = eachline.strip().split("\t")
    #checks for the bad input
    if len(data2) == 2:
        store3, cost3 = data2 
        cost3 = float(cost3.strip())
        if(int(actualstore) == int(store3.strip())): #check if the key is the same
            actualstoresum  += cost3 #calculatinf the total SALEPRICE
            newcount +=1
            continue

        #prints the output and send the output to the output file
        print(("{0}\t{1}\n".format(int(actualstore),actualstoresum/newcount)))
        outputFile3.write("{0}\t{1}\n".format(int(actualstore),actualstoresum/newcount))

        actualstore = store3
        actualstoresum = cost3
        newcount =0

#prints the output and send the output to the output file     
print(("{0}\t{1}\n".format(int(actualstore),actualstoresum/newcount)))
outputFile3.write("{0}\t{1}\n".format(int(actualstore),actualstoresum/newcount))
#closing the file
inputFile3.close()
outputFile3.close()
