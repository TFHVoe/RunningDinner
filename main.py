import pandas as pd
import numpy as np
df_bewoners = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Bewoners" )
df_adressen = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Adressen" )
df_paar_blijft_bij_elkaar = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Paar blijft bij elkaar" )
df_buren = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Buren" )
df_kookte_2021 = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Kookte vorig jaar")
df_tafelgenoot_2021 = pd.read_excel("Running Dinner dataset 2022.xlsx",sheet_name="Tafelgenoot vorig jaar")

#Indices
A = df_adressen.iloc[:,0] #Huisadressen
D = df_bewoners.iloc[:,0] #Bewoners/Deelnemers
bijelkaar = ["WO_59_M_Dré", "WO_59_V_Els","WO_25_M_Bar","WO_25_V_Bet"]
E = df_bewoners[df_bewoners.iloc[:,0].isin(bijelkaar)] #Bewoners/Deelnemers die bij elkaar blijven
G = ["Voor", "Hoofd", "Na"] #Gangen

#Parameters
ka = df_bewoners.iloc[:,2].replace(1, 0)
ka = df_bewoners.iloc[:,2].replace(np.NaN, 1) #1 wanneer een bewoner kookt

la = df_adressen.iloc[:,1] #Minimale aantal eters op adres
ua = df_adressen.iloc[:,2] #Maximale aantal eters op adres
   

#c = df_adressen.loc[[A],["Huisadres","Min groepsgrootte","Max groepsgrootte","Voorkeur gang"]]

#print(c)
print(df_adressen)
