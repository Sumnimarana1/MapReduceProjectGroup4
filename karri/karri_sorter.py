tempfile = open("tweety.txt","r")  # open file, read-only
sorted_output = open("sorted_tweety.txt", "w") # open file, write
lines = tempfile.readlines()
lines.sort()

for line in lines:
	sorted_output.write(line)
tempfile.close()
sorted_tweety.close()
