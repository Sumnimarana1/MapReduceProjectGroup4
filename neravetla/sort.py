'''Reads output from mapper.py, sorts it, and prints it to standard output
which can be read by reducer'''
import sys

input = sys.stdin
lines = input.readlines()
lines.sort()
for line in lines:
   print(line)
