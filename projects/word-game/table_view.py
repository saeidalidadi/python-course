import tkinter as tk
 
def create_event_starter(t):  
  
  def key_press(e):  
   print('Enter at x = % d, y = % d, t = % s'%(e.x, e.y,t))
  
  return key_press

def create_event_dispatcher(t):  
  
  def event(e):  
   print('Enter at x = % d, y = % d, t = % s'%(e.x, e.y,t))
  
  return event
 
def create_event_terminate(t):  
  
  def on_leave(e):  
     print('You on_leave x = % d, y = % d, t = % s'%(e.x, e.y,t))
  
  return on_leave
  

def drawTable(window, letters_sequence):
  """Create an side*side grids with letters.
  Args:
    window (TK): an instance of tkinter window
  Returns:
    None 
  """
  startButton = tk.Button(window, text="Start", bg="green", height="2",width="10", fg="#FFF")
  startButton.place(x=400, y=75) 
  quitButton = tk.Button(window, text="Quit", bg="red", height="2",width="10", fg="#FFF")
  quitButton.place(x=550, y=75)
  tkLabel = tk.Label(window, text="Words", bg="#fff", height="2",width="30", fg="#aaa")
  tkLabel.place(x=400, y=150)
  side_len = len(letters_sequence)
  for row in range(side_len):
    for col in range(side_len): 
      letter_container = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=1,bg ="#F1F0e1" ) 
      letter_container.grid(row=row, column=col)
      label = tk.Label(master=letter_container, text=letters_sequence[row][col]) 
      letter_container.bind("<Button-1>", create_event_starter(letters_sequence[row][col]))
      letter_container.bind("<Enter>", create_event_dispatcher(letters_sequence[row][col]))
      letter_container.bind("<Leave>", create_event_terminate(letters_sequence[row][col]))
      label.pack(padx=10, pady=10) 
      

