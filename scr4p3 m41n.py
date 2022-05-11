from distutils.filelist import findall
from email import header
from xml.etree.ElementPath import find
import requests
from bs4 import BeautifulSoup



prod = str(input("product:"))
proddict = {}

url1 = "https://www.olx.in/bengaluru_g4058803/q-"+prod+"?isSearchCall=true"
headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
html_T1 = requests.get(url1, headers=headers)
souped1 = BeautifulSoup(html_T1.text, 'lxml')
groupa = souped1.find_all('li', class_ = 'EIR5N')
secprice = int(souped1.find_all('li', class_ = '_89yzn').split()[-1])
prodops = []
#{`1` : {'name' : name, pricex' : pricex, 'relatedp' : {'proda' : {'pnamea' : pnamea, 'pcosta' : pcosta},'prodf' : {'pnameb' : pnameb, 'pcostb' : pcostb}}}, ...}

for j, i in groupa :
    proddict[j]['name'] = str(i.find('span', class_ = '_2tW1I').text)
    proddict[j]['pricex'] = int(i.find('span', class_ = '_89yzn').text.split()[-1])
    proddict[j]['relatedp'] = {'proda' : {}, 'prodf' : {}}
print(proddict)

    
