
#opens file in read format
readfile = open("DC.txt", "r")
#opens file in write format
writefile = open("MAPPED.txt","w")

#line counter
countLine = 1

for line in readfile:
    data = line.strip().split("\t")
    countLine += 1
    if len(data) == 49:
        ID,BATHRM,HF_BATHRM,HEAT,AC,NUM_UNITS,ROOMS,BEDRM,AYB,YR_RMDL,EYB,STORIES,SALEDATE,PRICE,QUALIFIED,SALE_NUM,GBA,BLDG_NUM,STYLE,STRUCT,GRADE,CNDTN,EXTWALL,ROOF,INTWALL,KITCHENS,FIREPLACES,USECODE,LANDAREA,GIS_LAST_MOD_DTTM,SOURCE,CMPLX_NUM,LIVING_GBA,FULLADDRESS,CITY,STATE,ZIPCODE,NATIONALGRID,LATITUDE,LONGITUDE,ASSESSMENT_NBHD,ASSESSMENT_SUBNBHD,CENSUS_TRACT,CENSUS_BLOCK,WARD,SQUARE,X,Y,QUADRANT = data
        writefile.write("{0}\t{1}\n".format(BATHRM,ROOMS))
print(countLine)
readfile.close()
writefile.close()
