import csv

def genrateCountriesCsv():
    # Change path depending on where the README with the list of matches is located
    fh = open("data/t20s_male_csv2/README.txt","r")
    word = "male"
    s = " "
    listOfMatchIds = []
    L = fh.readlines()

    for i in L:
        sentense = []
        L2 = i.split()
        if word in L2:
            sentense = i
            listOfMatchIds.append(sentense[42:49])

    fh.close()

    #print(listOfMatchIds)

    listOfVenues = []

    for j in listOfMatchIds:
        nameOfFile = j.strip()
        nameOfFile = nameOfFile+"_info.csv"
        # Change path depending on where the dataset is located
        f = open("data/t20s_male_csv2/"+nameOfFile,"r")
        csv_f = csv.reader(f)
        csv_f = list(csv_f)
    
        for k in csv_f:
            if "venue" in k:
                cR = " "
                #print("MatchID " + j + ": " + cR.join(k[2:]))
                listOfVenues.append([j,cR.join(k[2:])])
                break

        f.close()

    #print(listOfVenues)

    csv_file =  open("countries.csv", 'w')
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer.writerow(["Match ID","Venue","Country"])
    for row in listOfVenues:
        csv_writer.writerow(row)

    csv_file.close()

# The parameter has to be a string since the matchID in the countries.csv are strings
def findCountryWithMatchId(matchId):
    country = " "
    fileReader = open("countries.csv","r")
    csvFile = csv.reader(fileReader)
    
    for m in csvFile:
        if matchId in m:
            country = country.join(m[2:])

    if(country==" "):
        print("MatchID does not exist")
    fileReader.close()
    return country

#print(findCountryWithMatchId("682897"))
#print(findCountryWithMatchId("682"))

TeamAndVenues = {
    "Australia": ["Sydney Cricket Ground", "Manuka Oval", "Perth Stadium", "Melbourne Cricket Ground", "Brisbane Cricket Ground, Woolloongabba", "Adelaide Oval", "Carrara Oval", "Bellerive Oval", "Simonds Stadium, South Geelong", "Tony Ireland Stadium", "Stadium Australia", "Western Australia Cricket Association Ground"],
    "Bangladesh": ["Sylhet International Cricket Stadium", "Shere Bangla National Stadium, Mirpur", "Khan Shaheb Osman Ali Stadium", "Sheikh Abu Naser Stadium", "Sylhet Stadium", "Zahur Ahmed Chowdhury Stadium", "Shere Bangla National Stadium"],
    "Bermuda": ["White Hill Field, Sandys Parish", "Bermuda National Stadium", "National Stadium"],
    "Bulgaria": ["National Sports Academy, Sofia"],
    "Canada": ["Maple Leaf North-West Ground"],
    "Cyprus": ["Happy Valley Ground"],
    "Czech Republic": ["Scott Page Field, Vinor"],
    "Denmark": ["Svanholm Park, Brondby"],
    "England": ["Old Trafford, Manchester", "Headingley, Leeds", "Trent Bridge, Nottingham", "The Rose Bowl, Southampton", "Sophia Gardens, Cardiff", "The Rose Bowl", "Old Trafford", "Sophia Gardens", "Lord's", "County Ground", "Edgbaston", "Riverside Ground", "Queens Sports Club", "Kennington Oval", "Trent Bridge"],
    "Finland": ["Kerava National Cricket Ground"],
    "Germany": ["Bayer Uerdingen Cricket Ground"],
    "Guernsey": ["College Field", "King George V Sports Ground"],
    "Hong Kong": ["Mission Road Ground, Mong Kok"],
    "India": ["Narendra Modi Stadium","Rajiv Gandhi International Stadium, Uppal", "M.Chinnaswamy Stadium", "Rajiv Gandhi International Cricket Stadium, Dehradun", "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium", "Rajiv Gandhi International Cricket Stadium", "Holkar Cricket Stadium", "Greenfield International Stadium", "Arun Jaitley Stadium", "Barsapara Cricket Stadium", "Greater Noida Sports Complex Ground", "Green Park", "Feroz Shah Kotla", "Punjab Cricket Association IS Bindra Stadium, Mohali", "Vidarbha Cricket Association Stadium, Jamtha", "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium", "JSCA International Stadium Complex", "Maharashtra Cricket Association Stadium", "Barabati Stadium", "Himachal Pradesh Cricket Association Stadium", "Saurashtra Cricket Association Stadium", "Sardar Patel Stadium, Motera", "M Chinnaswamy Stadium", "Wankhede Stadium", "Subrata Roy Sahara Stadium", "MA Chidambaram Stadium, Chepauk", "Eden Gardens", "Punjab Cricket Association Stadium, Mohali", "Vidarbha Cricket Association Stadium, Jamtha", "Brabourne Stadium"],
    "Ireland": ["Bready Cricket Club, Magheramason, Bready", "Castle Avenue, Dublin", "Civil Service Cricket Club, Stormont, Belfast", "The Village, Malahide, Dublin", "The Village, Malahide", "Bready", "Bready Cricket Club, Magheramason", "Clontarf Cricket Club Ground", "Civil Service Cricket Club, Stormont"],
    "Kenya": ["Mombasa Sports Club Ground", "Gymkhana Club Ground"],
    "Luxembourg": ["Pierre Werner Cricket Ground"],
    "Malaysia": ["Kinrara Academy Oval"],
    "Malta": ["Marsa Sports Club"],
    "Namibia": ["Wanderers Cricket Ground, Windhoek", "Wanderers", "United Cricket Club Ground", "Wanderers Cricket Ground"],
    "Nepal": ["Tribhuvan University International Cricket Ground, Kirtipur", "Tribhuvan University International Cricket Ground"],
    "Netherlands": ["Sportpark Westvliet", "VRA Ground", "Hazelaarweg", "Sportpark Maarschalkerweerd", "Sportpark Het Schootsveld"],
    "New Zealand": ["Eden Park", "McLean Park", "Seddon Park", "Sky Stadium", "Westpac Stadium", "University Oval", "Hagley Oval", "Bay Oval", "Saxton Oval", "AMI Stadium", "Eden Park, Auckland", "Jade Stadium"],
    "Oman": ["Al Amerat Cricket Ground Oman Cricket (Ministry Turf 1)"],
    "Pakistan": ["Gaddafi Stadium", "Rawalpindi Cricket Stadium", "National Stadium"],
    "Papua New Guinea": ["Amini Park"],
    "Portugal": ["Gucherre Cricket Ground"],
    "Romania": ["Moara Vlasiei Cricket Ground, Ilfov County", "Moara Vlasiei Cricket Ground"],
    "Rwanda": ["Gahanga International Cricket Stadium. Rwanda", "Integrated Polytechnic Regional Centre"],
    "Scotland": ["Grange Cricket Club Ground, Raeburn Place, Edinburgh", "Grange Cricket Club, Raeburn Place", "Grange Cricket Club Ground, Raeburn Place"],
    "Singapore": ["Indian Association Ground"],
    "South Africa": ["SuperSport Park, Centurion", "The Wanderers Stadium, Johannesburg", "Boland Park", "The Wanderers Stadium", "Senwes Park", "Mangaung Oval", "Buffalo Park", "Moses Mabhida Stadium", "De Beers Diamond Oval", "OUTsurance Oval", "New Wanderers Stadium", "SuperSport Park", "Eden Park", "St George's Park", "Newlands", "Kingsmead"],
    "Spain": ["Desert Springs Cricket Ground, Almeria", "Desert Springs Cricket Ground", "La Manga Club Bottom Ground"],
    "Sri Lanka": ["R Premadasa Stadium, Colombo", "Pallekele International Cricket Stadium", "R.Premadasa Stadium, Khettarama", "P Sara Oval", "Mahinda Rajapaksa International Cricket Stadium, Sooriyawewa", "Pallekele International Cricket Stadium", "R Premadasa Stadium"],
    "Thailand": ["Terdthai Cricket Ground"],
    "Uganda": ["Entebbe Cricket Oval", "Kyambogo Cricket Oval", "Lugogo Cricket Oval"],
    "United Arab Emirates": ["ICC Academy, Dubai", "Sheikh Zayed Stadium", "Dubai International Cricket Stadium", "ICC Academy", "Tolerance Oval", "ICC Academy Ground No 2", "Sharjah Cricket Stadium", "ICC Global Cricket Academy"],
    "United States of America": ["Central Broward Regional Park Stadium Turf Ground"],
    "West Indies": ["Providence Stadium, Guyana", "Kensington Oval, Bridgetown, Barbados", "Daren Sammy National Cricket Stadium, Gros Islet, St Lucia", "National Cricket Stadium, St George's, Grenada", "Coolidge Cricket Ground, Antigua", "Warner Park, St Kitts", "National Cricket Stadium, Grenada", "Darren Sammy National Cricket Stadium, St Lucia", "Windsor Park, Roseau", "Sabina Park, Kingston", "Arnos Vale Ground, Kingstown", "Sir Vivian Richards Stadium, North Sound", "Beausejour Stadium, Gros Islet", "Providence Stadium", "Queen's Park Oval, Port of Spain", "Warner Park, Basseterre", "Kensington Oval, Bridgetown"],
    "Zimbabwe": ["Harare Sports Club"]
}