import tkinter as tk

import tkinter as tk
import random 

alphebet = [
    ["a","b","c","d","e","y"],
    ["f","g","h","i","n","k"],
    ["x","z","h","v","n","k"],
    ["t","g","h","m","n","k"],
    ["x","b","h","v","k","k"]
    ]
colors = ["#FFFEEE","#FFF" ]

def drawTable(window, side):
  """Create an side*side grids
  Args:
    window (TK): an instance of tkinter window
    side   (int): the number of rows and columns for grid
  Returns:
    None 
  """
  for row in range(side):
    for col in range(side): 
    #   print(alphebet[row][col]);
      letter_container = tk.Frame(master=window, relief=tk.RIDGE,  borderwidth=1, background=random.choice(colors),command=ree("Hi"))
      letter_container.grid(row=row, column=col)
      label = tk.Label(master=letter_container, text=random.choice(alphebet[row][col]))
      label.pack(padx=10, pady=10) 

def ree(hi):
  a = 3