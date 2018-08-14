from text_to_stringlist import text_to_stringlist
import numpy as np

def fileParser(String):
	stringlist = text_to_stringlist(String)
	nouns_in_String = []
	for word in stringlist:
		if is_noun(word):
			nouns_in_String.append(word)
	return nouns_in_String

def is_noun(subString):
	wlf = open("nouns.txt")
	for line in wlf:
		word = line.strip()
		if subString == word:
			return True


print(text_to_stringlist("Hello world i am a bat. I am not a ball. You are a banana."))
print(fileParser("Hello world i am a bat. I am not a ball. You are a banana."))

