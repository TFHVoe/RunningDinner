import pandas as pd
import numpy as np
df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')
df_adressen = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Adressen" )


def count_aantal_eters_voldoed(df, df_adressen):
    """Functie die telt hoevaak een bewoner voor een gaste aantal moet koken dat buiten het minimun of maximum valt van gasten waarvoor ze kunnen koken."""
    
    count_aantal_eters_voldoed = 0
    unique = []
    for i in range(len(df)):
        if df.iloc[i,2] not in unique:      
            unique.append(df.iloc[i,2])
            for j in range(len(df_adressen)):
                if df.iloc[i,2] == df_adressen.iloc[j,0] and (df_adressen.iloc[j,1] == np.nan and df_adressen[j,2] == np.nan): #Functie die controleert of de addressen gelijk zijn en dat de mensen die niet hoeven te koken niet meegenomen worden in de som.
                    if (df_adressen.iloc[j, 1] <= df.iloc[i,7] <= df_adressen.iloc[j,2]) == False:
                        count_aantal_eters_voldoed += 1        
    return count_aantal_eters_voldoed



