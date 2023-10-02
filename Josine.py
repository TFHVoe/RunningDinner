import pandas as pd
# Een heel klein aantal groepjes van deelnemers, vaak één of twee duo’s, zit tijdens het gehele Running Dinner voor elke gang bij elkaar aan tafel
df_paar_blijft_bij_elkaar = pd.read_excel("Running Dinner dataset 2023 v2.xlsx",sheet_name="Paar blijft bij elkaar" )
df = pd.read_excel('Running Dinner eerste oplossing 2023 v2.xlsx')

def paarbijelkaar(df, df_paar_blijft_bij_elkaar):
    """Functie die telt hoe vaak een paar die bij elkaar moet zitten niet bij elkaar zit."""

    count_paarnietbijelkaar = 0
    for i in range(1,len(df_paar_blijft_bij_elkaar)):
        a = df.loc[df["Bewoner"]== df_paar_blijft_bij_elkaar.iloc[i,0]]
        b = df.loc[df["Bewoner"]== df_paar_blijft_bij_elkaar.iloc[i,1]]
        a.reset_index(drop = True, inplace = True)
        b.reset_index(drop = True, inplace = True) 
        if (a["Voor"][0] == b["Voor"][0] and a["Hoofd"][0] == b["Hoofd"][0] and b["Na"][0] == a["Na"][0]) == 0:
            count_paarnietbijelkaar += 1   
    return count_paarnietbijelkaar

print(paarbijelkaar(df,df_paar_blijft_bij_elkaar))       

        
           
#deze eis werkt nu en is zo te gebruiken voor de data van 2023.