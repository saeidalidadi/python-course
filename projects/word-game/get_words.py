import requests
import random
def Words(num=100):
	words_list=[]

	get_words=requests.request("GET", "https://api.datamuse.com/words?ml=ringing+in+the+ears&max="+str(num))
	for i in range(num):
		w = get_words.json()[i]["word"]
		words_list.append(str(w))
	return words_list



def RandWords(Range_words,Word_length,Number_of_words):
	words=Words(Range_words)
	words2=[]
	for i in words:
		if len(i) != Word_length:
			words2.append(i)
	for j in words2:
		words.remove(j)
	del words2
	rand_words=random.sample(words,k=Number_of_words)
	return rand_words

print(RandWords(100,4,5))

