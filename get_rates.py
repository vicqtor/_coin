from bs4 import BeautifulSoup
import requests
import notify2

def f():
    try:
        url = 'https://www.coingecko.com/en/price_charts/bitcoin/inr'
        # header = {'user-Agent': 'Mozilla/5.0'}
        bitfile=requests.get(url)
   
        sp=BeautifulSoup(bitfile.text,'html.parser')
     
        bits=[]
        for tbl in sp.find_all('table',attrs={'class':'table'}):
            for td in tbl.find_all('td'):
                bits.append(td.text)
       
        del bits[3:]
        bits = list(map(lambda s : s.strip(), bits))
        
        # return bits
    except:bits = []
    return bits

rts=f()

res =''

if len(rts) != 0:
    res=res+str(rts[0])+'-'+str(rts[2].encode('utf-8'))+'\n'
