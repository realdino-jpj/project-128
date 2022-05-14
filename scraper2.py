from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
import requests

dwarf_stars_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome("chromedriver.exe")

page = requests.get(dwarf_stars_url)
print(page)

soup = BeautifulSoup(page.text,"html.parser")
star_table = soup.find_all('table')
table_rows = star_table[7].find_all('tr')

temp_lists = []

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_lists.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]

for i in range(1,len(temp_lists)):
    Star_names.append(temp_lists[i][1])
    Distance.append(temp_lists[i][3])
    Mass.append(temp_lists[i][5])
    Radius.append(temp_lists[i][6])
    
df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])
print(df2)

df2.to_csv('dwarf_stars.csv')