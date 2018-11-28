#this is to make the new file with just datas as correct column
inputFile = open("metoo.txt", "r")
outputFile = open("MapperOutput.txt", "w")
count =1
for line in inputFile:
    data = line.strip().split("\t")
    count += 1
    if len(data) == 5:
        ID,insertdate,twitterhandle,followers,hashtags= data
        if( ID[0] == '2' or followers[0] != '1'):
                if( followers[0] != ' ' or followers[0] != ' ' or followers[0] != '' or followers != " "):
                        if(followers != " "):
                                if(followers[0] != '1'):
                                        outputFile.write("{0}\t{1}".format(twitterhandle,followers))
                                        #print twitterhandle,"\t", followers
                                        outputFile.write("\n")
print(count)
inputFile.close()
outputFile.close()