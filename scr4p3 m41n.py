from distutils.filelist import findall
from email import header
from xml.etree.ElementPath import find
import requests
from bs4 import BeautifulSoup

prod = str(input("product:"))

url1 = "https://www.olx.in/bengaluru_g4058803/q-"+prod+"?isSearchCall=true"
headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
html_T1 = requests.get(url1, headers=headers)
souped1 = BeautifulSoup(html_T1.text, 'lxml')
groupa = souped1.find_all('li', class_ = 'EIR5N')
secprice = int(souped1.find_all('li', class_ = '_89yzn').split()[-1])
prodops = []

for i in groupa :
    prodops.append(str(i.find('span', class_ = '_2tW1I').text))
print(prodops)

for i in prodops :
    url2e = "https://www.amazon.in/s?k="+i+"&crid=LPWOCPEFVKNR&sprefix=gp%2Caps%2C379&ref=nb_sb_noss_2"
    url2 = url2e.replace(' ','+')
    html_T2 = requests.get(url2, headers=headers)
    souped2 = BeautifulSoup(html_T2.text, 'lxml')
    