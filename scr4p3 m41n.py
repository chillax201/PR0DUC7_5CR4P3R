from distutils.filelist import findall
from email import header
from xml.etree.ElementPath import find
import requests
from bs4 import BeautifulSoup

#this function chceks for the most relevant string from the list provided as `stra` to `strab`
def check_rel(stra,strab):
    refl = ['', 0, 0]
    y = 0
    for i in stra:
        rel = 0
        for x in strab.split(' ') :
            if i.find(x) != -1 :
                rel = rel + 1
        if refl[1] < rel :
            refl[2] = y
            refl[1] = rel
            refl[0] = i
        y += 1
    print(refl)
    return refl[2]

#set of inits 
prod = str(input("product:"))
prodals = {}
proddict = {}
prodops = []

#soupdata from the second hand sales website
url1 = "https://www.olx.in/bengaluru_g4058803/q-"+prod+"?isSearchCall=true"
headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
html_T1 = requests.get(url1, headers=headers)
souped1 = BeautifulSoup(html_T1.text, 'lxml')
groupa = souped1.find_all('li', class_ = 'EIR5N')


# data structure prototype : {`1` : {'name' : name, 'pricex' : pricex, 'relatedp' : {'proda' : {'pnamea' : pnamea, 'pcosta' : pcosta},'prodf' : {'pnameb' : pnameb, 'pcostb' : pcostb}}}, ...}

#price and name data from second hand sales website
i=0
for j in groupa :
    if j.find('span', class_ = '_89yzn') :
        proddict[i] = {'name':'','pricex': 0, 'relatedp' : {'proda' : {'pnamea' : '','pcosta' : 0}, 'prodf' : {'pnameb' : '','pcostb' : 0}}}
        proddict[i]['name'] = str(j.find('span', class_ = '_2tW1I').text)
        proddict[i]['pricex'] = int(j.find('span', class_ = '_89yzn').text.split(' ')[-1].replace(",",""))
        i += 1
print(proddict)

#most relevant first hand price and name data for each product
for i in proddict :
    n = proddict[i]['name']
    url2e = "https://www.amazon.in/s?k="+n+"&crid=LPWOCPEFVKNR&sprefix=gp%2Caps%2C379&ref=nb_sb_noss_2"
    url2 = url2e.replace(' ','+')
    html_T2 = requests.get(url2, headers=headers)
    souped2 = BeautifulSoup(html_T2.text, 'lxml')
    groupb = souped2.find_all('div', class_ = "s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16")
    k = 0
    prodals[i] = {'ls' : [], }
    for j in groupb:
        if j.find('span', class_ = 'a-price-whole'):
            prodals[i]['ls'].append(str(j.find('span', class_ = "a-size-medium a-color-base a-text-normal").text))
            prodals[i][k] = int(j.find('span', class_ = 'a-price-whole').text.replace(",","").replace(".",""))
            k += 1
    print(prodals)
    x = check_rel(prodals[i]['ls'], n)
    proddict[i]['relatedp']['proda']['pnamea'] = prodals[i]['ls'][x]
    proddict[i]['relatedp']['proda']['pcosta'] = prodals[i][x]
print(prodals)
print(proddict)
#same method will be applied for proddict[i]['relatedp']['prodf']
for j, i in groupa :
    proddict[j]['name'] = str(i.find('span', class_ = '_2tW1I').text)
    proddict[j]['relatedp'] = {'proda' : {}, 'prodf' : {}}
print(proddict)
