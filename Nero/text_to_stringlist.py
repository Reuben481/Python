def text_to_stringlist(String):
	list = []
	while len(String) > 0:
		new_word = String[0:String.find(' ')]
		if String.find(' ') ==-1:
			list.append(String[0:len(String)-1])
			break
		if new_word.find(".")==-1:
			list.append(new_word)
		else:
			list.append(new_word[0:len(new_word)-1])
		String = String[String.find(' ') + 1: len(String)]
	return list

#print(text_to_stringlist("Hello world i am a bat. I am not a ball. You are a banana."))
