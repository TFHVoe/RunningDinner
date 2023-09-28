import pandas as pd

df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')

ts = {} #Tafelschikking D X G --> A
gangen = ['Voor','Hoofd','Na']
for j in gangen:
    for i in range(len(df)):
        ts[(df.iloc[i, 1], j)] = df.loc[i, j]
#print(ts)
def elkegangandradres(ts):
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

