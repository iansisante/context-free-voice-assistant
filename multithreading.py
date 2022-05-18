from concurrent.futures import thread
import search
from threading import *
from news import gamespot as g_news
import time

the_value = ""
datas = g_news()

# GET USER INPUT IF REDIRECT TO LINK
def voiceRead():    
    print("SAY YES IF WANT TO READ THE LINK!")
    the_value = str(input("Voice input: "))
    return the_value

# SETS THE CURRENT DATA INTO A REDIRECTABLE DATA
def getNews():
    current_data = []

    for data in datas:

        current_data = data
        print(current_data['link'])
        print()

        time.sleep(0.5)
        return

    return current_data
    
# FIRST CREATED THREAD IS THREAD 1
t1 = Thread(target=getNews)
t1.start()


# THIS IS THE MAIN THREAD BUT NOT THREAD 1
# MAIN THREAD RUNS WHILE THREAD 1 IS STILL RUNNING
while(t1.is_alive()):
    
    if voiceRead() == "yes":
        print(current_data)

        

# print(search.websearch("what is the best genshin support"))