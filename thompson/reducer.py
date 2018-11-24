#Reducer for Realestate Data

import sys

totalcost = 0
totasqr = 0

for line in sys.stdin:
    data = line.strip().split("	")
    if len(data) = 2:
        cost, sqr = data

        if cost != "":
            totalcost = totalcost + cost
            totasqr = totasqr + sqr

print totalcost, "	", totasqr
