from bs4 import BeautifulSoup as bs
from more_itertools import first
import requests

google = "https://www.google.com/search?q="

def get_temperature(location):
    
    r = requests.get(google+location+"temperature next week")
    data = bs(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    return temp

temptemp = get_temperature("naic temperature")
print(temptemp)