import tkinter as tk

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
      letter_container = tk.Frame(master=window, relief=tk.RIDGE,  borderwidth=2)
      letter_container.grid(row=row, column=col)
      label = tk.Label(master=letter_container, text="A")
      label.pack(padx=8, pady=6)