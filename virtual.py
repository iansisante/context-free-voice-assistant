import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import webbrowser
import os
import smtplib
import cfg


print("Initializing Sakura")
MASTER = "User"

contacts = {
    "matthew" : "matthewperrybustarde@gmail.com",
    "kyle" : "kylechristianodecastro@gmail.com",
    "ian" : "ian.sisante@tup.edu.ph"
}

links = {
    "google" : "https://www.google.com/search?q=",
    "youtube" : "https://www.youtube.com/results?search_query=",
    "wikipedia" : "https://en.wikipedia.org/wiki/"
}

apps = {
    "spotify" : "C:\\Program Files\\WindowsApps\\SpotifyAB.SpotifyMusic_1.188.612.0_x86__zpdnekdrzrea0\\Spotify.exe",
    "discord" : "C:\\Users\\Matthew\\AppData\\Local\\Discord\\app-1.0.9005\\Discord.exe",
    "genshin" : "C:\\Program Files\\Genshin Impact\\Genshin Impact game\\GenshinImpact.exe"
}


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
#Speak function will speak/Pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

#This funtion will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    # print(hour)

    if hour>=0 and hour <12:
        speak("good morning" + MASTER)

    elif hour>=12 and hour<18:
        speak("good afternoon" + MASTER)

    else:
        speak("good Evening" + MASTER)

    # speak("i am your assistant. How may I help you?")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('sakura.assistant@gmail.com', 'xayvbzptpwbfmaab')
    server.sendmail("matthewperrybustarde@gmail.com", to, content)
    server.close()

    

#This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try :
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        query = None

    return query

#main program starting
def main():
    speak("Initializing Sakura...")
    wishMe()
    query = takeCommand()
    cfg.cfg_checker(query)

    #Logic for executing tasks as per the query
    if 'search' in query.lower():
        #webbrowser.open('youtube.com')
        url = "https://en.wikipedia.org/wiki/"
        speak("what do you want to search? ")
        query = takeCommand()
        surl = url+query    
        webbrowser.get().open(surl)
        
    elif 'check code' in query.lower():
        print(contacts["matthew"])
        splitter = takeCommand()
        print(splitter.split(" ")[-1])

    elif 'check time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"{MASTER} the time is {strTime}")

    elif 'launch' or 'start' or 'open' in query.lower():
        application = query.split(" ")[-1]
        os.startfile(apps[application])
    
    elif 'send email' in query.lower():
        try:
            name = query.split(" ")[-1]
            speak("what should i send")
            content = takeCommand()
            to = contacts[name]
            sendEmail(to, content)
            speak("Email has been sent to matt")
        except Exception as e:
            print(e)
main()