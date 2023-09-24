import pandas as pd
import numpy as np
df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')
print(df)
H_adres = df.iloc[:,2]

"""Elke gang wordt gegeten door iedere deelnemer:"""

df.iloc[:,3].isin(H_adres) #Dwingt af dat iedere deelnemer het voorgerecht eet op een adress.
df.iloc[:,4].isin(H_adres) #Dwingt af dat iedere deelnemer het hoofdgerecht eet op een adress.
df.iloc[:,5].isin(H_adres) #Dwingt af dat iedere deelnemer het nagerecht eet op een adress.

"""True wanneer de bewoner moet koken."""

elementen_gang = ['Voor', 'Hoofd', 'Na']
df.iloc[:,6].isin(elementen_gang) #Wanneer iemand kookt is het element een van de drie elementen in elementen_gang.

"""Gastheer en/of gastvrouw moeten gedurende de gang die zij bereiden aanwezig zijn op hun eigen huisadres."""

