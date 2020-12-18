import tkinter as tk
import random
alphebet =[
  ["a","b","c","d","e","f"],
  ["g","h","i","j","k","l"],
  ["o","m","n","p","q","r"],
  ["s","t","u","w","x","y"],
  ["z","f","b","n","h","r"],
  ["w","f","k","l","q","z"],
  ]
def drawTable(window, side):
  """Create an side*side grids
  Args: commit
    window (TK): an instance of tkinter window
    side   (int): the number of rows and columns for grid
  Returns:
    None 
  """
  for row in range(side):
    for col in range(side):
      letter_container = tk.Frame(master=window, relief=tk.RIDGE,  borderwidth=6)
      letter_container.grid(row=row, column=col)
      label = tk.Label(master=letter_container, text=alphebet[row][col])
      label.pack(padx=14, pady=13)