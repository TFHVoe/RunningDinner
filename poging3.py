#Libraries 
import pandas as pd

#Functies eisen: 

#Functies wensen:
def hoofdgerecht2022(gt, df_kookte_2021): #Functie die telt hoe vaak een huis houden het vorige jaar en dit jaar moet koken.
    """Functie die telt hoe vaak een huishouden dat in 2022 een hoofdgerecht bereid heeft, ook een hoofdgerecht bereidt tijdens de komende Running Dinner."""
    count_hoofdgerecht2022 = 0 #Count van aantal.
    hh = {} #Huisadress kookte hoofdgerecht vorig jaar.
    for i in range(len(df_kookte_2021)):
        hh[df_kookte_2021.iloc[i,0]] = df_kookte_2021.iloc[i,1]

    for j, k in gt.items():
        for l, m in hh.items():
            if j == l and k == m == 'Hoofd': #Twee for loops die kijken of de huisadressen gelijk zijn en dat het een hoofdgerecht is.
             count_hoofdgerecht2022 += 1
    return count_hoofdgerecht2022    
def voorkeursgang(df, df_adressen):#Functie die telt hoevaak een voorkeur gang juist is.
    """Functie kijkt of de voorkeur gang van een huisaderes aan dit huisaderes toegekent is."""
    count_voorkeur = 0 #Count van aantal
    vg = {} #Huisadressen met hun voorkeur
    for i in range(len(df_adressen)):
        vg[df.iloc[i,0]] = df.iloc[i, 3]

    for j, k in vg.items():
        for l, m in gt.items():
            if j == l and k == m: #Twee for loops die kijken voor ieder huisaderes of hiet de voorkeur gang gekookt wordt
                count_voorkeur += 1
    return count_voorkeur

#Data inladen 
df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')
df_adressen = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Adressen" )
df_kookte_2021 = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Kookte vorig jaar")

#Dictionarys met de beslisvariable 
gt = {} #Gangtoewijzing A --> G
for i in range(len(df)):
    gt[df.iloc[i,2]] = df.iloc[i,6]
#print(gt)

ts = {} #Tafelschikking D X G --> A
gangen = ['Voor','Hoofd','Na']
for j in gangen:
    for i in range(len(df)):
        ts[(df.iloc[i, 1], j)] = df.loc[i, j]
#print(ts)

#Gebruik functies

count_hoofdgerecht2022 = hoofdgerecht2022(gt, df_kookte_2021)
print(count_hoofdgerecht2022)
count_voorkeur = voorkeursgang(df, df_adressen)
print(count_voorkeur) 