import random
import os

def readRandomWords(number_of_words):
  file_dir = os.path.dirname(os.path.realpath(__file__))
  print(file_dir)
  file = open(file_dir + "/words.txt", "r")
  words = file.read().split()
  file.close()
  rand_words=random.sample(words,k=number_of_words)
  return rand_words

