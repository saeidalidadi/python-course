import random

def RandWords(Number_of_words):
	File = open("words.txt", "r")
	words = File.read().split()
	File.close()
	rand_words=random.sample(words,k=Number_of_words)
	return rand_words

print(RandWords(3))
