from ast import Index
from distutils.filelist import findall
from email import header
from xml.etree.ElementPath import find
import requests
from bs4 import BeautifulSoup

prod = str(input("product:"))

def getsite(b4,prod,aft3r) :
    url = b4 + prod.replace(' ','+') + aft3r
    headers = {'user-agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
    html_T1 = requests.get(url, headers=headers)
    return BeautifulSoup(html_T1.text, 'lxml')

def checkrel(strlist,str2find) :
    inca = 0
    rel = ""
    for i in strlist :
        incb = 0
        for j in str2find.split(" ") :
            if i.find(j):   
                incb += 1
        if incb > inca :
            inca = incb
            rel = i
    return rel

olxligroup = getsite("https://www.olx.in/bengaluru_g4058803/q-",prod,"?isSearchCall=true").find_all('li', class_ = 'EIR5N')

iter0 = 0
for li in olxligroup :
    proddict = {}
    if li.find('span', class_ = '_89yzn') :
        proddict[iter0] = {'name':str(li.find('span', class_ = '_2tW1I').text),'pricex': int(li.find('span', class_ = '_89yzn').text.split(' ')[-1].replace(",","")), 'relatedp' : {'proda' : {'pnamea' : '','pcosta' : 0}, 'prodf' : {'pnameb' : '','pcostb' : 0}}}
        iter0 += 1
print(proddict)
print('*'*20)

amazonprodls = {}
for prodn in proddict :
    amazonhtml = getsite("https://www.amazon.in/s?k=",proddict[int(prodn)]['name'],"&crid=LPWOCPEFVKNR&sprefix=gp%2Caps%2C379&ref=nb_sb_noss_2")
    amazondivlist = amazonhtml.find_all('div', class_ = "s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16")
    for amazprod in amazondivlist :
        if amazprod.find('span', class_ = 'a-price-whole'):
            amazonprodls[prodn] = {(str(amazprod.find('span', class_ = "a-size-medium a-color-base a-text-normal").text)) : int(amazprod.find('span', class_ = 'a-price-whole').text.replace(",","").replace(".",""))}
    print('*'*20)
    relprod = checkrel(amazonprodls[prodn],proddict[prodn]['name'])
    proddict[prodn]['relatedp']['proda']['pnamea'] = relprod
    proddict[prodn]['relatedp']['proda']['pcosta'] = amazonprodls[prodn][relprod]

print('*'*20)
print(amazonprodls)

print("**********************************************************************************************************************************************************************")
print("**********************************************************************************************************************************************************************")
print(proddict)
print("**********************************************************************************************************************************************************************")
print("**********************************************************************************************************************************************************************")

print("remember to chillax!")
