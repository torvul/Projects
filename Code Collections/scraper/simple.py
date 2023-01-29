import requests
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
page


#print(page)


from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')


pretty = soup.prettify()

#print(list(soup.children))

# https://www.dataquest.io/blog/web-scraping-python-using-beautiful-soup/
# This explains the three type: look for 'The first is a Docttyp'
#print([type(item) for item in list(soup.children)])



#My most important one is [2]

html = list(soup.children)[2]

body = list(html.children)[3]

p = list(body.children)[1]






# searching for tags by class and id

page = requests.get("https://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')


#print(soup.prettify())

print(soup.find_all('p', class_='outer-text'))
print("\n\n")




