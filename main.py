import pandas as pd
import os
import glob
import re

path = os.getcwd()
csv = glob.glob(os.path.join(path, "D:\\t20s_male_csv2\\*.csv"))
print(csv)

match_info = []
for f in csv:
    a = f.replace("D:\\t20s_male_csv2\\", "")
    match_info.append(a)
print(match_info)

match_dtl = match_info
regex = re.compile(r'(.*.)_info.csv$')
match_dtl = [i for i in match_dtl if not regex.match(i)]
print(match_dtl)


df = pd.DataFrame()
for i in match_dtl:
    df1 = pd.read_csv("t20s_male_csv2\\" + i)
    d = {}
    d.update({"match_id": df1['match_id'][0], "team1": df1['batting_team'][0], "team2": df1['bowling_team'][0]})
    df2 = pd.DataFrame.from_dict(d, orient='index')
    df2 = df2.T
    df = df.append(df2)

df.to_csv('file1.csv')
df_final = pd.read_csv('file1.csv')

ls = []


def find_id(t1, t2):
    for i in range(len(df_final['match_id'])):

        if df_final['team1'][i] == t1:
            if df_final['team2'][i] == t2:
                ls.append(df_final['match_id'][i])
        if df_final['team2'][i] == t1:
            if df_final['team1'][i] == t2:
                ls.append(df_final['match_id'][i])


find_id('Sri Lanka', 'Australia')
print(ls)
