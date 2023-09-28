#Libraries 
import pandas as pd

#Functies eisen: 
def elkegangandradres(ts):#Funcite die telt hoe vaak er niet door een persoon een voor, hoofd en nagerecht gegeten wordt en dat dit op een ander adres is.
    """Functie die telt hoe vaak niet door ieder persoon 3 gangen op verschillende adressen gegeten wordt."""
    lst_unique = []
    for i, j in ts.items():
        for k in i[0:2:len(i)]: #For loop die een lijst vult met alle unique deelnemers.
            if k not in lst_unique:
                lst_unique.append(k)

    lst_amount = []
    gangen = ['Voor','Hoofd','Na']
    for i in lst_unique:
        countabc = 0
        lst_adres = []
        for j, k in ts.items(): #Een complex van for loops die controlleert dat iedere deelnemer een voor, hoofd en na gerecht eet en dat geen gang op hetzelfde adres gegeten wordt. 
            for l in gangen:
                if i == j[0] and j[1] == l and k not in lst_adres:
                    countabc += 1
                    lst_adres.append(k)
        lst_amount.append(countabc)

    fout_count = 0
    for i in lst_amount:
        if i != 3:      #Een for loop die telt hoe vaak er niet voldaan wordt aan de eisen dat er een voor, hoofd en nagerecht gegeten wordt en dat dit op een ander adres is.    
            fout_count += 1
    return fout_count

#Functies wensen:
def meerdermalentafelgenoot(df):#Functi die telt hoe vaak er twee personen meer dat twee keer aan de zelfde tafel zitten.
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
def hoofdgerecht2022(gt, df_kookte_2021): #Functie die telt hoe vaak een huis houden het hoofdgerecht vorige jaar en dit jaar moet koken.
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
            if j == l and k == m: #Twee for loops die kijken voor ieder huisaderes of hier de voorkeur gang gekookt wordt.
                count_voorkeur += 1
    return count_voorkeur
def zelfdetafelpartners2022(df, df_tafelgenoot_2022):#Functie die telt hoevaak twee tafelgenoten in 2022 ook de tafelgenoot van 2023 waren.
    """Functie die telt hoe vaak twee deelnemers die in 2022 bij elkaar aan tafel zaten, in 2023 weer elkaars tafelgenoot waren."""
    countzelfdetafelpartner2021 = 0
    lst = []
    for i in range(1,len(df_tafelgenoot_2022)):
        lst.append((df_tafelgenoot_2022.iloc[i,0], df_tafelgenoot_2022.iloc[i,1])) #Lijst met alle paren die bij elkaar aan tafel hebben gezeten in 2022.

    lst_2023 = []
    for k in range(3,6):
       for j in range(len(df)):
           x = df.iloc[:,1][df.iloc[:,k] == df.iloc[j,k]] #Lijst van alle paren die bij elkaar gaan zitten per gang.
           for i in x:
                lst_2023.append((df.iloc[j,1],i))

       for i in lst_2023:
           if i[0] == i[1]:   # Verwijdert het personen paar wanneer de personen in het personenpaar hetzelfde zijn.
               lst_2023.remove(i)

    con = []
    lst_2023_2 = []
    for i in lst_2023:
        if i[0] + i[1] and i[1] + i[0] not in con: #Controleert of het personen paar niet twee keer voor komt in geval dat a = b en b = a.
            con.append(i[0]+i[1])
            lst_2023_2.append(i)

    for i in lst_2023_2:
        for j in lst:
            if i[0]+i[1] == j[0]+j[1] or i[1]+i[0] == j[0]+j[1] or i[0]+i[1] == j[1]+j[0] or i[1]+i[0] == j[1]+j[0]: #Telt 1 op bij de teller wanneer twee personen vorig jaar en dit jaar bij elkaar aan tafel zaten. 
                countzelfdetafelpartner2021 += 1
    return countzelfdetafelpartner2021
def metdeburenaantafel(df, df_buren):#Functie die telt hoevaak er met de driecte buren aan tafel gezeten wordt.
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
def zelfdetafelpartners2021(df, df_tafelgenoot_2021):#Functie die telt hoevaak twee tafelgenoten in 2021 ook de tafelgenoot van 2023 waren.
    """Functie die telt hoe vaak twee deelnemers die in 2022 bij elkaar aan tafel zaten, in 2023 weer elkaars tafelgenoot waren."""
    countzelfdetafelpartner2021 = 0
    lst = []
    for i in range(1,len(df_tafelgenoot_2021)):
        lst.append((df_tafelgenoot_2021.iloc[i,0], df_tafelgenoot_2021.iloc[i,1])) #Lijst met alle paren die bij elkaar aan tafel hebben gezeten in 2021.

    lst_2023 = []
    for k in range(3,6):
       for j in range(len(df)):
           x = df.iloc[:,1][df.iloc[:,k] == df.iloc[j,k]] #Lijst van alle paren die bij elkaar gaan zitten per gang.
           for i in x:
                lst_2023.append((df.iloc[j,1],i))

       for i in lst_2023:
           if i[0] == i[1]:   # Verwijdert het personen paar wanneer de personen in het personenpaar hetzelfde zijn.
               lst_2023.remove(i)

    con = []
    lst_2023_2 = []
    for i in lst_2023:
        if i[0] + i[1] and i[1] + i[0] not in con: #Controleert of het personen paar niet twee keer voor komt in geval dat a = b en b = a.
            con.append(i[0]+i[1])
            lst_2023_2.append(i)

    for i in lst_2023_2:
        for j in lst:
            if i[0]+i[1] == j[0]+j[1] or i[1]+i[0] == j[0]+j[1] or i[0]+i[1] == j[1]+j[0] or i[1]+i[0] == j[1]+j[0]: #Telt 1 op bij de teller wanneer twee personen vorig jaar en dit jaar bij elkaar aan tafel zaten. 
                countzelfdetafelpartner2021 += 1
    return countzelfdetafelpartner2021

def wensen(df, gt, df_kookte_2021, df_adressen, df_tafelgenoot_2022, df_buren, df_tafelgenoot_2021):#Een functie de alle wensen uitvoert
    count_meer_dan_twee_keer_zelfde_persoon = meerdermalentafelgenoot(df)
    count_hoofdgerecht2022 = hoofdgerecht2022(gt, df_kookte_2021)
    count_voorkeur = voorkeursgang(df, df_adressen)
    count_zelfde_tafelpartner_2022 = zelfdetafelpartners2022(df, df_tafelgenoot_2021)
    count_met_buren_aan_tafel = metdeburenaantafel(df, df_buren)
    count_zelfde_tafelpartner_2021 = zelfdetafelpartners2021(df, df_tafelgenoot_2021)
    return count_meer_dan_twee_keer_zelfde_persoon ,count_hoofdgerecht2022, count_voorkeur, count_zelfde_tafelpartner_2021, count_met_buren_aan_tafel

#Data inladen 
df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')
df_adressen = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Adressen" )
df_kookte_2021 = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Kookte vorig jaar")
df_tafelgenoot_2021 = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Tafelgenoot vorig jaar")
df_buren = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Buren" )

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
#print(s)

#Gebruik functies

wensen  = wensen(df, gt, df_kookte_2021, df_adressen, df_tafelgenoot_2021, df_buren, df_tafelgenoot_2021)
print(wensen)