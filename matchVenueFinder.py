import csv

def genrateCountriesCsv():
    # Change path depending on where the README with the list of matches is located
    fh = open("data/t20s_male_csv2/README.txt","r")
    word = "male"
    s = " "
    listOfMatchIds = []
    L = fh.readlines()

    for i in L:
        sentense = []
        L2 = i.split()
        if word in L2:
            sentense = i
            listOfMatchIds.append(sentense[42:49])

    fh.close()

    #print(listOfMatchIds)

    listOfVenues = []

    for j in listOfMatchIds:
        nameOfFile = j.strip()
        nameOfFile = nameOfFile+"_info.csv"
        # Change path depending on where the dataset is located
        f = open("data/t20s_male_csv2/"+nameOfFile,"r")
        csv_f = csv.reader(f)
        csv_f = list(csv_f)
    
        for k in csv_f:
            if "venue" in k:
                cR = " "
                #print("MatchID " + j + ": " + cR.join(k[2:]))
                listOfVenues.append([j,cR.join(k[2:])])
                break

        f.close()

    #print(listOfVenues)

    csv_file =  open("countries.csv", 'w')
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer.writerow(["Match ID","Venue","Country"])
    for row in listOfVenues:
        csv_writer.writerow(row)

    csv_file.close()

# The parameter has to be a string since the matchID in the countries.csv are strings
def findCountryWithMatchId(matchId):
    country = " "
    fileReader = open("countries.csv","r")
    csvFile = csv.reader(fileReader)
    
    for m in csvFile:
        if matchId in m:
            country = country.join(m[2:])

    if(country==" "):
        print("MatchID does not exist")
    fileReader.close()
    return country

#print(findCountryWithMatchId("682897"))
#print(findCountryWithMatchId("682"))