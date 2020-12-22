import random

def RandWords(Word_length,Number_of_words):
	File = open("words.txt", "r")
	words = File.read().split()
	File.close()

	words2=[]
	for i in words:
		if len(i) != Word_length:
			words2.append(i)
	for j in words2:
		words.remove(j)
	del words2
	rand_words=random.sample(words,k=Number_of_words)
	return rand_words

print(RandWords(4,3))