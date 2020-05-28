import pandas as pd


df1 = pd.read_excel("trekking2.xlsx", sheet_name='Справочник')

df2 = pd.read_excel("trekking2.xlsx", sheet_name='Раскладка')

for i in range(df2.shape[1]):
    df2.