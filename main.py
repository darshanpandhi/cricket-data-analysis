from headToHead import getHeadToHeadWinner
from teamRankings import getTeamRankingWinner
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

    print("-------------------------------------------------")

    print("\nPrediction with toss result known: ")
    teamWonToss = input("Enter the team name that won the toss: ")

    resultToss = tossEvalTeams(team1, team2, listofMatchIds)
    if teamWonToss == team1 and resultToss[0] > resultToss[1]:
        print("Winner: ", team1)
    elif teamWonToss == team2 and resultToss[1] > resultToss[0]:
        print("Winner: ", team2)
    else:
        print("Winner: ", resultHtoH)


predictMatchResult()
