import sys
#This program reads each line, and prints the Bathroom and Rooms values in pair to the standard input

countLine = 0

for line in sys.stdin:
    data = line.strip().split("\t")
    countLine += 1
    if len(data) == 49:
        ID,BATHRM,HF_BATHRM,HEAT,AC,NUM_UNITS,ROOMS,BEDRM,AYB,YR_RMDL,EYB,STORIES,SALEDATE,PRICE,QUALIFIED,SALE_NUM,GBA,BLDG_NUM,STYLE,STRUCT,GRADE,CNDTN,EXTWALL,ROOF,INTWALL,KITCHENS,FIREPLACES,USECODE,LANDAREA,GIS_LAST_MOD_DTTM,SOURCE,CMPLX_NUM,LIVING_GBA,FULLADDRESS,CITY,STATE,ZIPCODE,NATIONALGRID,LATITUDE,LONGITUDE,ASSESSMENT_NBHD,ASSESSMENT_SUBNBHD,CENSUS_TRACT,CENSUS_BLOCK,WARD,SQUARE,X,Y,QUADRANT = data
        if countLine >= 2:
            if (int(ROOMS) == 0) or (int(BATHRM) == 0):
                continue
            elif (int(ROOMS) < 10):
                ROOMS = "0" + ROOMS
                print("{0}\t{1}\n".format(ROOMS,BATHRM))
            else:
                print("{0}\t{1}\n".format(ROOMS,BATHRM))
