import csv

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
    print(teamName)
    print("Total Matches played: ",len(listofMatchIds))                      
    print("Tosses Won: ",totalTossWon)
    print("Toss winning probability: ",totalTossWon/len(listofMatchIds)*100)
    print("Matches Won while winning the Toss: ",matchesWon)
    

    winPercentage=(matchesWon/totalTossWon)*100
    print("Chances that "+teamName+" will win the match if "+teamName+" wins the toss(%): ",winPercentage)
    return winPercentage

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

    


tossWinPercentage("India")
print("-------------------------------------------------")
tossWinPercentage("Pakistan")
print("-------------------------------------------------")
headToHead("India","Pakistan")
