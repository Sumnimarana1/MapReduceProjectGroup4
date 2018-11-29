#Maximum

#Open the File that was mapped too, to read from
r = open("mapped.txt", "r")
#Open a new file to write too
w = open("Maximum.txt","w")

#Set max to Zero.(This data has no negative values)
max = 0.0

#Read Through the read file line by line
for line in r:
    #Strip whitespace and split line by tabs
    data = line.strip().split("\t")
    #Check to see the number of colums is appropriate
    if len(data) == 2:
        #Assign variable names to seperated columns
        price, sqrf = data
        #Use conditional to ensure valitdity of Data
        if( price != "" and price != "PRICE" and float(price) != 0 and float(sqrf) > 1):
            price = float(price)
            sqrf = float(sqrf)           
            #Ensure price is Authentic field
            if price > 1:
                #Use conditional to determine min price per square foot
                if(price/sqrf)>max:
                    max = price/sqrf

#Write the Maximum, price per
#Square foot out to the new file
w.write("{0}\n".format(max))

#Close both Files
r.close()
w.close()