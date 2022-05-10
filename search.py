import webbrowser

google = "https://www.google.com/search?q="

def websearch(search):
    surl = google+search    
    webbrowser.get().open(surl)