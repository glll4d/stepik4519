import pandas as pd

df = pd.read_excel("trekking1.xlsx")

print(df.sort_values(by=['ККал на 100', 'Unnamed: 0'], ascending=[False, True])['Unnamed: 0'].to_csv(sep='\t', index=False))
