import pandas as pd

df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')
df_buren = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Buren" )

def metdeburenaantafel(df, df_buren):
    """Functie die telt hoe vaak er met de directe buren aan tafel gezeten wordt"""
    countzelfdeburen = 0
    lst = []
    for i in range(1,len(df_buren)):
        lst.append((df_buren.iloc[i,0], df_buren.iloc[i,1])) #Lijst met alle buren.

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

    for i in lst_2023_2:
            for j in lst:
                if i[0]+i[1] == j[0]+j[1] or i[1]+i[0] == j[0]+j[1] or i[0]+i[1] == j[1]+j[0] or i[1]+i[0] == j[1]+j[0]: #Telt 1 op wanneer er met de directe buren aan tafel gezeten wordt.
                    countzelfdeburen += 1
    return countzelfdeburen
print(metdeburenaantafel(df, df_buren))
     

