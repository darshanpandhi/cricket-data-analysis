import csv


def findCountryWithMatchId(matchId):
    country = ""
    fileReader = open("countries.csv", "r")
    csvFile = csv.reader(fileReader)
    for m in csvFile:
        if matchId in m or m[0] == str(matchId):
            country = country.join(m[2:])

    if(country==" "):
        print("MatchID does not exist = " + matchId)
    fileReader.close()
    return country
