from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import os
root = Tk()
root.title("Mini Notepad")
root.minsize(650,650)
root.maxsize(650,650)
o = ImageTk.PhotoImage(Image.open("open.png"))
s = ImageTk.PhotoImage(Image.open("save.png"))
c = ImageTk.PhotoImage(Image.open("exit.jpg"))

e1 = Entry(root)
e1.place(relx=0.66, rely= 0.03, anchor= CENTER)

t1 = Text(root, height= 35, width= 80)
t1.place(relx=0.5, rely= 0.55, anchor= CENTER)

l1 = Label(root, text= "File Name")
l1.place(relx=0.48, rely= 0.03, anchor= CENTER)
 
fn=""


def op():
   global fn
   t1.delete(1.0, END)
   e1.delete(0, END)
   fp= filedialog.askopenfilename(title="Space", filetypes=(("Text files ", "*.txt"),))
   fn = os.path.basename(fp)
   name = fn.split(".")[0]
   root.title(name)
   e1.insert(END, name)
   fp= open(fn,"r")
   paragraph = fp.read()
   t1.insert(END, paragraph)
   fp.close()
    
def save():
    sv = e1.get()
    data = open(sv+ ".txt", "w")
    sv2 = t1.get(1.0, END)
    data.write(sv2)
    print(data)
    t1.delete(1.0, END)
    e1.delete(0, END)
    messagebox.showinfo("Update!!", "Success")
    
    
def close1():
    root.destroy()
    


b1 = Button(root, image= o, command= op)
b1.place(relx=0.05, rely= 0.03, anchor= CENTER)

b2 = Button(root, image= s , command= save)
b2.place(relx=0.15, rely= 0.03, anchor= CENTER)

b3 = Button(root, image = c , command= close1)
b3.place(relx=0.25, rely= 0.03, anchor= CENTER)





root.mainloop()