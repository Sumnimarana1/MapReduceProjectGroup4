#this is finding the total number of followers for the twitter handler whose name start with "A" or "a" 
inputFile3 = open("Sortoutput.txt", "r")
outputFile3 = open("ReducerOutputCountFollowers.txt", "w")

totalcount = 0
key = ""
for eachline in inputFile3:
    data = eachline.strip().split("\t")
    if len(data) == 2:
        key, followercount = data
        followercount = followercount.strip()
        if(key[0] == "A" or key[0] == 'a'):
            totalcount += float(followercount)
            continue

print("{0}\t{1}\n".format("A", totalcount))
outputFile3.write("{0}\t{1}\n".format("A", totalcount))
inputFile3.close()
outputFile3.close()