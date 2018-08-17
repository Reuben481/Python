from text_to_stringlist import text_to_stringlist
import numpy as np

def fileParser(String):
	stringlist = text_to_stringlist(String)
	nouns_in_String = []
	verbs_in_string = []
	for word in stringlist:
		if is_noun(word):
			nouns_in_String.append(word)
		if is_verb(word):
			verbs_in_string.append(word)
	return nouns_in_String, verbs_in_string

def is_noun(subString):
	wlf = open("nouns.txt")
	for line in wlf:
		word = line.strip()
		if subString == word:
			return True

def is_verb(subString):
	wlf = open("verbs.txt")
	for line in wlf:
		word = line.strip()
		if subString == word:
			return True

#print(text_to_stringlist("Hello world i am a bat. I am not a ball. You are a banana."))
#print(fileParser("Hello world i am a bat. I am not a ball. You are a banana."))

text = """Once upon a time there lived a lion in a forest. One day after a heavy meal. It was sleeping under a tree.
After a while, there came a mouse and it started to play on the lion. 
Suddenly the lion got up with anger and looked for those who disturbed its nice sleep.
 Then it saw a small mouse standing trembling with fear. The lion jumped on it and started to kill it. 
 The mouse requested the lion to forgive it. The lion felt pity and left it. The mouse ran away.
 On another day, the lion was caught in a net by a hunter. The mouse came there and cut the net. 
 Thus it escaped. There after, the mouse and the lion became friends. They lived happily in the forest afterwards."""
print(fileParser(text))
print(text_to_stringlist(text))