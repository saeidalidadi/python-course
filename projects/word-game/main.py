import tkinter as tk
import table_view as tw

window = tk.Tk()
window.title("word game")
window.geometry("500x500")

letterSequence = [
    ["a","b","c","d","e"],
    ["f","g","h","i","n"],
    ["x","z","h","v","n"],
    ["t","g","h","m","n"],
    ["x","b","h","v","k"]
]

tw.drawTable(window, 5, letterSequence)

window.mainloop()