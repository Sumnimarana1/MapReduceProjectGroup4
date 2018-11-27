
#opens mapped.txt in read mode
inputFile2 = open("MAPPED.txt", "r")
#opens sorted.txt in write mode
outputFile2 = open("SORTED.txt", "w")

#reading the first line and writing it seperately because it is a header. It needs to be excluded.
header = inputFile2.readline()
outputFile2.write(header)

#read after the first line(we are exclusing the headline)
lines = inputFile2.readlines()[1:]
lines.sort()
for line in lines:
   outputFile2.write(line)
inputFile2.close()
outputFile2.close()
