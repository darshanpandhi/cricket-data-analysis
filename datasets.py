import pandas as pd
import os
import glob
import re


def read_file():
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(path, "..\\cricket-data-analysis\\data\\t20s_male_csv2"
                                             "\\*.csv"))
    match_detail = csv_files
    regex = re.compile(r'(.*.)_info.csv$')
    match_detail = [i for i in match_detail if not regex.match(i)]
    df = pd.DataFrame()
    for i in match_detail:
        dataframe = pd.read_csv(i)
        d = {}
        d.update({"match_id": dataframe['match_id'][0], "team1": dataframe['batting_team'][0],
                  "team2": dataframe['bowling_team'][0]})

        dataframe1 = pd.DataFrame.from_dict(d, orient='index')
        dataframe1 = dataframe1.T
        df = df.append(dataframe1)
    df.to_csv('extracted_data.csv')


def find_match_ids(t1, t2):
    ls = []
    final_data = pd.read_csv('extracted_data.csv')
    for i in range(len(final_data['match_id'])):
        if final_data['team1'][i] == t1:
            if final_data['team2'][i] == t2:
                ls.append(final_data['match_id'][i])
        if final_data['team2'][i] == t1:
            if final_data['team1'][i] == t2:
                ls.append(final_data['match_id'][i])


def generateCountriesCsv():
    # Change path depending on where the README with the list of matches is located
    fh = open("data/t20s_male_csv2/README.txt", "r")
    word = "male"
    s = " "
    listOfMatchIds = []
    L = fh.readlines()

    for i in L:
        sentence = []
        L2 = i.split()
        if word in L2:
            sentence = i
            listOfMatchIds.append(sentence[42:49])

    fh.close()

    listOfVenues = []

    for j in listOfMatchIds:
        nameOfFile = j.strip()
        nameOfFile = nameOfFile + "_info.csv"
        # Change path depending on where the dataset is located
        f = open("data/t20s_male_csv2/" + nameOfFile, "r")
        csv_f = csv.reader(f)
        csv_f = list(csv_f)

        for k in csv_f:
            if "venue" in k:
                cR = " "
                # print("MatchID " + j + ": " + cR.join(k[2:]))
                listOfVenues.append([j, cR.join(k[2:])])
                break

        f.close()

    csv_file = open("countries.csv", 'w')
    csv_writer = csv.writer(csv_file, delimiter=",")
    csv_writer.writerow(["Match ID", "Venue", "Country"])
    for row in listOfVenues:
        csv_writer.writerow(row)

    csv_file.close()
