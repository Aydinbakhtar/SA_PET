from enum import unique
import pandas as pd
import numpy as np

df = pd.read_csv('MONTHLY_ETP_FULL.csv')

columns = ['climate', 'Code', 'daytime', 'Tmax', 'Tmin', 'Rhmean', 'u2', 'GAMA', 'Rn', 'G', 'es']

df1 = pd.DataFrame(df, columns=columns)
# print(df1)

df1 = df1.round({'Tmax' : 2, 'Tmin' : 2, 'Rhmean' :2, 'u2' : 2, 'GAMA': 2, 'Rn' :2, 'G' :2, 'es': 2})

# print(df1)

climates= df1['climate'].unique()
print('climates=', climates)

group1 = df1.groupby("climate")["Tmax"].count()
print(group1)

for cliamte, data in df1.groupby('climate'):
    data.to_csv("{}.csv".format(cliamte))






