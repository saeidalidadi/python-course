import tkinter as tk

def drawTable(window, side, letterSequence):
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
      letter_container = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=1)
      letter_container.grid(row=row, column=col)
      label = tk.Label(master=letter_container, text=letterSequence[row][col])
      label.pack(padx=10, pady=10)

