import pandas as pd
import numpy as np
df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')
df_paar_blijft_bij_elkaar = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Paar blijft bij elkaar" )





# Een heel klein aantal groepjes van deelnemers, vaak één of twee duo’s, zit tijdens het gehele Running Dinner voor elke gang bij elkaar aan tafel
#setl = df.loc[df['Bewoner'] == "WO_59_V_Els"] 
#set1a = df.loc[df['Bewoner'] == "WO_59_M_Dré"]
#set1a.reset_index(drop = True, inplace = True)
#setl.reset_index(drop = True, inplace = True) 
#if setl["Voor"][0] == set1a["Voor"][0] and setl["Hoofd"][0] == set1a["Hoofd"][0] and setl["Na"][0] ==set1a["Na"][0]:
 #   print("jaaaaaaaaaaaa")
    
#print(setl)

for i in range(1,len(df_paar_blijft_bij_elkaar)):
    print(df.loc[df_paar_blijft_bij_elkaar.iloc[i,0],'Bewoner'])
        
