# if you wanna scrape a website
# 1. use API
# 2. HTML web scraping using some  tool like bs4


# install all the requirements

# pip install requests
# pip install bs4
# pip install html4lib

import requests
from bs4 import BeautifulSoup
url = "https://www.espncricinfo.com/cricketers/sam-curran-662973"

# 1. get the html 
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)
# 2. parse the html 
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

# 3. html tree traversal
# 
# commonly used types of objects:
# print(type(title))                1. tag
#  print(type(title.string))     2. navigableString
# 3.print(type(soup))            3.BeautifulSoup
# 4.comment 


# get the title of html page 

title = soup.title
 
# get all the paragraphs from the  page 
paras = soup.find_all('p')
# print(paras)


# print(anchors)

# get first element of the html page

print(soup.find('p')) 

# get classes of the any element in the html page
print(soup.find('p')['class']) #class of the first paragraph

# find all the elements of the class lead 
print(soup.find_all('p', class_='lead'))

# get the all texts from the tags/soup
print(soup.find('p').get_text())

# gete all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
# get all the links on the page
for link in anchors: 
    if (link.get('href') !="#"):
        linkText ="https://www.espncricinfo.com/cricketers/sam-curran-662973"+ link.get('href')
        all_links.add(link)
        print(linkText)

        