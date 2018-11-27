#Reducer and computer for Realestate Data

import sys

totalcost = 0	#Counter for Total Cost
totasqr = 0	#Counter for total square feet

for line in sys.stdin:		#reads through input file line by line
    data = line.strip().split("\t")	#assigns line to list called data
    if len(data) = 2:			#checks to make sure correct data is being used
        cost, sqr = data

        if(cost != " " and cost != "COST":	#ensures the Header Line isn't computed,
						#and that sqrfeet of blank costs aren't added
            totalcost = totalcost + float(cost)
            totasqr = totasqr + float(sqr)

avg = totalcost/totasqr		#computes avg cost per square foot
print("{0}".format(avg))	#prints avg to system
