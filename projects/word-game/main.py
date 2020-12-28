import tkinter as tk
import table_view as tw
import random_word as wo
import random

window = tk.Tk()
window.title("word game")
window.geometry("500x500")
dencity = 5

allLetter = wo.word_object()
letterArray = wo.set_word_in_array(allLetter, dencity)

tw.drawTable(window, letterArray, dencity)
 
 

window.mainloop()

 