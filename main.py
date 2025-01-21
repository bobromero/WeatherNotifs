import requests
from bs4 import BeautifulSoup

def getdata(url):
    r = requests.get(url)

    return r.text


htmldata = getdata("https://weather.com/weather/today/l/Tallahassee+FL?canonicalCityId=f7dbdd0b7c2e54f47aa09058fc60f9fce2af5b7d76ffe3487e30d6edd47684bd")

soup = BeautifulSoup(htmldata, 'html.parser')


current_temp = soup.find_all("span",  
                             class_="CurrentConditions--tempValue--zUBSz") 
temp = (str(current_temp))

result = "\nCurrent Temp " + temp[92:94]+ " in Tallahassee"
print("Weather update", result)




















