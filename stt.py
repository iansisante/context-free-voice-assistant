from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import os

# Capture Voice
# takes command through microphone
def takecommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("listening.....")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing.....")
		query = r.recognize_google(audio, language='en-in')
		print(f"user said \n {query}\n")
		return query
	except Exception as e:
		print("say that again please.....")
		return "None"
	return query

# Taking voice input from the user
# query returns the string output
query = takecommand()
while (query == "None"):
	query = takecommand()


