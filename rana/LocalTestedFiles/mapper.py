#this is to open the text files to read
inputFile = open("DC.txt", "r")
#this is to open the file to write the output to
outputFile = open("MapperOutput.txt", "w")
count =1
#start the for loop and goes through each line in the file
for line in inputFile:
    #strips and splits the data at the tab-delimiter
    data = line.strip().split("\t")
    count += 1
    # check for the bad input
    if len(data) == 49:
        #values of all 49 columns
        ID,BATHRM,HF_BATHRM,HEAT,AC,NUM_UNITS,ROOMS,BEDRM,AYB,YR_RMDL,EYB,STORIES,SALEDATE,PRICE,QUALIFIED,SALE_NUM,GBA,BLDG_NUM,STYLE,STRUCT,GRADE,CNDTN,EXTWALL,ROOF,INTWALL,KITCHENS,FIREPLACES,USECODE,LANDAREA,GIS_LAST_MOD_DTTM,SOURCE,CMPLX_NUM,LIVING_GBA,FULLADDRESS,CITY,STATE,ZIPCODE,NATIONALGRID,LATITUDE,LONGITUDE,ASSESSMENT_NBHD,ASSESSMENT_SUBNBHD,CENSUS_TRACT,CENSUS_BLOCK,WARD,SQUARE,X,Y,QUADRANT= data
        newdata = SALEDATE.strip().split("/") #splits the Data at '/' 
        if len(newdata) == 3: # if the date is valid
            #seperates as Month, Day and year
            Month, Day, year = newdata
            if int(Month) < 10: # if the month is less that 10
                Month = "0" + Month #adding the prefix in the month as 01,02..11,12
            #ignores the bad input( if the price is empty)
            if(PRICE != "" and float(PRICE) !=0): 
                outputFile.write("{0}\t{1}".format(Month,PRICE)) # write to the file
                print Month,"\t", PRICE
                outputFile.write("\n")
print(count)
#closing the file
inputFile.close()
outputFile.close()
