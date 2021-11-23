import csv

def venueWinPercentage():
     f=open("data/t20s_male_csv2/README.txt","r")
     listofMatchIds=[]
     L=f.readlines()
     
     for line in L:
            
        Id=line[42:49]
        Id.strip()
        listofMatchIds.append(Id)
        print(listofMatchIds)
     f.close()     

     matchesWonhome = 0
     winHomepercentage =0

# get the list of match ids of a team that u r interested in
#for every match Id u have to search in the countries.csv to check if the match was played in home or away
#also have to open .info file for every match id to check if they won the match or not
# need counter to count the number of wins

venueWinPercentage()