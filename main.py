from headToHead import getHeadToHeadWinner
from teamRankings import getTeamRankingWinner
from venue import getHomeAdvantage
from toss import tossEvalTeams
from datasets import generateList


def predictMatchResult():
    team1 = input("Enter the name of team1: ")
    team2 = input("Enter the name of team2: ")

    listofMatchIds = generateList(team1, team2)

    if len(listofMatchIds) == 0:
        getTeamRankingWinner(team1, team2, True)
    else:
        resultHtoH = getHeadToHeadWinner(team1, team2, True)
        winner=resultHtoH

    print("-------------------------------------------------")

    print("\nPrediction with toss result known: ")
    teamWonToss = input("Enter the team name that won the toss: ")
    resultToss = tossEvalTeams(team1, team2, listofMatchIds)
    if teamWonToss == team1 and resultToss[0] > resultToss[1]:
        winner=team1
    elif teamWonToss == team2 and resultToss[1] > resultToss[0]:
        winner=team2
    print("Winner: ", winner)

    
    print("-------------------------------------------------")
    print("\nPrediction based on venue:")
    venue = input("Enter the venue as a team name: ")
    resultVenue=getHomeAdvantage(team1,team2)
    if venue == team1 and resultVenue[0] > resultVenue[1]:
        winner=team1
    elif venue == team2 and resultVenue[1] > resultVenue[0]:
        winner=team2
    print("Winner: ", winner)

def predictMatchResult(team1,team2,teamWonToss,venue):
    
    listofMatchIds = generateList(team1, team2)

    if len(listofMatchIds) == 0:
        getTeamRankingWinner(team1, team2, True)
    else:
        resultHtoH = getHeadToHeadWinner(team1, team2, True)
        winner=resultHtoH
    
    print("-------------------------------------------------")

    print("\nPrediction with toss result known: ")
    resultToss = tossEvalTeams(team1, team2, listofMatchIds)
    if teamWonToss == team1 and resultToss[0] > resultToss[1]:
        winner=team1
    elif teamWonToss == team2 and resultToss[1] > resultToss[0]:
        winner=team2
    print("Winner: ", winner)
    
    print("-------------------------------------------------")
    print("\nPrediction based on venue:")
    resultVenue=getHomeAdvantage(team1,team2)
    if venue == team1 and resultVenue[0] > resultVenue[1]:
        winner=team1
    elif venue == team2 and resultVenue[1] > resultVenue[0]:
        winner=team2
    print("Winner: ", winner)

    return winner


#predictMatchResult()
(predictMatchResult("India","Pakistan","India","Pakistan"))

