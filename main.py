import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

engine = pyttsx3.init()

def speaknow():
    text = txt.get(1.0,END)
    gender = gendercb.get()
    speed = speedcb.get()
    voices = engine.getProperty('voices')
    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            engine.say(text)
            engine.runAndWait()
    if(text):
        if(speed == "Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed == "Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',50)
            setvoice()

def download():
    text = txt.get(1.0,END)
    gender = gendercb.get()
    speed = speedcb.get()
    voices = engine.getProperty('voices')
    def setvoice():
        if (gender == 'Male'):
            engine.setProperty('voice',voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice',voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
    if(text):
        if(speed == "Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed == "Normal"):
            engine.setProperty('rate',150)
            setvoice()
        else:
            engine.setProperty('rate',50)
            setvoice()

root = Tk()
root.title("Text to speech")
root.geometry("900x450")
root.resizable(False,False)
root.configure(bg="#305065")

image_icon = PhotoImage(file="images/speak.png")
root.iconphoto(False,image_icon)

#top frame
Top_frame = Frame(root,bg="white",width=900,height=100).place(x=0,y=0)

Logo = PhotoImage(file="images/speaker logo.png")
Label(Top_frame,image=Logo,bg="white").place(x=10,y=5)

Label(Top_frame,text="Text to Speech",font="arial 20 bold",bg="white",fg="black").place(x=100,y=30)

#interface
txt = Text(root,font="Robote 20",bg="White",relief=GROOVE,wrap=WORD)
txt.place(x=10,y=150,width=500,height=250)

Label(root,text="Voice",font="arial 15 bold",bg="#305065",fg="white").place(x=580,y=160)
Label(root,text="Speech",font="arial 15 bold",bg="#305065",fg="white").place(x=760,y=160)

gendercb = Combobox(root,values=['Male','Female'],font="arial 14",state='r',width=10)
gendercb.place(x=550,y=200)
gendercb.set('Male')

speedcb = Combobox(root,values=['Fast','Normal','Slow'],font="arial 14",state='r',width=10)
speedcb.place(x=730,y=200)
speedcb.set('Normal')

image1 = PhotoImage(file="images/speak.png")
Button(root,text="Speak",compound=LEFT,image=image1,width=130,font="arial 14 bold",command=speaknow).place(x=550,y=280)

image2 = PhotoImage(file="images/download.png")
Button(root,text="Save",compound=LEFT,image=image2,width=130,font="arial 14 bold",command=download).place(x=730,y=280)

root.mainloop()