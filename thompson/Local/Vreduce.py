#VREDUCE

#Open the File that was mapped too, to read from
r = open("mapped.txt", "r")
#Open a new file to write too
w = open("reduced.txt","w")

totprice = 0.0
totsqr = 0.0

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
                #Aggregate total price and total square feet
                totprice = totprice + price
                totsqr = totsqr + sqrf
#Calculate average price per square foot
#Divide the total price by the total square feet
avg = totprice/totsqr
#Write the average price per
#Square foot out to the new file
w.write("{0}\n".format(avg))

#Close both Files
r.close()
w.close()