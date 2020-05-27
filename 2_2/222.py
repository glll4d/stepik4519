import pandas as pd


df = pd.read_excel("salaries.xlsx")

df_median = df.median(axis=1)
print(df[df_median == df_median.max()])

df_mean = df.mean(axis=0)
print(df_mean[df_mean == df_mean.max()])
