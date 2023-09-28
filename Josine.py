import pandas as pd
#twee verschillende deelnemers zo weining mogelijk met elkaar aan tafel
df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')

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
