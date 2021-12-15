import pandas as pd

data = pd.DataFrame(pd.read_csv('Candy Grams Input Batch 2.csv'))
finalData = pd.DataFrame(columns=data.columns[:-1])

print(data.head())

data['Count'].fillna(1, inplace=True)
data.fillna('', inplace=True)

check = False
idx = 0

for row in data.iterrows():
        newrow = [row[1][x] for x in range(3)]
        for x in range(int(row[1][-1])):
            finalData.loc[idx] = newrow
            idx+=1


finalData.to_csv('finaldata_batch2.csv')
