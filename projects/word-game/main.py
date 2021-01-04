import tkinter as tk
import table_view as tw
import words as wd

window = tk.Tk()
window.title("word game")
window.geometry("500x500")

word_list = wd.readRandomWords(10)
letters_sequence = wd.wordToLetters(word_list)
tw.drawTable(window, letters_sequence)

window.mainloop()