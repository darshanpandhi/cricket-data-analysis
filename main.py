from toss import generateList, teamRanking, headToHead, tossEvalTeams


def predictMatchResult():
    team1=input("Enter the name of team1: ")
    team2=input("Enter the name of team2: ")

    listofMatchIds=generateList(team1,team2)
    if(len(listofMatchIds)==0):
        result=teamRanking(team1,team2)
        if result[0]>result[1]:
            print("Winner: ",team1)
        elif result[1]>result[0]:
            print("Winner: ",team2)
        else:
            print("Match might tie, win percentage is 50-50")

    else:
        resultHtoH=headToHead(team1,team2,listofMatchIds)
        if resultHtoH[0]>resultHtoH[1]:
            print("Winner: ",team1)
            winner=team1
        elif resultHtoH[1]>resultHtoH[0]:
            print("Winner: ",team2)
            winner=team2
        else:
            print("Match might tie, win percentage is 50-50")
            winner=team1 +" or "+team2
        print("-------------------------------------------------")

        print("\nPrediction with toss result known: ")
        teamWonToss=input("Enter the team name that won the toss: ")
        resultToss=tossEvalTeams(team1,team2,listofMatchIds)
        if teamWonToss==team1 and resultToss[0]>resultToss[1]:
            print("Winner: ",team1)
        elif teamWonToss==team2 and resultToss[1]>resultToss[0]:
            print("Winner: ",team2)
        else:
            print("Winner: ",winner)

predictMatchResult()
