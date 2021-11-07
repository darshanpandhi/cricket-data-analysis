import pandas as pd
import os
import glob
import re

path = os.getcwd()
csv = glob.glob(os.path.join(path, "C:\\Users\\Ronak Vyas\\Desktop\\project\\cricket-data-analysis\\data\\t20s_male_csv2\\*.csv"))
print(csv)

match_info = []
for f in csv:
    a = f.replace("C:\\Users\\Ronak Vyas\\Desktop\\project\\cricket-data-analysis\\data\\t20s_male_csv2\\", "")
    match_info.append(a)
print(match_info)

match_detail = match_info
regex = re.compile(r'(.*.)_info.csv$')
match_detail = [i for i in match_detail if not regex.match(i)]
print(match_detail)

df = pd.DataFrame()
for i in match_detail:
    data_frame1 = pd.read_csv("t20s_male_csv2\\" + i)
    d = {}
    d.update({"match_id": data_frame1['match_id'][0], "team1": data_frame1['batting_team'][0], "team2": data_frame1['bowling_team'][0]})
    data_frame2 = pd.DataFrame.from_dict(d, orient='index')
    data_frame2 = data_frame2.T
    df = df.append(data_frame2)

df.to_csv('Extracted_Data_From.csv')
final_data = pd.read_csv('Extracted_Data_From.csv')

ls = []


def find_match_id(t1, t2):
    for i in range(len(final_data['match_id'])):

        if final_data['team1'][i] == t1:
            if final_data['team2'][i] == t2:
                ls.append(final_data['match_id'][i])
        if final_data['team2'][i] == t1:
            if final_data['team1'][i] == t2:
                ls.append(final_data['match_id'][i])


find_match_id('Sri Lanka', 'Australia')
print(ls)
print(len(ls))
