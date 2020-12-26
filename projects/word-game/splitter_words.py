import Words_file

def splitter(main_words):
	words_list=[]
	for word in main_words:
		convert_to_list = list(word)
		words_list.append(convert_to_list)
	return words_list

##########test##########
print (splitter(Words_file.RandWords(4)))
##########test##########
