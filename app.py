from random import randint
import tkinter as tk
import threading

root = tk.Tk()

def tread():
    threading.Timer(5.0, tread).start()
    arr = [randint(1,100)]
    label = tk.Label(root, text=arr)
    label.pack()
     
tread()
root.mainloop()   


