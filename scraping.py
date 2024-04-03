from bs4 import BeautifulSoup
import requests
import pandas as pd
import re

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'}

url = requests.get('https://www.transfermarkt.com.br/campeonato-brasileiro-serie-a/marktwerte/wettbewerb/BRA1/pos//detailpos/0/altersklasse/alle/plus/1',headers=headers)
table = BeautifulSoup(url.text, 'html.parser')

#extract table infos into a list
data = []
for row in table.find_all('tr'):
    row_data = []
    for cell in row.find_all('td'):
        row_data.append(cell.text)
    data.append(row_data)

data_new = []

#cut data
for index in range(len(data)):
    if data[index]==[] or len(data[index]) > 2:
        data_new.append(data[index])

#cleaning data
for index in range(len(data_new)):
    for sub_index in range(len(data_new[index])):
        data_new[index][sub_index] = re.sub(r"[\n]", "", data_new[index][sub_index]).strip()

data_new_2 = pd.DataFrame(data_new).drop(columns=[0,1,2,5,7])
print(data_new_2)
#import ipdb; ipdb.set_trace()




