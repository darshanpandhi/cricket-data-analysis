import csv

def generateList(team1,team2):
    f=open("data/t20s_male_csv2/README.txt","r")
    listofMatchIds=[]
    L=f.readlines()
    str1=team1+" vs "+team2
    str2=team2+" vs "+team1
    for line in L:
        if str1 in line or str2 in line:
            Id=line[42:49]
            Id.strip()
            listofMatchIds.append(Id)
    f.close()
    return listofMatchIds

def tossEvalTeams(team1,team2):
    listofMatchIds=[]
    listofMatchIds=generateList(team1, team2)
    team1WonTosses=0
    team1WonMatches=0
    team2WonTosses=0
    team2WonMatches=0

    for matchId in listofMatchIds:
        fileName=matchId.strip()
        fileName=fileName+"_info.csv"
        f=open("data/t20s_male_csv2/"+fileName,"r")
        csv_f=csv.reader(f)
        csv_f=list(csv_f)
    
        for info in csv_f:
            if "toss_winner" in info:
                team=""
                for words in info[2:]:
                    team+=words
                if team1 == team:
                    team1WonTosses+=1
                    break
            if "winner" in info:
                winner=""
                for words in info[2:]:
                    winner+=words
                if team1 == winner:
                    team1WonMatches+=1
                    break
                else:
                    break       
        f.close()
        for info in csv_f:
            if "toss_winner" in info:
                team=""
                for words in info[2:]:
                    team+=words
                if team2 == team:
                    team2WonTosses+=1
                    break
            if "winner" in info:
                winner=""
                for words in info[2:]:
                    winner+=words
                if team2 == winner:
                    team2WonMatches+=1
                    break
                else:
                    break       
        f.close()
    print(team1+" will win the match if they win the toss: ",team1WonMatches/team1WonTosses*100)
    print(team2+" will win the match if they win the toss: ",team2WonMatches/team2WonTosses*100)
        


def tossWinPercentage(teamName):
    f=open("data/t20s_male_csv2/README.txt","r")
    listofMatchIds=[]
    L=f.readlines()

    for line in L:
        if teamName in line:    
            Id=line[42:49]
            Id.strip()
            listofMatchIds.append(Id)
    f.close()

    totalTossWon=0
    matchesWon=0
    winPercentage=0

    for matchId in listofMatchIds:
        fileName=matchId.strip()
        fileName=fileName+"_info.csv"
        f=open("data/t20s_male_csv2/"+fileName,"r")
        csv_f=csv.reader(f)
        csv_f=list(csv_f)
    
        for info in csv_f:
            if "toss_winner" in info:
                team=""
                for words in info[2:]:
                    team+=words
                if teamName == team:
                    totalTossWon=totalTossWon+1
                    break
            if "winner" in info:
                winner=""
                for words in info[2:]:
                    winner+=words
                if teamName == winner:
                    matchesWon=matchesWon+1
                    break
                else:
                    break       
        f.close()
    #print(teamName)
    #print("Total Matches played: ",len(listofMatchIds))                      
    #print("Tosses Won: ",totalTossWon)
    #print("Toss winning probability: ",totalTossWon/len(listofMatchIds)*100)
    #print("Matches Won while winning the Toss: ",matchesWon)
    
    if(totalTossWon>0):
        winPercentage=(matchesWon/totalTossWon)*100
    #print("Chances that "+teamName+" will win the match if "+teamName+" wins the toss(%): ",winPercentage)
    return winPercentage

def tossAverage():
    teams=['England', 'Pakistan', 'India', 'New Zealand', 'South Africa', 'Australia', 'Afghanistan', 'Bangladesh', 'Sri Lanka', 'West Indies', 'Zimbabwe', 'Ireland', 'Nepal', 'Scotland', 'Namibia', 'UAE', 'Oman', 'Netherlands', 'Papua New Guinea', 'Singapore', 'Qatar', 'Canada', 'Jersey', 'Hong Kong', 'Kenya', 'Kuwait', 'Italy', 'Uganda', 'United States', 'Saudi Arabia', 'Malaysia', 'Bermuda', 'Germany', 'Denmark', 'Botswana', 'Nigeria', 'Bahrain', 'Tanzania', 'Guernsey', 'Romania', 'Spain', 'Norway', 'France', 'Belgium', 'Austria', 'Finland', 'Philippines', 'Mexico', 'Cayman Islands', 'Belize', 'Vanuatu', 'Portugal', 'Ghana', 'Isle of Man', 'Luxembourg', 'Malawi', 'Peru', 'Fiji', 'Sweden', 'Samoa', 'Hungary', 'Japan', 'Costa Rica', 'Argentina', 'Thailand', 'Panama', 'Malta', 'Czech Republic', 'South Korea', 'Greece', 'Rwanda', 'Bulgaria', 'Mozambique', 'Bhutan', 'Saint Helena', 'Seychelles', 'Brazil', 'Maldives', 'Chile', 'Myanmar', 'Indonesia', 'Lesotho', 'Eswatini', 'Turkey', 'China', 'Serbia', 'Gibraltar']
    totalTeams=len(teams)
    tossWinPercent=0
    for team in teams:
        win=tossWinPercentage(team)
        #tossWinPercent+=win
        if(win>0):
            tossWinPercent+=win
        else:
            totalTeams-=1
    print("If a team wins the toss, their match winning chances are(%): ",tossWinPercent/totalTeams)


def headToHead(team1,team2):
    f=open("data/t20s_male_csv2/README.txt","r")
    listofMatchIds=[]
    L=f.readlines()
    str1=team1+" vs "+team2
    str2=team2+" vs "+team1
    for line in L:
        if str1 in line or str2 in line:
            Id=line[42:49]
            Id.strip()
            listofMatchIds.append(Id)
    f.close()
    
    team1MatchesWon=0
    team2MatchesWon=0
    for matchId in listofMatchIds:
        fileName=matchId.strip()
        fileName=fileName+"_info.csv"
        f=open("data/t20s_male_csv2/"+fileName,"r")
        csv_f=csv.reader(f)
        csv_f=list(csv_f)
    
        for info in csv_f:
            if "winner" in info:
                team=""
                for words in info[2:]:
                    team+=words
                if team1 == team:
                    team1MatchesWon+=1
                elif team2 == team:
                    team2MatchesWon+=1
        f.close()

    print(str1)
    print("Total matches played: ",len(listofMatchIds))
    print("Matches won by "+team1+": ",team1MatchesWon)
    print("Matches won by "+team2+": ",team2MatchesWon)
    if(len(listofMatchIds)!=0):
        print(team1+" will win: ",team1MatchesWon/(team1MatchesWon+team2MatchesWon)*100)
        print(team2+" will win: ",team2MatchesWon/(team1MatchesWon+team2MatchesWon)*100)

def teamRanking(team1, team2):
    team1Rating=0
    team2Rating=0
    f=open("data/t20s_male_csv2/team_ranking.csv","r")
    csv_f=csv.reader(f)
    csv_f=list(csv_f)

    for line in csv_f:
        if team1 in line:
            team1Rating=line[4:]
        if team2 in line:
            team2Rating=line[4:]
        if team1Rating!=0 and team2Rating!=0:
            break
    f.close()
    
    team1Rating=int(team1Rating[0])
    team2Rating=int(team2Rating[0])
    print(team1+"'s Rating: ",team1Rating)
    print(team2+"'s Rating: ",team2Rating)
    print(team1+" will win: ",team1Rating/(team1Rating+team2Rating)*100)
    print(team2+" will win: ",team2Rating/(team1Rating+team2Rating)*100)




    
#print(tossWinPercentage("India"))
#headToHead("India","Pakistan")
#print("-------------------------------------------------")
#teamRanking("Australia","New Zealand")
print("-------------------------------------------------")
tossEvalTeams("India", "Pakistan")
#tossAverage()
