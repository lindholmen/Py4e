
from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("500x450")
btn = Button(root, text = "click me by tkinter")
btn2 = ttk.Button(root, text = "click me by ttk")
btn.pack()
btn2.pack()

root.mainloop()
