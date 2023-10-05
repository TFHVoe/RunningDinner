import pandas as pd
import numpy as np
df = pd.read_excel('Running Dinner eerste oplossing 2023 v2.xlsx')

#continue

gebr_oplossing = dict()
verwisselde_personen = []
for i in range(3):
    for j in range(3):
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

   


            
            

