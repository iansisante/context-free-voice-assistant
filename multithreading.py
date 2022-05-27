from pyparsing import And
import search
from threading import *
from news import gamespot as g_news
import time

datas = g_news()
print(type(datas))

i = 0
for data in datas:
    print(data,'\n')
    i+=1

    if(i%5==0):
        ask = str(input("\nRead link? (Number or n) "))
        try:
            iAsk = int(ask)

            if(iAsk>0 and iAsk<6):
                print("Selected: ", data,'\n')

        except:
            pass
        
        if(ask == 'n'):
            print("ok boomer")
        