#package:collections of classes and methods
from translate import Translator #package imported
to=Translator(to_lang="Marathi") #created translator
line=input("Enter line to translate:") #read
line_translated=to.translate(line) #translate
print("Translated line is:",line_translated) #print

from translate import Translator #package imported
line=input("Enter line to translate:") #read
lang=[
    "Hindi", #hi
    "Marathi", #mr
    "Tamil", #ta
    "Telugu", #te
    "Kannada", #kn
    "Gujarati", #gu
    "Malayalam", #ml
    "Bengali", #bn
    "Assamese", #as
]
for language in lang:
    to = Translator(to_lang=language) #created Translator
    line_translated = to.translate(line) #translate
    print("Language is:", language,"\tLine is", line_translated)
