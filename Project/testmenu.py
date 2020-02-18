from tkinter import *

def start() :
    Label(root, text='How many place you want to go ?? ').pack()
    Button(root, text="1").pack()
    Button(root, text="2").pack()
    Button(root, text="3").pack()

root = Tk()
root.title('---| Project Thai Map |---')
Label(root ,text = "Welcome To Count Map").pack()
Button(root, text='start', command=start()).pack()
root.mainloop()