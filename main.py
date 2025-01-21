import requests
from bs4 import BeautifulSoup

def getdata(url):
    r = requests.get(url)

    return r.text


htmldata = getdata("https://weather.com/weather/tenday/l/Tallahassee+FL?canonicalCityId=f7dbdd0b7c2e54f47aa09058fc60f9fce2af5b7d76ffe3487e30d6edd47684bd")

soup = BeautifulSoup(htmldata, 'html.parser')

#print(soup.prettify())

current_temp = soup.find_all("span",  
                             class_="DailyContent--temp--axgOn DailyContent--tempN--DPsDJ") 
chances_rain = soup.find_all("span",  
                             class_= "DetailsTable--value--pWEVz") 
temp = (str(current_temp))
temp_rain = str(chances_rain)

result = "current_temp " + temp[109:111] + " in Tallahassee " + "\n" + "Humidity of " + temp_rain[72:75]
print("Weather update", result)




















