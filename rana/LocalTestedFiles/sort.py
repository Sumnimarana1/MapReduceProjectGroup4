#thisis to create a new text file with sorted store and cost

inputFile2 = open("MapperOutput.txt", "r")
outputFile2 = open("Sortoutput.txt", "w")
lines = inputFile2.readlines()
lines.sort()
for line in lines:
   outputFile2.write(line)
inputFile2.close()
outputFile2.close()
