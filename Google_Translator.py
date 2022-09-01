from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

#Use translator
def change(text="type",src="English",dest="Hindi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,src=src1,dest=dest1)
    return trans1.text

def data():
    s=comb_Sourc.get()
    d=comb_dest.get()
    masg=stxt.get(1.0,END)
    textget=change(text=masg,src=s,dest=d)
    dtxt.delete(1.0,END)
    dtxt.insert(END,textget)

#Main
win=Tk()
win.title("Translator")
win.geometry("500x500+500+100")
win.config(bg='cyan')

#1st line
lab=Label(win, text="Translator", font=("Time New Roman",40), bg='cyan', fg='blue')
lab.place(x=100, y=10, height =50, width=300)

frame=Frame(win).pack(side=BOTTOM)

#Source Box
lab=Label(win, text="Source Text", font=("Time New Roman",10), bg='cyan', fg='red')
lab.place(x=100, y=70, height =10, width=300)

stxt=Text(frame, font=("Time New Roman",20), wrap=WORD)
stxt.place(x=20, y=80, height =100, width=460)

#Language
Lst=list(LANGUAGES.values())

comb_Sourc=ttk.Combobox(frame, value=Lst)
comb_Sourc.place(x=20, y=190, height =20, width=70)
comb_Sourc.set("english")

butchange=Button(frame, text="Translate", relief=RAISED, command=data)
butchange.place(x=100, y=190, height =20, width=70)

comb_dest=ttk.Combobox(frame, value=Lst)
comb_dest.place(x=180, y=190, height =20, width=70)
comb_dest.set("english")

#Destination Box
lab=Label(win, text="Destination Text", font=("Time New Roman",10), bg='cyan', fg='red')
lab.place(x=100, y=220, height =10, width=300)

dtxt=Text(frame, font=("Time New Roman",20), wrap=WORD)
dtxt.place(x=20, y=230, height =100, width=460)

win.mainloop()