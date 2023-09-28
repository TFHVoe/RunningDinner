def zelfdetafelpartners2021(df, df_tafelgenoot_2021):#Functie die telt hoevaak twee tafelgenoten in 2022 ook de tafelgenoot van 2023 waren.
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