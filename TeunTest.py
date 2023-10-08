import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_excel('Oplossing 1 Running dinner 2023.xlsx')


df = pd.read_excel('Running Dinner tweede oplossing 2023 v2.xlsx')
ts = {} #Tafelschikking D X G --> A
gangen = ['Voor','Hoofd','Na']
for j in gangen:
    for i in range(len(df)):
        ts[(df.iloc[i, 1], j)] = df.loc[i, j]
print(ts)