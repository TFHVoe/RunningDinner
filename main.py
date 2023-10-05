#Libraries 
import pandas as pd
import numpy as np
import logging
import sys
logger = logging.getLogger(name='sa-logger')
logging.basicConfig(level=logging.DEBUG,
format='[%(asctime)s] %(message)s',
handlers=[logging.FileHandler("sa.log"),logging.StreamHandler(stream=sys.stdout)])
logging.getLogger('matplotlib.font_manager').disabled = True
 
#Functies eisen: 
def elkeganganderadres(ts):#Functie die telt hoe vaak er niet door een persoon een voor, hoofd en nagerecht gegeten wordt en dat dit op een ander adres is.
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
def moetkoken(df, df_bewoners):#Functie die telt hoe vaak er een persoon niet kookt die wel moet koken.
    """Functie die telt hoeveel mensen die een van de gangen moet koken niet kookt."""
    count_bewoners_die_moeten_koeken_maar_niet_koken = 0
    gangen = ['Voor','Hoofd','Na']
    for i in range(len(df)):
        for j in range(len(df_bewoners)):
            if df_bewoners.iloc[j,2] != 1 and df.iloc[i,1] == df_bewoners.iloc[j, 0] and df.iloc[i,6] not in gangen: #For loop die controlleert of er geen bewoner is die moet koken die niet een van de gangen kookt. 
                count_bewoners_die_moeten_koeken_maar_niet_koken += 1 
    
    return count_bewoners_die_moeten_koeken_maar_niet_koken         
def kookadresishuisadres(df):#Functie die telt hoe vaak het kook adres niet gelijk is aan het thuisaders.

    """Functie die telt hoe vaak het kook adres niet gelijk is aan het huisadres."""
    count_kook_adres_is_niet_huisadres = 0
    gangen = ['Voor','Hoofd','Na']
    for i in range(len(df)):
        if df.iloc[i,6] in gangen:
            if df.iloc[i, 1] == df.loc[df.iloc[i,0],df.iloc[i,6]]: #Loop die controleert of het huisadres gelijk is aan het kookadres. 
                count_kook_adres_is_niet_huisadres += 1
    return count_kook_adres_is_niet_huisadres
def countaantaletersvoldoed(df, df_adressen):#Functie die telt hoe vaak het gasten aantal waarvoor ze moeten koken buit het gasten aantal waarvoor ze kunnen koken ligt.
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
def paarbijelkaar(df, df_paar_blijft_bij_elkaar):#Functie die telt hoe vaak een paar dat bij elkaar moet blijven niet bij elkaar is.
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

def eisen(ts, df, df_bewoners, df_adressen, df_paar_blijft_bij_elkaar):#Een Functie die alle eisen controleert.
    count_elke_gang_anders = elkeganganderadres(ts)
    moet_koken = moetkoken(df, df_bewoners)
    kookadres_is_huisadres = kookadresishuisadres(df)
    count_aantal_eters_voldoed = countaantaletersvoldoed(df, df_adressen)
    paar_bij_elkaar = paarbijelkaar(df, df_paar_blijft_bij_elkaar)

    return count_elke_gang_anders + moet_koken + kookadres_is_huisadres + count_aantal_eters_voldoed + paar_bij_elkaar

#Functies wensen:
def meerdermalentafelgenoot(df):#Functie die telt hoe vaak er twee personen meer dat twee keer aan de zelfde tafel zitten.
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
        if i > 2:
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
                count_voorkeur -= 1
    return count_voorkeur
def zelfdetafelpartners2022(df, df_tafelgenoot_2022):#Functie die telt hoevaak twee tafelgenoten in 2022 ook de tafelgenoot van 2023 waren.
    """Functie die telt hoe vaak twee deelnemers die in 2022 bij elkaar aan tafel zaten, in 2023 weer elkaars tafelgenoot waren."""
    countzelfdetafelpartner2022 = 0
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
                countzelfdetafelpartner2022 += 1

    return countzelfdetafelpartner2022
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

def wensen(df, gt, df_kookte_2022, df_adressen, df_tafelgenoot_2022, df_buren, df_tafelgenoot_2021):#Een Functie die alle wensen controleert.
    count_meer_dan_twee_keer_zelfde_persoon = meerdermalentafelgenoot(df)
    count_hoofdgerecht2022 = hoofdgerecht2022(gt, df_kookte_2022)
    count_voorkeur = voorkeursgang(df, df_adressen)
    count_zelfde_tafelpartner_2022 = zelfdetafelpartners2022(df, df_tafelgenoot_2022)
    count_met_buren_aan_tafel = metdeburenaantafel(df, df_buren)
    count_zelfde_tafelpartner_2021 = zelfdetafelpartners2021(df, df_tafelgenoot_2021)

    return  count_meer_dan_twee_keer_zelfde_persoon * 0.3 + count_hoofdgerecht2022 * 0.2 + count_voorkeur * 0.175 + count_zelfde_tafelpartner_2022 * 0.15 + count_met_buren_aan_tafel * 0.125 + count_zelfde_tafelpartner_2021 * 0.05

#Data inladen 
df = pd.read_excel('Running Dinner eerste oplossing 2023 v2.xlsx')
df_bewoners = pd.read_excel("Running Dinner dataset 2023 v2.xlsx",sheet_name="Bewoners" )
df_adressen = pd.read_excel("Running Dinner dataset 2023 v2.xlsx",sheet_name="Adressen" )
df_kookte_2022 = pd.read_excel("Running Dinner dataset 2023 v2.xlsx",sheet_name="Kookte vorig jaar")
df_tafelgenoot_2022 = pd.read_excel("Running Dinner dataset 2023 v2.xlsx",sheet_name="Tafelgenoot vorig jaar")
df_buren = pd.read_excel("Running Dinner dataset 2023 v2.xlsx",sheet_name="Buren" )
df_paar_blijft_bij_elkaar = pd.read_excel("Running Dinner dataset 2023 v2.xlsx",sheet_name="Paar blijft bij elkaar" )
df_tafelgenoot_2021 = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Tafelgenoot vorig jaar")

#Dictionarys met de beslisvariable 
gt = {} #Gangtoewijzing A --> G
for i in range(len(df)):
    gt[df.iloc[i,2]] = df.iloc[i,6]

ts = {} #Tafelschikking D X G --> A
gangen = ['Voor','Hoofd','Na']
for j in gangen:
    for i in range(len(df)):
        ts[(df.iloc[i, 1], j)] = df.loc[i, j]

#Gebruik functies
logger.debug(msg=f'Start:{wensen(df, gt, df_kookte_2022, df_adressen, df_tafelgenoot_2022, df_buren, df_tafelgenoot_2021)}')
verwisselde_personen = []
itteratie = 0  
improved = True
while improved:
    impoved = False
    for i in range(len(df)):
        for j in range(len(df)):
            if i == j:
                continue
            else:
                df_new = df.copy()
                changes = []
                change1 = df.iloc[i,3]
                change2 = df.iloc[j,3]      #De verwisseling van de twee cellen
                df_new.iloc[j,3] = change1
                df_new.iloc[i,3] = change2

                koppel = []
                persoon1 = df.iloc[i,1]
                persoon2 = df.iloc[j, 1]   #Het maken van een tuple met het verwisselde koppel en de gang.
                koppel.append(persoon1)
                koppel.append(persoon2)
                koppel.append('Voor')
                
                tup = tuple(sorted(koppel))
                if tup not in verwisselde_personen:  #Het zorgen dat er alleen gekeken wordt naar unique oplossing door de verwisselde bewoners en de gang in een lijste te stoppen.
                    verwisselde_personen.append(tup)
                    if eisen(ts, df_new, df_bewoners, df_adressen, df_paar_blijft_bij_elkaar) > 0: #De controlle dat er geen eisen overschreden worden
                        continue
                    else:
                        sol = wensen(df_new, gt, df_kookte_2022, df_adressen, df_tafelgenoot_2022, df_buren, df_tafelgenoot_2021) 
                        start = wensen(df, gt, df_kookte_2022, df_adressen, df_tafelgenoot_2022, df_buren, df_tafelgenoot_2021)
                        itteratie += 1
                        logger.debug(msg=f'Itteratie:{itteratie}')                   
                        if sol < start: #Wanneer de oplossing kleiner is dan de start wordt de oplossing de nieuwe start.
                            df = df_new
                            improved = True
                            logger.debug(msg=f'Oplossing:{sol}')
