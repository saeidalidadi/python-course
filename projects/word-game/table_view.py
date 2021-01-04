import tkinter as tk

def drawTable(window, letters_sequence):
  """Create an side*side grids with letters.
  Args:
    window (TK): an instance of tkinter window
  Returns:
    None 
  """
  side_len = len(letters_sequence)
  for row in range(side_len):
    for col in range(side_len):
      letter_container = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=1)
      letter_container.grid(row=row, column=col)
      label = tk.Label(master=letter_container, text=letters_sequence[row][col])
      label.pack(padx=10, pady=10)