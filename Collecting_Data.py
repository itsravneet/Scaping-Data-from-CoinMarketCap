from bs4 import BeautifulSoup
import sys
sys.path.append("/Library/Python/2.7/site-packages")
from selenium import webdriver
import requests 
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time 

#collecting top 20 names of coins
url="https://coinmarketcap.com/coins/"
driver = webdriver.Chrome('chromedriver')
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html,'lxml')
table_data=soup.find("table",class_="h7vnx2-2 czTsgW cmc-table")
#storing headers
headers = []
for i in table_data.find_all('th'):
  title = i.text.strip()
  headers.append(title)
#storing links to different coins
links=[]
z=0
for j in table_data.find_all('tr'):
  if(z==21):
    break
  else:
    z+=1
  row_data = j.find_all('td')
  row=[]
  for j in row_data:
    try:
      k=j.find('a', href=True)
      row=k.get('href')
      break
    except:
      pass
  links.append(row)
links=links[1:]




#collecting market value of coins
rows=[]
headers=[]
for link in links:
  url='https://coinmarketcap.com'+link+'markets/'
  print(url)
  driver.get(url)
  time.sleep(5)
  driver.execute_script("window.scrollTo(0, 6000)")
  time.sleep(3) 
  html = driver.page_source
  soup = BeautifulSoup(html,'lxml')
  table_data=soup.find("table",class_="h7vnx2-2 ecUULi cmc-table")
  #storing headers
  headers = []
  for i in table_data.find_all('th'):
    title = i.text.strip()
    headers.append(title)
  #storing rows values
  

  for j in table_data.find_all('tr'):
    row_data = j.find_all('td')
    row=[]
    for j in row_data:
      if(j.text!=None):
        row.append(j.text)
    if(row!=[]):
      rows.append(row)
  rows=rows[1:]
  print(rows)


#Adding rows,Columns and renaming columns
df=pd.DataFrame(rows)
df.columns=headers
df=df.rename(columns={"Pairs": "Symbol", "Source": "Exchange"})
df.drop(['#'],axis=1,inplace=True)
print(df)



#converting string values to float like price
col=['Price','+2% Depth','-2% Depth','Volume' ,'Volume %','Liquidity']
for i in col:
  temp=[]
  a=df[i]
  for j in a:
    try:
      j=j.replace(',','')
    except:
      pass
    try:
      j=j.replace('$','')
    except:
      pass
    try:
      j=j.replace("%",'')
    except:
      pass
    try:
      j=float(j)
    except:
      pass
    temp.append(j)
  df[i]=temp


#Adding new columns base and quoteas per question
base=[]
for i in df.Symbol:
  try:
    base.append(i.split('/')[0])
  except:
    base.append("-")
quote=[]
for i in df.Symbol:
  try:
    quote.append(i.split('/')[1])
  except:
    quote.append('-')
df['Base']=base
df['Quote']=quote

print(df)

#saving the dataframe
df.to_csv("data.csv",index=False)
