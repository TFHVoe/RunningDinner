import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_excel('Oplossing 1 Running dinner 2023.xlsx')
df_bewoners = pd.read_excel("Running Dinner dataset 2023 v2.xlsx",sheet_name="Bewoners" )

X= [0, 1, 2, 3]
Y = [4, 6, 8, 10]

def plot(X, Y):
    plt.plot(X,Y) 
    plt.show()


plot(X,Y)
