import json
import requests
import notify2
from bs4 import BeautifulSoup

def getrates():
    url = 'https://www.coingecko.com/en/price_charts/bitcoin/inr' # header = {'user-Agent': 'Mozilla/5.0'}
    
    bitfile = requests.get(url)
    soup_object = BeautifulSoup(bitfile.text,'html.parser')

    bits = []
    for tbl in soup_object.find_all('table', attrs = {'class':'table'}):
        for td in tbl.find_all('td'):
            bits.append(td.text)

    del bits[3:]
    bits = list(map(lambda s : s.strip(), bits))

    return bits

rates = getrates()
rates_set = ''
rates_set = rates_set + rates[0] + ':' + rates[2].encode('utf-8') + '\n'
