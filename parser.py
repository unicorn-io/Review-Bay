from bs4 import BeautifulSoup as bs 
import urllib.request
import re


target-url='https://fms.nrsc.gov.in/fmsexternal/newuserh.php'

##to connect to the website
try:
    page = urllib.request.urlopen(target_url)
except Exception as e:
    print(e)

###add functionality for php also ...currently working for html only 
soup = bs(page,'html.parser')
print(soup)

## using regex to find label 

regex =re.compile('^pwd')
content_lbl = soup.find_all('label',attrs={'class':regex})
print(content_lbl)

## toget data from the font part
font_part =soup.find_all('font',attrs={'class':regex})
font_part_soup = font_part.fins_all('font')
print(font_part_soup)


## creating a file and writing into it as a .json file and can be converted into .csv

with open('content.json','w') as f:
    for i in content:
        f.write(i+"\n")
        




