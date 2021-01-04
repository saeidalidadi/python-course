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

def wordToLetters(main_words):

  letters_sequence = []
  words_len = len(main_words)
  row_sequence = ["*"] * words_len
  for word in main_words:
    word_letters = list(word)
    word_letters = [
        word_letters[i] if len(word_letters) > i else item for i,item in enumerate(row_sequence)
      ]
    
    letters_sequence.append(word_letters)
  return letters_sequence