#VREDUCE

r = open("mapped.txt", "r")
w = open("reduced.txt","w")

totprice = 0.0
totsqr = 0.0

for line in r:
    data = line.strip().split("\t")
    if len(data) == 2:
        price, sqrf = data
        if( price != " " and price != "PRICE"):
            price = float(price)
            sqrf = float(sqrf)    
            #print(price)
            #print("\t")
            #print(sqrf)       
            if price > 1:
                totprice = totprice + price
                totsqr = totsqr + sqrf
avg = totprice/totsqr
w.write("{0}\n".format(avg))
r.close()
w.close()