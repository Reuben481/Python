def text_to_stringlist(String):
	list = []
	while len(String) > 0:
		new_word = String[0:String.find(' ')]
		if String.find(' ') ==-1:
			list.append(String)
			break
		list.append(new_word)
		String = String[String.find(' ') + 1: len(String)]
		if len(list)>100:
			break
	return list

print(text_to_stringlist("Hello world my name is nero and im a bot."))
