
#opens file in read format
readfile = open("DC.txt", "r")
#opens file in write format
writefile = open("MAPPED.txt","w")

#line counter
countLine = 0

for line in readfile:
    data = line.strip().split("\t") #this remove any white space, and turns the rest into a list
    countLine += 1
    if len(data) == 49:#checks if it is the right input
        ID,BATHRM,HF_BATHRM,HEAT,AC,NUM_UNITS,ROOMS,BEDRM,AYB,YR_RMDL,EYB,STORIES,SALEDATE,PRICE,QUALIFIED,SALE_NUM,GBA,BLDG_NUM,STYLE,STRUCT,GRADE,CNDTN,EXTWALL,ROOF,INTWALL,KITCHENS,FIREPLACES,USECODE,LANDAREA,GIS_LAST_MOD_DTTM,SOURCE,CMPLX_NUM,LIVING_GBA,FULLADDRESS,CITY,STATE,ZIPCODE,NATIONALGRID,LATITUDE,LONGITUDE,ASSESSMENT_NBHD,ASSESSMENT_SUBNBHD,CENSUS_TRACT,CENSUS_BLOCK,WARD,SQUARE,X,Y,QUADRANT = data
        if countLine >= 2:#ignores the header
            if (int(ROOMS) == 0) or (int(BATHRM) == 0):#removes invalid data
                continue
            elif (int(ROOMS) < 10):#adds 0 to key value that helps with proper sorting later
                ROOMS = "0" + ROOMS
                writefile.write("{0}\t{1}\n".format(ROOMS,BATHRM))#write to file
            else:
                writefile.write("{0}\t{1}\n".format(ROOMS,BATHRM))
print(countLine)
readfile.close()#closed file IO
writefile.close()
