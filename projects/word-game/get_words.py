import requests
import random
def Words(num=100):
 	words_list=[]

	get_words=requests.request("GET", "https://api.datamuse.com/words?ml=ringing+in+the+ears&max="+str(num))
	for i in range(num):
		print('\n')
		w = get_words.json()[i]["word"]
		words_list.append(str(w))
	return words_list



def RandWords(num1,num2,num3):
	words=Words(num1)
	words2=[]
	for i in words:
		if len(i) != num2:
			words2.append(i)
	for j in words2:
		words.remove(j)
	del words2
	rand_words=random.sample(words,k=num3)
	return rand_words

print(RandWords(100,4,5))

