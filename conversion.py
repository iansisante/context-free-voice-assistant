from playsound import playsound
import speech_recognition as sr
from gtts import gTTS
import os

# Capture Voice
# takes command through microphone
def speech_conversion():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("listening.....")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing.....")
		query = r.recognize_google(audio, language='en-in')
		# print(f"user said \n {query}\n")
		return query
	except Exception as e:
		print("say that again please.....")
		return "None"
	return query


def text_conversion(text):
	speak = gTTS(text=text, lang='en', slow=False)

	speak.save("captured_voice.mp3")
	playsound('captured_voice.mp3')
	os.remove('captured_voice.mp3')
