from ast import Index
from distutils.filelist import findall
from email import header
from xml.etree.ElementPath import find
import requests
from bs4 import BeautifulSoup

prod = str(input("product:"))

def getsite(b4,prod,aft3r) :
    url = b4+prod+aft3r
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

olxvar = getsite("https://www.olx.in/bengaluru_g4058803/q-",prod,"?isSearchCall=true")
