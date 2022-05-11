from concurrent.futures import thread
from traceback import print_tb
import search
from threading import *
from news import gamespot as g_news
import time

the_value = 1
datas = g_news()
current_data = []

# GET USER INPUT IF REDIRECT TO LINK
def doThis():
    the_value = input("Voice input: ")
    print("\nThe value: "+str(the_value)+"\n")

# SETS THE CURRENT DATA INTO A REDIRECTABLE DATA
def getNews():
    for data in datas:
        current_data = data
        print(current_data['link'])
        print()

        time.sleep(0.5)
    
# FIRST CREATED THREAD IS THREAD 1
t1 = Thread(target=getNews)
t1.start()



# THIS IS THE MAIN THREAD BUT NOT THREAD 1
# MAIN THREAD RUNS WHILE THREAD 1 IS STILL RUNNING
while(t1.is_alive()):
    if the_value == 0:
        print("GOTO: "+str(current_data['link']))
        t1.join()
        
    doThis()
    time.sleep(0.5)

# print(search.websearch("what is the best genshin support"))