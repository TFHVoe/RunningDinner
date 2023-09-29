import pandas as pd

df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')
df_bewoners = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Bewoners" )

gt = {} #Gangtoewijzing A --> G
for i in range(len(df)):
    gt[df.iloc[i,2]] = df.iloc[i,6]


def moetkoken(df, df_bewoners):#Functie die telt hoe vaak er een persoon niet kookt die wel moet koken of andersom.
    """Functie die telt hoeveel mensen die een van de gangen moet koken niet kookt."""
    count_bewoners_die_moeten_koeken_maar_niet_koken = 0
    gangen = ['Voor','Hoofd','Na']
    for i in range(len(df)):
        for j in range(len(df_bewoners)):
            if df_bewoners.iloc[j,2] != 1 and df.iloc[i,1] == df_bewoners.iloc[j, 0] and df.iloc[i,6] not in gangen: #For loop die controlleert of er geen bewoner is die moet koken die niet een van de gangen kookt. 
                count_bewoners_die_moeten_koeken_maar_niet_koken += 1 
    
    return count_bewoners_die_moeten_koeken_maar_niet_koken               



