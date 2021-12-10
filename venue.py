import csv

from matchVenueFinder import findCountryWithMatchId

def getVenuePrediction(teamName):
    f=open("data/t20s_male_csv2/README.txt","r")
    listofMatchIds=[]
    L=f.readlines()

    for line in L:
        if teamName in line:    
            Id=line[42:49]
            Id.strip()
            listofMatchIds.append(Id)
    f.close()

    print(len(listofMatchIds))
    # print(homeMatches)
    homeWins = 0
    awayWins = 0

    totalMatches = 0
    homeMatches = 0
    awayMatches = 0

    matchesPlayed = 0
    matchesWon = 0
    #print(homeWins)

    for matchId in listofMatchIds:
        fileName=matchId.strip()
        fileName=fileName+"_info.csv"
        f=open("data/t20s_male_csv2/"+fileName,"r")
        csv_f=csv.reader(f)
        csv_f=list(csv_f)

        for info in csv_f:
            if "team" in info:
                team = ""
                for words in info[2:]:
                    team+=words
                if teamName == team:
                    matchesPlayed = matchesPlayed+1

                    if(findCountryWithMatchId(matchId)==teamName):
                        homeMatches = homeMatches+1
                    else:
                        awayMatches = awayMatches + 1
                    
            # if "winner" in info:
            #     winner=""
            #     for words in info[2:]:
            #         winner+=words
            #     if teamName == winner:
            #         awayMatches = awayMatches + 1
            #         break

        for info in csv_f:
            if "winner" in info:
                winner=""
                for words in info[2:]:
                    winner+=words
                if teamName == winner:
                    matchesWon = matchesWon+1
                    # print(findCountryWithMatchId(matchId),matchId,teamName,(findCountryWithMatchId(matchId)==teamName))
                    if(findCountryWithMatchId(matchId)==teamName):
                        homeWins=homeWins+1
                    else:
                        awayWins =  awayWins+1
                
                else:
                    break 

         
        f.close()

    if(homeWins is not 0):
        print("\nPrediction Percentage Win at Home:", homeWins/homeMatches*100, "%")
    else:
        print("\nZero Matches Played At home")
    if(awayWins is not 0):
        print("Prediction Percentage Win while Away:", awayWins/awayMatches*100, "%")
    else:
        print("Zero Matches Played Away")

    print("\nTotal T20 Matches played Home:", homeMatches)
    print("Total T20 Matches played Away:", awayMatches)
    print("Total Matches Played in T20 format:", matchesPlayed)

    print("\nTotal Home Wins:", homeWins)    

    print("Total Away Wins:", awayWins)
    
    print("Total Matches Won:", matchesWon)
    totalMatches = homeWins+awayWins

    # print("\nPrediction Percentage Win at Home:", homeWins/homeMatches*100, "%")             
    # print("Prediction Percentage Win at Away:", awayWins/awayMatches*100, "%")

getVenuePrediction("India")