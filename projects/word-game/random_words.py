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

def set_word_in_array(arr, dencity): 
  lines = []  
  matrix = [[None for c in range(dencity)] for r in range(dencity)]

  current_position = 0 

  for line in arr:   
    for char in line:  
        lines.append(char) 
   
  if(lines) :
    wordArray = list(lines) 
    for i in range(dencity): 
      for j in range(dencity): 
        if(current_position < len(wordArray)):
          matrix[i][j] = wordArray[current_position]
          current_position += 1 
        else:
          matrix[i][j] = 'A' 
 
  return matrix