from toss import main

d = {"Australia": 0, "South Africa": 0, "England": 0, "India": 0, "Pakistan": 0, "Sri Lanka": 0, "Afghanistan": 0,
     "Scotland": 0, "West Indies": 0
    , "New Zealand": 0, "Namibia": 0, "Bangladesh": 0, }

d1 = {"England": 0, "Australia": 0, "South Africa": 0, "Sri Lanka": 0, "West Indies": 0, "Bangladesh": 0}
d2 = {"Pakistan": 0, "New Zealand": 0, "India": 0, "Afghanistan": 0, "Namibia": 0, "Scotland": 0}


def checkWinner(Winner):
    updatePoints(Winner)


def simulation():
    # main("Australia", "South Africa", "Australia ", "United Arab Emirates")
    Winner = main("Australia", "South Africa", "Australia ", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("England", "West Indies", "England", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("Sri Lanka", "Bangladesh", "Sri Lanka", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("India", "Pakistan", "Pakistan", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("Afghanistan", "Scotland", "Afghanistan", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("South Africa", "West Indies", "South Africa", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("Pakistan", "New Zealand", "Pakistan", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("England", "Bangladesh", "Bangladesh", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("Scotland", "Namibia", "Namibia", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("Australia", "Sri Lanka", "Australia", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("West Indies", "Bangladesh", "Bangladesh", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("Pakistan", "Afghanistan", "Afghanistan", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("South Africa", "Sri Lanka", "South Africa", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("Australia", "England", "England", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("Afghanistan", "Namibia", "Afghanistan", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("India", "New Zealand", "New Zealand", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("England", "Sri Lanka", "Sri Lanka", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("South Africa", "Bangladesh", "South Africa", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("Pakistan", "Namibia", "Pakistan", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("New Zealand", "Scotland", "Scotland", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("India", "Afghanistan", "Afghanistan", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("Australia", "Bangladesh", "Australia", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("West Indies", "Sri Lanka", "West Indies", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("New Zealand", "Namibia", "Namibia", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("India", "Scotland", "India", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("Australia", "West Indies", "Australia", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("England", "South Africa", "England", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("New Zealand", "Afghanistan", "Afghanistan", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("Pakistan", "Scotland", "Pakistan", "United Arab Emirates")
    checkWinner(Winner)
    Winner = main("India", "Namibia", "India", "United Arab Emirates")
    checkWinner(Winner)



def updatePoints(matchWinner):
    # Add +2 points to the match winner key in the dictionary variable
    # check if dictionary contains match winner key
    # if it does upadate it to 2
    # if not create a new match winner key and initialize it to 2

    if matchWinner in d1:
        d1[matchWinner] = d1[matchWinner] + 2
        print("the match Winner is", matchWinner, "and their points is ", d1[matchWinner])
    elif matchWinner in d2:
        d2[matchWinner] = d2[matchWinner] + 2
        print("the match Winner is", matchWinner, "and their points is ", d2[matchWinner])
    else:
        print("No match Winners")
    print("\n")

    print("The matches of Group 1 is ", d1)
    print("The matches of Group 2 is ", d2)



simulation()
