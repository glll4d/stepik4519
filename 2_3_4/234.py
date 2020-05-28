import pandas as pd
import math

df1 = pd.read_excel("trekking3.xlsx", sheet_name='Справочник')
df2 = pd.read_excel("trekking3.xlsx", sheet_name='Раскладка')

for i in range(df2.shape[0]):
    df3 = pd.merge(left=df2, right=df1, left_on='Продукт', right_on='Unnamed: 0')

aDay = []
aCallories = []
aProteins = []
aFats = []
aCarbohydrates = []

for i in range(1, df3['День'].max()+1):
    aDay.append(i)
    df4 = df3[df3['День'] == i]
    df4.reset_index(inplace=True, drop=True)
    Callories = 0
    Proteins = 0
    Fats = 0
    Carbohydrates = 0
    for j in range(df4.shape[0]):
        if not math.isnan(df4['ККал на 100'][j]):
            Callories += df4['ККал на 100'][j] / 100 * df4['Вес в граммах'][j]
        if not math.isnan(df4['Б на 100'][j]):
            Proteins += df4['Б на 100'][j] / 100 * df4['Вес в граммах'][j]
        if not math.isnan(df4['Ж на 100'][j]):
            Fats += df4['Ж на 100'][j] / 100 * df4['Вес в граммах'][j]
        if not math.isnan(df4['У на 100'][j]):
            Carbohydrates += df4['У на 100'][j] / 100 * df4['Вес в граммах'][j]
    aCallories.append(math.floor(Callories))
    aProteins.append(math.floor(Proteins))
    aFats.append(math.floor(Fats))
    aCarbohydrates.append(math.floor(Carbohydrates))

df_ans = pd.DataFrame({'Day': aDay,
                       'Callories': aCallories,
                       'Proteins': aProteins,
                       'Fats': aFats,
                       'Carbohydrates': aCarbohydrates})
print(df_ans)