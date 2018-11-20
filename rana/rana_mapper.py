import sys
#reads for the each line in the file
for line in sys.stdin:
    #splits the data by tab-delimeter
    data = line.strip().split("\t")
    #each data is mapped
    ID,BATHRM,HF_BATHRM,HEAT,AC,NUM_UNITS,ROOMS,BEDRM,AYB,YR_RMDL,EYB,STORIES,SALEDATE,PRICE,QUALIFIED,SALE_NUM,GBA,BLDG_NUM,STYLE,STRUCT,GRADE,CNDTN,EXTWALL,ROOF,INTWALL,KITCHENS,FIREPLACES,USECODE,LANDAREA,GIS_LAST_MOD_DTTM,SOURCE,CMPLX_NUM,LIVING_GBA,FULLADDRESS,CITY,STATE,ZIPCODE,NATIONALGRID,LATITUDE,LONGITUDE,ASSESSMENT_NBHD,ASSESSMENT_SUBNBHD,CENSUS_TRACT,CENSUS_BLOCK,WARD,SQUARE,X,Y,QUADRANT
= data
    #here spliting the date in order to get month only
    newdata = SALEDATE.strip().split("/")
    #check if there is valid date given
    if len(newdata) == 3:
            Month, Day,year =newdata
            #If MONTH is less than 10 then adds 0 at the beginning
            if int(Month) < 10:
                Month = "0" + Month
            print Month,"\t", PRICE #prints the month and price
