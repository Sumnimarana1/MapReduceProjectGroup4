
#opens mapped.txt in read mode
inputFile = open("MAPPED.txt", "r")
#opens sorted.txt in write mode
outputFile = open("SORTED.txt", "w")

#reading the first line and writing it seperately because it is a header. It needs to be excluded.
#header = inputFile2.readline()
#outputFile2.write(header)

#read after the first line(we are exclusing the headline)
#lines = inputFile2.readlines()[1:]
lines = inputFile.readlines()
lines.sort()
for line in lines:
   outputFile.write(line)
inputFile.close()
outputFile.close()
