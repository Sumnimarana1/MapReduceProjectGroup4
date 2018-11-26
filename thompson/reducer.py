#Reducer for Realestate Data

import sys

totalcost = 0
totasqr = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) = 2:
        cost, sqr = data

        if(cost != " " and cost != "COST":
            totalcost = totalcost + float(cost)
            totasqr = totasqr + float(sqr)
avg = totalcost/totasqr
print("{0}".format(avg))
