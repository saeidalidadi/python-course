import tkinter as tk

import tkinter as tk
import random

my_list = []
def word_object(window, letter, side, color):
  alphebet1 = list(letter)
  my_list.append(alphebet1)
  return my_list

def drawTable(window, alphebet1, side):  

  """Create an side*side grids
  Args:
    window (TK): an instance of tkinter window
    side (int): the number of rows and columns for grid
  Returns:
    None 
  """ 
  colors = ['#fff','#A3E4D7','#E67E22','#85C1E9','#E74C3C','#8E44AD','#21618C','#5D6D7E','#BDC3C7','#922B21','#F7DC6F','#27AE60','#2E86C1','#2E86C1']
  i = 0
  for row in range(side):
    color = random.choice(colors)
    for col in range(side):   
      if(alphebet1[i] and i<len(alphebet1)-1 ) :
        letter_container = tk.Frame(master=window, relief=tk.RIDGE,  borderwidth=1, background=color,command=ree("Hi"))
        letter_container.grid(row=row, column=col)
        label = tk.Label(master=letter_container, text= alphebet1[row][col]) 
        label.pack(padx=10, pady=10) 
       
      

def ree(hi):
  a = 3
