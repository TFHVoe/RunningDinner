import pandas as pd

df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')
df_tafelgenoot_2021 = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Tafelgenoot vorig jaar")

#lst = []
#for i in range(1,len(df_tafelgenoot_2021)):
#    lst.append((df_tafelgenoot_2021.iloc[i,0], df_tafelgenoot_2021.iloc[i,1]))

lst_voor = []
#print(df)

for j in range(len(df)):
    x = df.iloc[:,1][df['Voor'] == df.iloc[j,3]]
    for i in x:
        lst_voor.append((df.iloc[j,1],i))
#print(lst_voor)


for i in lst_voor:
    j = list(i)
    if j[0] == j[1]:
        lst_voor.remove(i)


con = []
for i in lst_voor:
    j = list(i)
    if j[0] + j[1] and j[1] + j[0] not in con:
       con.append(j[0]+j[1])
    else:
        lst_voor.remove(i)
print(con)
print(lst_voor)
   

     

