from datasets import confirmMatchWinner, generateList

from matchVenueFinder import findCountryWithMatchId

from TeamAndVenues import TeamAndVenues

def getHomeAndAwayPercentage(teamName):

    homeMatchIds = []
    homeMatchesWon = 0

    awayMatchIds = []
    awayMatchesWon = 0
    
    listOfMatchIds = generateList(teamName,"")
    matchesPlayed = len(listOfMatchIds)

    for matchId in listOfMatchIds:
        if(findCountryWithMatchId(matchId)==teamName):
            homeMatchIds.append(matchId)
        else:
            awayMatchIds.append(matchId)

    noOfHomeMatches = len(homeMatchIds)
    noOfAwayMatches = len(awayMatchIds)

    homeMatchesWon = findNoOfWins(homeMatchIds,teamName)
    awayMatchesWon = findNoOfWins(awayMatchIds,teamName)

    if(noOfHomeMatches):
        homeWinPercentage = homeMatchesWon/noOfHomeMatches*100
    else:
        homeWinPercentage = 100    
    
    if(noOfAwayMatches):
        awayWinPercentage = awayMatchesWon/noOfAwayMatches*100
    else:
        awayWinPercentage = 100
    
    #print("Home: " + str(noOfHomeMatches))
    #print("Away: " + str(noOfAwayMatches))

    return homeWinPercentage, awayWinPercentage

def findNoOfWins(matchIds, team):
    matchesWon = 0

    for matchId in matchIds:
        if(confirmMatchWinner(matchId,team)):
            matchesWon = matchesWon+1
    
    return matchesWon

def HomeAndAwayForWorldCupTeams():
    for teams in TeamAndVenues.keys:
        currentTeam = teams
        print(currentTeam + ":" + str(getHomeAndAwayPercentage(currentTeam)))

