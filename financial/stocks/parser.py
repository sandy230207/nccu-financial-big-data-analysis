import pandas as pd

df = pd.read_csv('result.csv', encoding='utf-8')
for index, row in df.iterrows():
    data = row['新聞'] 
    if data.count('漲') > data.count('跌'):
        with open('train/pos/' + str(index) + '.txt', 'w', encoding='utf-8') as f:
            f.writelines(data)
    if data.count('跌') > data.count('漲'):
        with open('train/neg/' + str(index) + '.txt', 'w', encoding='utf-8') as f:
            f.writelines(data)