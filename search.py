from bs4 import BeautifulSoup as bs
from more_itertools import first
import requests
import webbrowser

google = "https://www.google.com/search?q="

def websearch(search):
    
    surl = google+search    
    webbrowser.get().open(surl)