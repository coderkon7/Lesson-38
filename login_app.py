from tkinter import *

root = Tk()
root.title('Login App')
root.geometry('400x400')

frame = Frame(master=root, height=200, width=360, bg='#d0efff')

lbl1 = Label(frame, text="Full Name", bg="#3895D3", fg='white', width=12)
lbl2 = Label(frame, text="Email ID", bg="#3895D3", fg='white', width=12)
lbl3 = Label(frame, text="Enter Password", bg="#3895D3", fg='white', width=12)

name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show='*')

def display():
    name = name_entry.get()
    greet = "Hey "+name
    message = "\nYour account was succesfully created!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

textbox = Text(bg="#BEBEBE", fg='black')

btn = Button(text='Create Account', command=display, bg='red')

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=40)
email_entry.place(x=150, y=40)
lbl3.place(x=20, y=60)
pass_entry.place(x=150, y=60)
btn.place(x=150, y=100)
textbox.place(x=0, y=120)

root.mainloop()