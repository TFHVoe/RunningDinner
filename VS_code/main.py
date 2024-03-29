#Libraries 
import pandas as pd
import numpy as np
import logging
import sys
import matplotlib.pyplot as plt

logger = logging.getLogger(name='sa-logger')
logging.basicConfig(level=logging.DEBUG,
format='[%(asctime)s] %(message)s',
handlers=[logging.FileHandler("sa.log"),logging.StreamHandler(stream=sys.stdout)])
logging.getLogger('matplotlib.font_manager').disabled = True
 
#Functies eisen: 
def ElkeGangAnderAdres(ts):#Functie die telt hoe vaak er niet door een persoon een voor, hoofd en nagerecht gegeten wordt en dat dit op een ander adres is.
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
def MoetKoken(df):#Functie die telt hoe vaak er een persoon niet kookt die wel moet koken.    """Functie die telt hoe vaak het kook adres niet gelijk is aan het huisadres."""
    """Functie die telt hoeveel mensen die een van de gangen moet koken niet kookt."""
    count_kook_adres_is_niet_huisadres = 0
    gangen = ['Voor','Hoofd','Na']
    for i in range(len(df)):
        if df.iloc[i,6] in gangen:
            if df.iloc[i,2] != df.loc[i,df.iloc[i,6]]:
                count_kook_adres_is_niet_huisadres +=1 
    return count_kook_adres_is_niet_huisadres
    
    return count_bewoners_die_moeten_koeken_maar_niet_koken         
def KookadresIsHuisadres(df):#Functie die telt hoe vaak het kook adres niet gelijk is aan het thuisaders.
    """Functie die telt hoe vaak het kook adres niet gelijk is aan het huisadres."""
    count_kook_adres_is_niet_huisadres = 0
    gangen = ['Voor','Hoofd','Na']
    for i in range(len(df)):
        if df.iloc[i,6] in gangen:
            if df.iloc[i,2] != df.loc[i,df.iloc[i,6]]: #Controleert of het huisadres gelijk is aan het kookaders.
                count_kook_adres_is_niet_huisadres +=1 
    return count_kook_adres_is_niet_huisadres 
def CountAantalEtersVoldoed(df, df_adressen):#Functie die telt hoe vaak het gasten aantal waarvoor ze moeten koken buit het gasten aantal waarvoor ze kunnen koken ligt.
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
def PaarBijElkaar(df, df_paar_blijft_bij_elkaar):#Functie die telt hoe vaak een paar dat bij elkaar moet blijven niet bij elkaar is.
    """Functie die telt hoe vaak een paar die bij elkaar moet zitten niet bij elkaar zit."""

    count_PaarNietBijElkaar = 0
    for i in range(1,len(df_paar_blijft_bij_elkaar)):
        a = df.loc[df["Bewoner"]== df_paar_blijft_bij_elkaar.iloc[i,0]]
        b = df.loc[df["Bewoner"]== df_paar_blijft_bij_elkaar.iloc[i,1]]
        a.reset_index(drop = True, inplace = True)
        b.reset_index(drop = True, inplace = True) 
        if (a["Voor"][0] == b["Voor"][0] and a["Hoofd"][0] == b["Hoofd"][0] and b["Na"][0] == a["Na"][0]) == 0:
            count_PaarNietBijElkaar += 1   
    return count_PaarNietBijElkaar

def eisen(ts, df, df_adressen, df_paar_blijft_bij_elkaar):#Een Functie die alle eisen controleert.
    count_elke_gang_anders = ElkeGangAnderAdres(ts)
    moet_koken = MoetKoken(df)
    kookadres_is_huisadres = KookadresIsHuisadres(df)
    count_aantal_eters_voldoed = CountAantalEtersVoldoed(df, df_adressen)
    paar_bij_elkaar = PaarBijElkaar(df, df_paar_blijft_bij_elkaar)

    return count_elke_gang_anders + moet_koken + kookadres_is_huisadres + count_aantal_eters_voldoed + paar_bij_elkaar

#Functies wensen:
def MeerdereMalenTafelgenoot(df):#Functie die telt hoe vaak er twee personen meer dat twee keer aan de zelfde tafel zitten.
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
    count_DezelfdeTafelgenoot2OfMeer = 0

    for i in unique_lst_2023_amount:
        if i > 2:
            count_DezelfdeTafelgenoot2OfMeer += 1 #Het tellen hoe vaak er een twee personen meer dan twee keer bij elkaar aan aantal aan tafel zitten.
    return count_DezelfdeTafelgenoot2OfMeer
def Hoofdgerecht2022(gt, df_kookte_2021): #Functie die telt hoe vaak een huis houden het hoofdgerecht vorige jaar en dit jaar moet koken.
    """Functie die telt hoe vaak een huishouden dat in 2022 een hoofdgerecht bereid heeft, ook een hoofdgerecht bereidt tijdens de komende Running Dinner."""
    count_Hoofdgerecht2022 = 0 #Count van aantal.
    hh = {} #Huisadress kookte hoofdgerecht vorig jaar.
    for i in range(len(df_kookte_2021)):
        hh[df_kookte_2021.iloc[i,0]] = df_kookte_2021.iloc[i,1]

    for j, k in gt.items():
        for l, m in hh.items():
            if j == l and k == m == 'Hoofd': #Twee for loops die kijken of de huisadressen gelijk zijn en dat het een hoofdgerecht is.
             count_Hoofdgerecht2022 += 1
    return count_Hoofdgerecht2022    
def Voorkeursgang(df, df_adressen):#Functie die telt hoevaak een voorkeur gang juist is.
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
def DezelfdeTafelpartners2022(df, df_tafelgenoot_2022):#Functie die telt hoevaak twee tafelgenoten in 2022 ook de tafelgenoot van 2023 waren.
    """Functie die telt hoe vaak twee deelnemers die in 2022 bij elkaar aan tafel zaten, in 2023 weer elkaars tafelgenoot waren."""
    CountDezelfdeTafelpartner2022 = 0
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
                CountDezelfdeTafelpartner2022 += 1

    return CountDezelfdeTafelpartner2022
def MetDeBurenAanTafel(df, df_buren):#Functie die telt hoevaak er met de driecte buren aan tafel gezeten wordt.
    """Functie die telt hoe vaak er met de directe buren aan tafel gezeten wordt"""
    CountDezelfdeBuren = 0
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
                    CountDezelfdeBuren += 1
    return CountDezelfdeBuren
def DezelfdeTafelpartners2021(df, df_tafelgenoot_2021):#Functie die telt hoevaak twee tafelgenoten in 2021 ook de tafelgenoot van 2023 waren.
    """Functie die telt hoe vaak twee deelnemers die in 2022 bij elkaar aan tafel zaten, in 2023 weer elkaars tafelgenoot waren."""
    CountDezelfdeTafelpartner2021 = 0
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
                CountDezelfdeTafelpartner2021 += 1
    return CountDezelfdeTafelpartner2021

def wensen(df, gt, df_kookte_2022, df_adressen, df_tafelgenoot_2022, df_buren, df_tafelgenoot_2021):#Een Functie die alle wensen controleert.
    count_meer_dan_twee_keer_zelfde_persoon = MeerdereMalenTafelgenoot(df)
    count_hoofdgerecht2022 = Hoofdgerecht2022(gt, df_kookte_2022)
    count_voorkeur = Voorkeursgang(df, df_adressen)
    count_zelfde_tafelpartner_2022 = DezelfdeTafelpartners2022(df, df_tafelgenoot_2022)
    count_met_buren_aan_tafel = MetDeBurenAanTafel(df, df_buren)
    count_zelfde_tafelpartner_2021 = DezelfdeTafelpartners2021(df, df_tafelgenoot_2021)

    return  count_meer_dan_twee_keer_zelfde_persoon * 0.3 + count_hoofdgerecht2022 * 0.2 + count_voorkeur * 0.175 + count_zelfde_tafelpartner_2022 * 0.15 + count_met_buren_aan_tafel * 0.125 + count_zelfde_tafelpartner_2021 * 0.05

#Data inladen 
df = pd.read_excel('Running Dinner tweede oplossing 2023 v2.xlsx')
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

#Visualisatie
def plot(X, Y, Y1):#De plot van de iteraties tegen de oplossing voor deze iteratie
    """Functie voor het plotten van de grafiek: iteraties tegen de oplossing voor deze iteratie """
    plt.plot(X,Y)
    plt.plot(X,Y1, 'r')
    plt.title('Uitkomsten Toegestanen Oplossingen per Iteratie')
    plt.xlabel('Iteratie')
    plt.ylabel('Oplossing')
    plt.show()


#2 opt toegepast bij running dinner
def TwoOpt(df, gt, df_kookte_2022, df_adressen, df_tafelgenoot_2022, df_buren, df_tafelgenoot_2021, ts, df_paar_blijft_bij_elkaar, verwisselingen, gang_wissel):
    """
    Returns een verbeterde tafel planning na een meegegeven aantal twee-opt verwisselingen.
    
    Args:
        df (dataframe):                         Start oplossing
        gt (dictionary):                        Gerecht per adres
        ts (dictionary):                        Bewoner voor gerecht per adres
        df_kookte_2022 (dataframe):             Wie wat kookte in 2022
        df_adressen (dataframe):                Bewoner per adres
        df_tafelgenoot_2022 (dataframe):        Tafelgenoten 2022
        df_buren (dataframe):                   Directe buren per adres
        df_tafelgenoot_2022 (dataframe):        Tafelgenoten 2021
        df_paar_blijft_bij_elkaar (dataframe):  Bewoners die ieder gerecht bij elkaar blijven
        verwisselingen (int):                   Hoeveel verwisselingen tot het uitschrijven van een verbeterde oplossing en visualisatie
        gang_wissel (int):                      Na hoeveel verwisselingen er in de gangen gewisselt wordt
    
    Return:
        'Verbeterde planning Running dinner 2023.xlsx': een excel bestand met een verbeterde planning.
    """

    moment0 = wensen(df, gt, df_kookte_2022, df_adressen, df_tafelgenoot_2022, df_buren, df_tafelgenoot_2021)
    logger.debug(msg=f'Start:{moment0}')
    class IteratiePerGang(Exception): pass
    
    verwisselde_personen = []
    iteratie = 0  
    improved = True
    gangen = ['','','Voor','Hoofd','Na']
    X = []
    Y = []
    Y1 = []
    X.append(0)
    Y.append(moment0)
    Y1.append(moment0)
    while improved:
        for k in range(2,5):
            loc_iteratie = 0
            try:   
                for i in range(len(df)):
                    for j in range(len(df)):
                        if i == j:
                            continue
                        else:
                            df_new = df.copy()
                            change1 = df.iloc[i,k]
                            change2 = df.iloc[j,k]      #De verwisseling van de twee cellen
                            df_new.iloc[j,k] = change1
                            df_new.iloc[i,k] = change2

                            koppel = []
                            persoon1 = df.iloc[i,1]
                            persoon2 = df.iloc[j,1]   #Het maken van een tuple met het verwisselde koppel en de gang.
                            koppel.append(persoon1)
                            koppel.append(persoon2)
                            koppel.append(gangen[k])
                    
                            tup = tuple(sorted(koppel))
                            if tup not in verwisselde_personen:  #Het zorgen dat er alleen gekeken wordt naar unique oplossing door de verwisselde bewoners en de gang in een lijste te stoppen.
                                verwisselde_personen.append(tup)

                                if eisen(ts, df_new, df_adressen, df_paar_blijft_bij_elkaar) > 0: #De controlle dat er geen eisen overschreden worden
                                    continue

                                else:
                                    sol = wensen(df_new, gt, df_kookte_2022, df_adressen, df_tafelgenoot_2022, df_buren, df_tafelgenoot_2021) 
                                    start = wensen(df, gt, df_kookte_2022, df_adressen, df_tafelgenoot_2022, df_buren, df_tafelgenoot_2021)
                                    iteratie += 1
                                    loc_iteratie += 1
                                    logger.debug(msg=f'Iteratie:{iteratie}, local:{loc_iteratie}')

                                    X.append(iteratie)
                                    Y.append(sol)
                                

                                    if sol < start: #Wanneer de oplossing kleiner is dan de start wordt de oplossing de nieuwe start.
                                        df = df_new
                                        improved = True
                                        logger.debug(msg=f'Oplossing:{sol}')
                                        Y1.append(sol)
                                    else:
                                        Y1.append(start)

                                    if iteratie % verwisselingen == 0:
                                        df.to_excel('Verbeterde planning Running dinner 2023.xlsx', index = False) #Als er 1000 itearteis zijn geweest wordt er een grafiek gemaakt en een oplossing in een excel bestand gegenereerd.
                                        plot(X,Y,Y1)

                                    
                                    if loc_iteratie == gang_wissel:
                                        raise IteratiePerGang()
                                              
                
            except IteratiePerGang:
                pass

verwisselingen = 1500
gang_wissel = 3
TwoOpt(df, gt, df_kookte_2022, df_adressen, df_tafelgenoot_2022, df_buren, df_tafelgenoot_2021, ts, df_paar_blijft_bij_elkaar, verwisselingen, gang_wissel)