# -*- coding: UTF-8 -*-
import numpy as np
import os
import PIL.Image
import tkFont
from Tkinter import *
from PIL import Image, ImageTk


#Create the Registration window
master1 = Tk() #  (main) window
master1.title("Crime Prediction")  #Title the form
master1.configure(background = '#35302F')
master1.resizable(False, False)
Label(master1, text="SF Police Dept",fg='#FFFFFF',font=("Segoe UI Light", 40),bg='#35302F').grid(row=0,sticky=W,padx=28,pady=10)
Label(master1, text="________________",fg='#FFFFFF',font=("Segoe UI Light", 20),bg='#35302F').grid(row=3,sticky=W,padx=100,pady=0)
Label(master1, text="Username",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#35302F').grid(row=4,sticky=W,pady=10,padx=10)
Label(master1, text="Password",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#35302F').grid(row=5,sticky=W,pady=10,padx=10)
Label(master1, text=" ",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#35302F').grid(row=8,sticky=W,pady=0,padx=10)


f1=Entry(master1,width=30)
f2=Entry(master1,width=30)

f1.grid(row=4,sticky=E,padx=50)
f2.grid(row=5,sticky=E,padx=50)



menubar = Menu(master1)
master1.config(menu=menubar)

fileMenu = Menu(menubar)



def Homepage():
    def quit4():
        master1.destroy()
    def quit5():
        f1.delete(0,END)
        f2.delete(0,END)
        master2.destroy()
    if f1.get()=="admin" and f2.get()=="admin":
        quit4()
        os.startfile('Homepage.py')
    else:
        master2=Tk()
        master2.title("Incorrect Password")
        master2.configure(background = '#FFF7F4')
        Label(master2, text="Warning: Incorrect password was entered",fg='#000000',font=("Segoe UI Light", 15),bg='#FFF7F4').grid(row=0,sticky=W,padx=5,pady=10)
        B3 = Button(master2, text='Reset',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#2C2827', command=None,height = 1, width = 16)
        B3.grid(row=1,sticky=W,pady=0,padx=0)
        B4 = Button(master2, text='Cancel',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#2C2827', command=quit5,height = 1, width = 16)
        B4.grid(row=1,sticky=E,pady=0,padx=0)


def about(event):
    about_window=Tk()
    about_window.title("About")
    about_window.configure(background = '#800011')
    Label(about_window, text="About",fg='#FFFFFF',font=("Segoe UI Light",30),bg='#800011').grid(row=0,sticky=W,padx=20,pady=20)
    Label(about_window, text="Simple ChatBot (with RSA Encryption)",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#800011').grid(row=1,sticky=W,padx=20,pady=0)
    Label(about_window, text="Version 10.1604.21020.0",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#800011').grid(row=2,sticky=W,padx=20,pady=0)
    Label(about_window, text="Developed by Joel Jogy",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#800011').grid(row=3,sticky=W,padx=20,pady=0)
    Label(about_window, text="© Copyright 2018 MIT,Manipal",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#800011').grid(row=4,sticky=W,padx=20,pady=0)
    Label(about_window, text="All rights reserved.",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#800011').grid(row=5,sticky=W,padx=20,pady=0)
    Label(about_window, text=" ",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#800011').grid(row=6,sticky=W,padx=20,pady=0)



def about2():
   return about(1)


# setting up the menu bar
helpMenu = Menu(menubar)
helpMenu.add_command(label='About Chatbot',underline=0,command=about2)
helpMenu.add_separator()

fileMenu.add_command(label="RSA Settings", underline=0, command=None)
fileMenu.add_command(label="Exit", underline=0, command=None)
menubar.add_cascade(label="File", underline=0, menu=fileMenu)
menubar.add_cascade(label="Options", underline=0, menu=fileMenu)
menubar.add_cascade(label="Help", underline=0, menu=helpMenu)


# loading images for homepage
image_logo = PIL.Image.open("Logo.png")
photo_logo = ImageTk.PhotoImage(image_logo)



# buttons for the homepage

#Logo
B1 = Button(master1, text=None,fg='#3498DB',font=("Segoe UI Semibold", 16),bg='#35302F', command=None,height = 120, width = 150,image=photo_logo,compound="top",borderwidth=0)
B1.grid(row=2,columnspan=1,sticky=W,padx=110,pady=10)

#Log in
B2 = Button(master1, text='Log in',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#2C2827', command=Homepage,height = 1, width = 30)
B2.grid(row=6,sticky=W,pady=5,padx=16)

mainloop()
