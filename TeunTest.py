import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#df = pd.read_excel('Oplossing 1 Running dinner 2023.xlsx')

x = [1000, 1001, 2000, 2002, 3000, 3003]

count = []
for i in x:
    if i%1000 == 0:
        count.append(i)
print(count)


