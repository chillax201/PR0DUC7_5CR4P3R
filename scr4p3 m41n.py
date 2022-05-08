from distutils.filelist import findall
from xml.etree.ElementPath import find
import requests
from bs4 import BeautifulSoup

prod = str(input("product:"))

url1 = "https://www.olx.in/bengaluru_g4058803/q-"+prod+"?isSearchCall=true"
headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
html_T1 = requests.get(url1)
souped1 = BeautifulSoup(html_T1, 'lxml')
