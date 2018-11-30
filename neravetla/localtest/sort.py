'''Reads output from mapper.py, sorts it, and prints it to standard output
which can be read by reducer'''

#opens mapped.txt in read mode
inputFile = open("MAPPED.txt", "r")
#opens sorted.txt in write mode
outputFile = open("SORTED.txt", "w")


lines = inputFile.readlines()
lines.sort()
for line in lines:
   outputFile.write(line)
inputFile.close()
outputFile.close()
