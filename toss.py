import csv

def tossWinPercentage(teamName):
    f=open("data/t20s_male_csv2/README.txt","r")
    listofMatchIds=[]
    L=f.readlines()

    for line in L:
        words=line.split()
        teamNameWords=teamName.split()
        if len(teamNameWords)>1:
            for i in teamNameWords:
                if i in words:
                    t=1
                    if(t==1):
                        Id=line[42:49]
                        Id.strip()
                        listofMatchIds.append(Id)
        else:
            if teamName in words:
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
    print("Total Matches played: ",len(listofMatchIds))                      
    print("Tosses Won: ",totalTossWon)
    print("Toss winning probability: ",totalTossWon/len(listofMatchIds)*100)
    print("Matches Won while winning the Toss: ",matchesWon)
    

    winPercentage=(matchesWon/totalTossWon)*100
    print("Chances that "+teamName+" will win the match if "+teamName+" wins the toss(%): ",winPercentage)
    return winPercentage

tossWinPercentage("India")
