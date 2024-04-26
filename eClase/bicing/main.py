import pandas as pd

file = '/dades/davidMartinez/bicing.csv'

cols = ['station_id', 'name', 'capacity']

csv = pd.read_csv(file, index_col=cols[0], usecols=cols)

max, min = 0, 1000
maxIndex, minIndex = 0, 0

all = 0

for index, row in csv.iterrows():
    name = row['name']
    cap = row['capacity']

    all += cap

    if int(cap) > max:
        max = cap
        maxIndex = index
    
    if int(cap) < min:
        min = cap
        minIndex = index

print(max, min, all)
print(csv.iloc[maxIndex])
print(csv.iloc[minIndex])