import pandas as pd
#twee verschillende deelnemers zo weining mogelijk met elkaar aan tafel
df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')

#Functie die telt hoe vaak deelnemers in 2023 meerdere malen elkaars tafelgenoten zijn."""
count_dezelfdetafelgenoot2ofmeer = 0
lst_2023 = []
for k in range(3,6):
    for j in range(len(df)):
        x = df.iloc[:,1][df.iloc[:,k] == df.iloc[j,k]] #Lijst van alle paren die bij elkaar gaan zitten per gang.
        for i in x:
            lst_2023.append((df.iloc[j,1],i))

for i in lst_2023:
    j = list(i)
    if j[0] == j[1]:   # Verwijdert het personen paar wanneer de personen in het personenpaar hetzelfde zijn.
         lst_2023.remove(i)

con = []
lst_2023_2 = []
for i in lst_2023:
    if i[0] + i[1] and i[1] + i[0] not in con: #Controleert of het personen paar niet twee keer voor komt in geval dat a = b en b = a.
        con.append(i[0]+i[1])
        lst_2023_2.append(i)






#lijst met alle duo's die elkaar tegenkomen
koppels2023 = []
for i in lst_2023_2:
    koppel = i[0]+i[1]
    koppels2023.append(koppel)
    

for k in koppels2023:
    if k[0] == k[1]:
        count_dezelfdetafelgenoot2ofmeer +=1
print(count_dezelfdetafelgenoot2ofmeer)



#Data inladen 
df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')
df_adressen = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Adressen" )
df_kookte_2021 = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Kookte vorig jaar")
df_tafelgenoot_2021 = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Tafelgenoot vorig jaar")
df_buren = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Buren" )
