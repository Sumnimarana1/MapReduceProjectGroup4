#thisis to create a new text file with sorted month and Price
#this is to open the text files to read
inputFile2 = open("MapperOutput.txt", "r")
#this is to open the file to write the output to
outputFile2 = open("Sortoutput.txt", "w")
lines = inputFile2.readlines()
lines.sort()
#going through each line
for line in lines:
   outputFile2.write(line) #sorts the line
#closing the file
inputFile2.close()
outputFile2.close()
