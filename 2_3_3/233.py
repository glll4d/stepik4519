import pandas as pd
import math

df1 = pd.read_excel("trekking2.xlsx", sheet_name='Справочник')
df2 = pd.read_excel("trekking2.xlsx", sheet_name='Раскладка')

for i in range(df2.shape[0]):
    df3 = pd.merge(left=df1, right=df2, left_on='Unnamed: 0', right_on='Продукт')

Callories = 0
Proteins = 0
Fats = 0
Carbohydrates = 0

for i in range(df3.shape[0]):
    Callories += df3['ККал на 100'][i]/100*df3['Вес в граммах'][i]
    Proteins += df3['Б на 100'][i] / 100 * df3['Вес в граммах'][i]
    Fats += df3['Ж на 100'][i] / 100 * df3['Вес в граммах'][i]
    if not math.isnan(df3['У на 100'][i]):
        Carbohydrates += df3['У на 100'][i] / 100 * df3['Вес в граммах'][i]

print(str(math.floor(Callories))+' ККал')
print(str(math.floor(Proteins))+' Белков')
print(str(math.floor(Fats))+' Жиров')
print(str(math.floor(Carbohydrates))+' Углеводов')
