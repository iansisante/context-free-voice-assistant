from bs4 import BeautifulSoup as bs
from numpy import piecewise
import requests

# DEFAULT URL
url = "https://www.google.com/search?q="

def gamespot():

    try:
        # GET DATA FROM GAMESPOT
        url = "https://www.gamespot.com/news"
        result = requests.get(url)
        doc = bs(result.text, "html.parser")

        # FIND ALL TITLES
        news = doc.find_all("h4", attrs={"class": "card-item__title"})

        # INITIATION FOR SAVING WEBSCRAPED DATA
        newsOut = []

        # SAVE ALL WEBSCRAPED DATA INTO DICT
        for n in news:

            nDate = str(n.parent.next_sibling.time["datetime"]).split(" ")
            newsOut.append({
                "link": "https://www.gamespot.com" + n.parent["href"],
                "text": n.text,
                "date": nDate[1]+" "+nDate[2]+" "+nDate[3]
            })
            #susume = input("Next? y/n: ")
        return newsOut

    # CATCHES UNEXPECTED EXCEPTIONS
    except Exception as e:
        return "Something occured! Exception name: " + str(e)

