import pandas as pd

df = pd.read_excel('Running Dinner eerste oplossing 2022.xlsx')

ts = {} #Tafelschikking D X G --> A
gangen = ['Voor','Hoofd','Na']
for j in gangen:
    for i in range(len(df)):
        ts[(df.iloc[i, 1], j)] = df.loc[i, j]
#print(ts)

lst_unique = []
for i, j in ts.items():
    for k in i[0:2:len(i)]:
        if k not in lst_unique:
            lst_unique.append(k)

lst_amount = []
gangen = ['Voor','Hoofd','Na']
for i in lst_unique:
    countabc = 0
    for j, k in ts.items():
        for l in gangen:
            if i == j[0] and j[1] == l:
                countabc += 1
    lst_amount.append(countabc)

for i in lst_amount:
    if i != 3:
        print('Voldoet niet')
print(lst_amount)

