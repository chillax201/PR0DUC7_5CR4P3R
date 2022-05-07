from distutils.filelist import findall
from xml.etree.ElementPath import find
import requests
from bs4 import BeautifulSoup

prod = str(input("product:"))

url1 = "https://olx.in/"+prod
headers = {'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
soup1 = ''