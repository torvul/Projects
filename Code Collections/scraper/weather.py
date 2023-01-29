import requests
import bs4

url = "https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"


r = requests.get(url)

soup = bs4.BeautifulSoup(r.content, 'html.parser')



#print(soup.prettify())


#print(soup.select("div p"))

'''
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
print(tonight.prettify())
'''

# This is the most important thing
'''
newsitem = soup.find(id='news-items')
print(newsitem.prettify())
'''


printtheb = soup.find(id='current-conditions-body')

theb = printtheb.find_all('b')

#print(theb[0].get_text())
print(theb)



print("\n\n\n")


seven = soup.find(id="seven-day-forecast-body")
periodname = seven.find_all(class_="period-name")
print(periodname)




detailed = soup.find(id='detailed-forecast-body')
rows = soup.find_all('b')
print(rows)


