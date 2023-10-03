import pandas as pd
import numpy as np
df = pd.read_excel('Running Dinner eerste oplossing 2023 v2.xlsx')

#continue

for i in range(len(df)):
    for j in range(len(df)):
        if i == j:
            continue
        else:
            change1 = df.iloc[i,3]
            change2 = df.iloc[j,3]

            df.iloc[j,3] = change1
            df.iloc[i,3] = change2
            print(change1, change2)
