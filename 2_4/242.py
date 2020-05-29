import os
import pandas as pd

files = os.listdir(os.path.abspath(os.curdir) + '\\rogaikopyta')

fio = []
cash = []

for i in files:
    df = pd.read_excel(os.path.abspath(os.curdir) + '\\rogaikopyta\\' + i)
    fio.append(df['Unnamed: 1'][0])
    cash.append(int(df['Unnamed: 3'][0]))

df_ans = pd.DataFrame({'Name': fio, 'Cash': cash}).sort_values(by='Name')
df_ans.to_csv('Answer.txt', sep=' ', index=False, encoding='utf-8', quoting=3, quotechar="",  escapechar=" ")
