import pandas as pd
#twee verschillende deelnemers zo weining mogelijk met elkaar aan tafel
df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')
df_adressen = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Adressen" )

def meerdermalentafelgenoot(df):
    """Functie die telt hoe vaak deelnemers in 2023 meerdere malen elkaars tafelgenoten zijn."""

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

    sorted_lst_2023 = []
    for i in lst_2023:  #Sorteerd de inhoud van tuples in de lijst 2023 op alfabetische volgorde.
        sorted_lst_2023.append(tuple(sorted(i)))

    unique_lst_2023 = []
    for i in sorted_lst_2023:
       if i not in unique_lst_2023: #Het vullen van een lijst met de unique tuples uit de lijst list_2023.
            unique_lst_2023.append(i)

    unique_lst_2023_amount = []
    for i in unique_lst_2023:
        count_amount = 0        #Het tellen hoe vaak er een tuple in de lijst sorted_lst_2023 zit per unique tuple
        for j in sorted_lst_2023:
            if i == j:
                count_amount += 1
        unique_lst_2023_amount.append(count_amount)
    count_dezelfdetafelgenoot2ofmeer = 0

    for i in unique_lst_2023_amount:
        if i >= 2:
            count_dezelfdetafelgenoot2ofmeer += 1 #Het tellen hoe vaak er een twee personen meer dan twee keer bij elkaar aan aantal aan tafel zitten.
    return count_dezelfdetafelgenoot2ofmeer


#Het aantal tafelgenoten dat op een bepaald huisadres eet, voldoet aan de bij het adres horende minimum en maximum groepsgrootte.
#dict huisadres: aantal gasten ingeplnad, die dmv een for loop kijkt of tussen min of max aantal gasten zit anders stop loop
huisadres_ingedeelde_aantaleters = {}
for i in range(len(df)):
    huisadres_ingedeelde_aantaleters[df.iloc[i,2]] = df.iloc[i,7]
df_ingeplande_eters = pd.DataFrame({"Huisadres": huisadres_ingedeelde_aantaleters.keys(), "Aantal ingedeelde eters": huisadres_ingedeelde_aantaleters.values()})
df_ingeplande_eters = df_ingeplande_eters.fillna(0)
print(df_ingeplande_eters)
                
niets = 0                
count = []
for i in range(len(df_adressen)):
    for j in range(len(df_ingeplande_eters)):
        if df_ingeplande_eters.iloc[j,0] == df_adressen.iloc[i,0]:
            if df_adressen.iloc[i,1] <=  df_ingeplande_eters.iloc[j,1] <= df_adressen.iloc[i,2]:
                niets += 1
            else:
                print("aantal niet toegestaan")
                print(df_ingeplande_eters.iloc[i,0])
                count.append(df_adressen.iloc[i,0])
print(count)
 #niet toegestaan huishoudens als je adressen print ipv df_ingeplande_eters: WO6,WO1,VW36,VW56,WO40,WO41,W)79
 #dit is de toegelaten oplossen dus alle huishoudens zouden overeen moeten komen, heb zogenaamde foutieve adressen gecontroleerd en ze zijn toegelaten               

unique = []
for i in range(len(df)):
    if i not in unique:
        unique.append(i)    
    
  
    
    
    
    
    
# Een heel klein aantal groepjes van deelnemers, vaak één of twee duo’s, zit tijdens het gehele Running Dinner voor elke gang bij elkaar aan tafel