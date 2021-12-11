import csv
from TeamAndVenues import TeamAndVenues


def generateList(team1, team2):
    f = open("data/t20s_male_csv2/README.txt", "r")
    listofMatchIds = []
    L = f.readlines()
    str1 = team1 + " vs " + team2
    str2 = team2 + " vs " + team1
    for line in L:
        if str1 in line or str2 in line:
            Id = line[42:49]
            Id.strip()
            listofMatchIds.append(Id)
    f.close()
    return listofMatchIds


def tossEvalTeams(team1, team2, listofMatchIds):
    team1WonTosses = 0
    team1WonMatches = 0
    team2WonTosses = 0
    team2WonMatches = 0

    for matchId in listofMatchIds:
        fileName = matchId.strip()
        fileName = fileName + "_info.csv"
        f = open("data/t20s_male_csv2/" + fileName, "r")
        csv_f = csv.reader(f)
        csv_f = list(csv_f)

        for info in csv_f:
            if "toss_winner" in info:
                team = ""
                for words in info[2:]:
                    team += words
                if team1 == team:
                    team1WonTosses += 1
                    break
            if "winner" in info:
                winner = ""
                for words in info[2:]:
                    winner += words
                if team1 == winner:
                    team1WonMatches += 1
                    break
                else:
                    break
        f.close()
        for info in csv_f:
            if "toss_winner" in info:
                team = ""
                for words in info[2:]:
                    team += words
                if team2 == team:
                    team2WonTosses += 1
                    break
            if "winner" in info:
                winner = ""
                for words in info[2:]:
                    winner += words
                if team2 == winner:
                    team2WonMatches += 1
                    break
                else:
                    break
        f.close()
    if team1WonTosses > 0:
        team1tossWin = team1WonMatches / team1WonTosses * 100
    else:
        team1tossWin = 0
    if team2WonTosses > 0:
        team2tossWin = team2WonMatches / team2WonTosses * 100
    else:
        team2tossWin = 0

    return [team1tossWin, team2tossWin]


def tossWinPercentage(teamName, listofMatchIds):
    totalTossWon = 0
    matchesWon = 0
    winPercentage = 0

    for matchId in listofMatchIds:
        fileName = matchId.strip()
        fileName = fileName + "_info.csv"
        f = open("data/t20s_male_csv2/" + fileName, "r")
        csv_f = csv.reader(f)
        csv_f = list(csv_f)

        for info in csv_f:
            if "toss_winner" in info:
                team = ""
                for words in info[2:]:
                    team += words
                if teamName == team:
                    totalTossWon = totalTossWon + 1
                    break
            if "winner" in info:
                winner = ""
                for words in info[2:]:
                    winner += words
                if teamName == winner:
                    matchesWon = matchesWon + 1
                    break
                else:
                    break
        f.close()

    if (totalTossWon > 0):
        winPercentage = (matchesWon / totalTossWon) * 100
    else:
        winPercentage = -1

    return winPercentage


def tossAverage():
    teams = TeamAndVenues.keys()
    totalTeams = len(teams)
    tossWinPercent = 0
    for team in teams:
        listofMatchIds = generateList(team, "")
        win = tossWinPercentage(team, listofMatchIds)
        if (win >= 0):
            tossWinPercent += win
        else:
            totalTeams -= 1
    print("\nIf a team wins the toss, their match winning chances are(average %): ", tossWinPercent / totalTeams)


def headToHead(team1, team2, listofMatchIds):
    team1MatchesWon = 0
    team2MatchesWon = 0
    for matchId in listofMatchIds:
        fileName = matchId.strip()
        fileName = fileName + "_info.csv"
        f = open("data/t20s_male_csv2/" + fileName, "r")
        csv_f = csv.reader(f)
        csv_f = list(csv_f)

        for info in csv_f:
            if "winner" in info:
                team = ""
                for words in info[2:]:
                    team += words
                if team1 == team:
                    team1MatchesWon += 1
                elif team2 == team:
                    team2MatchesWon += 1
        f.close()

        team1win = team1MatchesWon / (team1MatchesWon + team2MatchesWon) * 100
        team2win = team2MatchesWon / (team1MatchesWon + team2MatchesWon) * 100

        return [team1win, team2win]


def teamRanking(team1, team2):
    team1Rating = 0
    team2Rating = 0
    f = open("data/t20s_male_csv2/team_ranking.csv", "r")
    csv_f = csv.reader(f)
    csv_f = list(csv_f)

    for line in csv_f:
        if team1 in line:
            team1Rating = line[4:]
        if team2 in line:
            team2Rating = line[4:]
        if team1Rating != 0 and team2Rating != 0:
            break
    f.close()

    team1Rating = int(team1Rating[0])
    team2Rating = int(team2Rating[0])
    team1win = team1Rating / (team1Rating + team2Rating) * 100
    team2win = team2Rating / (team1Rating + team2Rating) * 100

    return [team1win, team2win]


def main(team1, team2, teamWonToss, venueCountry):
    listofMatchIds = generateList(team1, team2)
    if len(listofMatchIds) == 0:
        result = teamRanking(team1, team2)
        if result[0] > result[1]:
            print("Winner: ", team1)
        elif result[1] > result[0]:
            print("Winner: ", team2)
        else:
            print("Match might tie, win percentage is 50-50")

    else:
        resultHtoH = headToHead(team1, team2, listofMatchIds)
        if resultHtoH[0] > resultHtoH[1]:
            print("Winner: ", team1)
            winner = team1
        elif resultHtoH[1] > resultHtoH[0]:
            print("Winner: ", team2)
            winner = team2
        else:
            print("Match might tie, win percentage is 50-50")
            winner = team1 + " or " + team2
        print("-------------------------------------------------")

        print("\nPrediction with toss result known: ")
        # teamWonToss = input("Enter the team name that won the toss: ")
        resultToss = tossEvalTeams(team1, team2, listofMatchIds)
        if teamWonToss == team1 and resultToss[0] > resultToss[1]:
            print("Winner: ", team1)
        elif teamWonToss == team2 and resultToss[1] > resultToss[0]:
            print("Winner: ", team2)
        else:
            print("Winner: ", winner)


tossAverage()
