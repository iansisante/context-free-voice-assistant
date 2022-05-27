
import search
import conversion as conv

query = conv.speech_conversion()
while (query == "None"):
	query = conv.speech_conversion()

print(search.websearch(query))

conv.text_conversion("these are the results")