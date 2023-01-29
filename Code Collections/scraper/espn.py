import requests
import bs4

r = requests.get('https://www.espn.com/nfl/standings')
soup = bs4.BeautifulSoup(r.content, 'html.parser')


print(soup.prettify())


card = soup.find(class_='Wrapper Card__Content')


#print(card)


tabletd = soup.find(class_='Table__Colgroup')



tableteam = soup.find_all(class_=['Table__TR Table__TR--sm Table__even','Image Logo Logo__sm', 'hide-mobile'])

for team in list(tableteam):
    print(team)
    print('\n\n')


