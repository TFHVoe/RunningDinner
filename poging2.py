import pandas as pd
import numpy as np
df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')
df_adressen = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Adressen" )
print(df)
H_adres = df.iloc[:,2]

"""Elke gang wordt gegeten door iedere deelnemer:"""

df.iloc[:,3].isin(H_adres) #Dwingt af dat iedere deelnemer het voorgerecht eet op een adress.
df.iloc[:,4].isin(H_adres) #Dwingt af dat iedere deelnemer het hoofdgerecht eet op een adress.
df.iloc[:,5].isin(H_adres) #Dwingt af dat iedere deelnemer het nagerecht eet op een adress.

"""True wanneer de bewoner moet koken."""

elementen_gang = ['Voor', 'Hoofd', 'Na']
a = df.iloc[:,6].isin(elementen_gang) #Wanneer iemand kookt is het element een van de drie elementen in elementen_gang.

"""Gastheer en/of gastvrouw moeten gedurende de gang die zij bereiden aanwezig zijn op hun eigen huisadres."""
count1 = 0
count2 = 0
for j in elementen_gang:                                        
    for i in range(len(df)):
        if df.iloc[i,6] == j and df.iloc[i,2] == df.loc[i, j]: #Controleert dat wanneer iemand een gang kookt hij ook thuis is.  
            #print(df.iloc[i,2], df.loc[i, j], df.iloc[i,6])
            count1 +=1
if count1 == sum(a):    #Controleert of het aantal mensen die koken en het aantal mensen dat op hun thuisadress koken overeen komen. 
    print(True)

"""Het minimale aantal gasten per huisadres."""