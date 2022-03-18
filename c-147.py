from tkinter import *

root=Tk()
root.title("Ascii")

root.geometry("400x400")
root.configure(background = "snow")

enter_word = Entry(root)
enter_word.place(relx=0.5,rely=0.4,anchor=CENTER)

label = Label(root, text = "Name in Ascii: ", bg="light yellow", fg = "black")
label2 = Label(root, text = "Name encrypted:", bg="cyan", fg = "black")
            
def asciiConverter():
   input_word = str(enter_word.get())
    
   for letter in input_word:
       label["text"] += str(ord(letter))+ "  "
       original= int(ord(letter))
       encrypt = original-1
       label2["text"]+= str(chr(encrypt))
       
        
btn = Button (root,text = "Display the Ascii code and Encrypted Value", command = asciiConverter, bg="gold", fg="black")
btn.place(relx=0.5, rely=0.5,anchor=CENTER)

label.place(relx=0.5, rely=0.6,anchor=CENTER)
label2.place(relx=0.5, rely=0.7,anchor=CENTER)

root.mainloop()