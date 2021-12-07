import pandas as pd
import os
import glob
import re


def read_file():
    path = os.getcwd()
    csv_files = glob.glob(os.path.join(path, "..\\cricket-data-analysis-datasets\\data\\t20s_male_csv2"
                                             "\\*.csv"))
    match_detail = csv_files
    regex = re.compile(r'(.*.)_info.csv$')
    match_detail = [i for i in match_detail if not regex.match(i)]
    print(len(match_detail))
    print(match_detail)
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


def find_match_id(t1, t2):
    ls = []
    final_data = pd.read_csv('extracted_data.csv')
    for i in range(len(final_data['match_id'])):
        if final_data['team1'][i] == t1:
            if final_data['team2'][i] == t2:
                ls.append(final_data['match_id'][i])
        if final_data['team2'][i] == t1:
            if final_data['team1'][i] == t2:
                ls.append(final_data['match_id'][i])
    print(ls)
    print("the total list of match id's for the two teams is ", len(ls))


def main():
    read_file()
    find_match_id('Sri Lanka', 'Australia')


if __name__ == "__main__":
    main()
