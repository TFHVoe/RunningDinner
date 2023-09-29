import pandas as pd

df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')

def kookadresishuisadres(df):
    """Functie die telt hoe vaak het kook adres niet gelijk is aan het huisadres."""
    count_kook_adres_is_niet_huisadres = 0
    gangen = ['Voor','Hoofd','Na']
    for i in range(len(df)):
        if df.iloc[i,6] in gangen:
            if df.iloc[i, 1] == df.loc[df.iloc[i,0],df.iloc[i,6]]: #Loop die controleert of het huisadres gelijk is aan het kookadres. 
                count_kook_adres_is_niet_huisadres += 1
    return count_kook_adres_is_niet_huisadres