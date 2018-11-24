#this is to make the new file with just datas as correct column
inputFile = open("DC.txt", "r")
outputFile = open("MapperOutput.txt", "w")
count =1
for line in inputFile:
    data = line.strip().split("\t")
    count += 1
    if len(data) == 49:
        ID,BATHRM,HF_BATHRM,HEAT,AC,NUM_UNITS,ROOMS,BEDRM,AYB,YR_RMDL,EYB,STORIES,SALEDATE,PRICE,QUALIFIED,SALE_NUM,GBA,BLDG_NUM,STYLE,STRUCT,GRADE,CNDTN,EXTWALL,ROOF,INTWALL,KITCHENS,FIREPLACES,USECODE,LANDAREA,GIS_LAST_MOD_DTTM,SOURCE,CMPLX_NUM,LIVING_GBA,FULLADDRESS,CITY,STATE,ZIPCODE,NATIONALGRID,LATITUDE,LONGITUDE,ASSESSMENT_NBHD,ASSESSMENT_SUBNBHD,CENSUS_TRACT,CENSUS_BLOCK,WARD,SQUARE,X,Y,QUADRANT= data
        newdata = SALEDATE.strip().split("/")
        if len(newdata) == 3:
            Month, Day, year = newdata
            if int(Month) < 10:
                Month = "0" + Month
            outputFile.write("{0}\t{1}".format(Month,PRICE))
            print Month,"\t", PRICE
            outputFile.write("\n")
print(count)
inputFile.close()
outputFile.close()
