from tkinter import*
import string
import random
import pyperclip

def generate():
    small_alphabets=string.ascii_lowercase
    capital_alphabetes=string.ascii_uppercase
    numbers=string.digits
    special_characters=string.punctuation

    all=small_alphabets+capital_alphabetes+numbers+special_characters
    password_length=int(length_Box.get())

    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alphabets,password_length))

    if choice.get()==2:
       passwordField.insert(0,random.sample(small_alphabets+capital_alphabetes,password_length))

    if choice.get()==3:
       passwordField.insert(0,random.sample(all,password_length))

    # password=random.sample(all,password_length)
    # passwordField.insert(0,password)

def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)
    

root = Tk()
root.config(bg="#FFEBCD")
choice=IntVar()
Font=("arial",13,"bold")
passwordLabel=Label(root,text="Password Generator",font=("Time New Roman",20,"bold"),bg="#FFEBCD",fg="#000000")
passwordLabel.grid(pady=10)
weakradiobutton=Radiobutton(root,text="weak",value=1,variable=choice,font=Font)
weakradiobutton.grid(pady=5)


mediumradiobutton=Radiobutton(root,text="medium",value=2,variable=choice,font=Font)
mediumradiobutton.grid(pady=5)

strongradiobutton=Radiobutton(root,text="strong",value=3,variable=choice,font=Font)
strongradiobutton.grid(pady=5)

lengthLabel=Label(root,text="Password Length",font=Font,bg="#FFEBCD",fg="#000000")
lengthLabel.grid(pady=5)

length_Box=Spinbox(root,from_=5,to_=18,width=5,font=Font)
length_Box.grid(pady=5)

generateButton=Button(root,text="Generate",font=Font,command=generate)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=Font)
passwordField.grid()

copyButton=Button(root,text="Copy",font=Font,command=copy)
copyButton.grid(pady=5)

root.mainloop()