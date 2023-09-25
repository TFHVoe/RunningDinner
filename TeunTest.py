import pandas as pd

df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')
df_tafelgenoot_2021 = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Tafelgenoot vorig jaar")

#tv = []
#for j in range(3,6):
#    for i in range(len(df)):
#        x = df.iloc[df[df.iloc[:,3] == df.iloc[0,3]].index.values,1].tolist()
#        for k in x:
#            if df.iloc[i, 2] != df.iloc[i, j] != x[i]:
           
#                tv.append((df.iloc[i,1],k))
#print(len(tv))
#print(tv)




x = df.iloc[df[df.iloc[:,3] == df.iloc[0,3]].index.values,1].tolist()
print(x)




#print(tv[0])
#lst = []
#for i in range(10):
#    for j in range(10):
#        lst.append((i,j))
#print(lst)