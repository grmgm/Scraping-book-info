# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup
URL='http://books.toscrape.com/'
data1 = []    
# 1. 
res=requests.get(URL)

# 2. 
html=res.text

# 3. 
soup=BeautifulSoup(html, 'html.parser')

# 4. 
items=soup.find('ul', class_='nav').find('ul').find_all('li')

# 5. 

for item in items:
    titl=item.text.strip()
    data1.append(titl)
    #print(titl)

df= pd.DataFrame(data1,columns=['Theme'])
df.to_csv('theme.csv')     


#%% 
import requests
from bs4 import BeautifulSoup

baseurl = 'http://books.toscrape.com/catalogue/category/books_1/page-'
datalist = []    

for i in range(0,50):       
    
    url = baseurl + str(i+1) + '.html'
    
    # 1. 
    res=requests.get(url)
    
    # 2. 
    html=res.text
    
    # 3. 
    soup=BeautifulSoup(html, 'html.parser')
    
    # 4.
    #items=soup.find('ul', class_='nav').find('ul').find_all('li')
    x1=soup.find_all(class_='product_pod')
    
    for item in x1:
        data2 = []
        book_name=item.find('h3').find('a')
        data2.append(book_name['title'])
        book_rating=item.find('p')
        data2.append(book_rating['class'][1])        
        book_price=item.find('div', class_='product_price').find('p', class_='price_color')
        price=book_price.text.strip()
        price = price.replace('Â£','')
        data2.append(price)
        #print('Title:'+book_name['title']+'\n','Price:'+book_price.text.strip()+'\n',book_rating['class'])     
        
        datalist.append(data2) 
        
df= pd.DataFrame(datalist,columns=['Title','Rating','Price(Pound )'])
df.to_csv('title.csv')     
    