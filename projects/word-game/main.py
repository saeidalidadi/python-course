import tkinter as tk
import table_view as tw

window = tk.Tk()
window.title("word game")
window.geometry("500x500")
tw.drawTable(window, 6)

window.mainloop()