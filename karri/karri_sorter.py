tempfile = open("tweety.txt","r")  # open file, read-only
sorted_tweety = open("sorted_tweety.txt", "w") # open file, write
lines = tempfile.readlines()
lines.sort()

for line in lines:
	sorted_tweety.write(line)
tempfile.close()
sorted_tweety.close()