from nltk import pos_tag
from nltk import RegexpParser
from nltk.stem import WordNetLemmatizer
import nltk

lemmatizer = WordNetLemmatizer()

rules = {

    # TERMINALS
    "s": [
        ["skr", "vb"],
        ["skr", "vb", "app"],
        ["skr", "vb", ""]
    ],
    "rq": [
        ["", ""]
    ],

    # NON TERMINALS 
    "vb" : [
        ["pls","open"],
        ["search"],
        ["check"]
    ],
    "app" : [
        ["discord"],
        ["browser"]
    ],

    "skr": "sakura",
    "discord":"",
    "browser":"",
    
}


# text ="learn php from guru99 and make study easy".split()
# print("\n\nAfter Split:",text)
# tokens_tag = pos_tag(text)
# 
# print("\n\nAfter Token:",tokens_tag)
# patterns= """mychunk:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}"""
# chunker = RegexpParser(patterns)
# 
# print("\n\nAfter Regex:",chunker)
# output = chunker.parse(tokens_tag)
# 
# print("\n\nAfter Chunking",output)

my_str = "sakura open discord"

cmd = my_str.split()
print("\n\nSplitted command: ",cmd)
# print("\nLemmatized str: ",lemmatizer.lemmatize(my_str))
print("\nPos tag: ", pos_tag({"my"}))
print()