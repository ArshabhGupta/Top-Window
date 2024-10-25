from tkinter import *

root = Tk()
root.geometry("200x100")
root.title("Main Window")

def TopWin():
    top = Toplevel()
    top.geometry("100x50")
    top.title("Top Window")
    l2 = Label(top, text = "This is the top level window")
    l2.pack()
    top.mainloop()

l = Label(root, text = "This is the root window")
btn = Button(root, text = "Click here to open another window", command = TopWin)

l.pack()
btn.pack()
root.mainloop()