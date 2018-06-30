# -*- coding: UTF-8 -*-
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import PIL.Image
import folium
import datetime
from Tkinter import *
from PIL import Image, ImageTk
import sys
from browser import BrowserDialog
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QUrl
from PyQt4.QtWebKit import QWebView
 


master = Tk() #  (main) window
master.title("Crime Predictions")  #Title the form
master.configure(background = '#494949')
master.resizable(False, False) #Block maximize window mode

#Label(master,text=None,image=logo).grid(row=0,columnspan=2,sticky=W,padx=80)
Label(master, text="Crime2Vec Prediction",fg='#FFFFFF',font=("Segoe UI Light", 45),bg='#494949').grid(row=0,columnspan=2,sticky=E,padx=40)




def report_crime():
    def quit2():
        master1.destroy()

    def add_to_database():
        F_date = f1.get()
        F_time = f2.get()
        F_category = f3.get()
        F_pdistrict = f4.get()
        F_desc = f5.get()
        F_xloc = f6.get()
        F_yloc = f7.get()
        
        f1.delete(0,END)
        f2.delete(0,END)
        f3.delete(0,END)
        f4.delete(0,END)
        f5.delete(0,END)
        f6.delete(0,END)
        f7.delete(0,END)


        #Split the date
        day_list = [7,1,2,3,4,5,6]
        split_date = F_date.split('-')
        day = int(split_date[0])
        month = int(split_date[1])
        year = int(split_date[2])
        date = datetime.date(year,month,day)
        day_of_week = date.weekday()+1
        day_of_week = day_list.index(day_of_week)+1

        #Split the time
        split_time=F_time.split(':')
        hour = split_time[0]
        minute = split_time[1]

        f=open('new_train(kaggledata).csv','a')
        f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %(day_of_week,day,month,year,hour,minute,F_category,F_pdistrict,F_xloc,F_yloc))
        f.close()

    #Create the add to database window
    master1 = Tk() #form window
    master1.title("Report Crime")  #Title of the form
    master1.configure(background = '#656565')
    master1.resizable(False, False) 
    Label(master1, text="Report a Crime",fg='#FFFFFF',font=("Segoe UI Light", 30),bg='#656565').grid(row=0,columnspan=1,sticky=W,padx=10,pady=10)
    Label(master1, text="* indicates mandatory fields",fg='#FFFFFF',font=("Segoe UI Light", 12),bg='#656565').grid(row=1,columnspan=1,sticky=W,padx=10,pady=10)


    #Label box in each row
    var = IntVar()
    Radiobutton(master1, text="Administrator",fg='#000000', variable=var,font=("Segoe UI Light", 15),bg='#494949', value=1).grid(sticky=W,row=2,columnspan=1,pady=10,padx=50)
    Radiobutton(master1, text="Verified User",fg='#000000', variable=var,font=("Segoe UI Light", 15),bg='#494949', value=2).grid(sticky=E,row=2,columnspan=2,pady=10,padx=50)
    Label(master1, text="Date of crime(dd-mm-yyyy)*",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=3,sticky=W,pady=10)
    Label(master1, text="Time of crime(hh:mm)*",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=4,sticky=W,pady=10)
    Label(master1, text="Category*",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=5,sticky=W,pady=10)
    Label(master1, text="PdDistrict*",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=6,sticky=W,pady=10)
    Label(master1, text="Description*",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=7,sticky=W,pady=10)
    Label(master1, text="Location(X Coordinate)",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=8,sticky=W,pady=10)
    Label(master1, text="Location(Y Coordinate)",fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#494949').grid(row=9,sticky=W,pady=10)

    
    #Text entry/box for each label
    f1=Entry(master1,width=30)
    f2=Entry(master1,width=30)
    f3=Entry(master1,width=30)
    f4=Entry(master1,width=30)
    f5=Entry(master1,width=30)
    f6=Entry(master1,width=30)
    f7=Entry(master1,width=30)
    
    #Text box in each row
    f1.grid(row=3, column=1,sticky=E,padx=10)
    f2.grid(row=4, column=1,sticky=E,padx=10)
    f3.grid(row=5, column=1,sticky=E,padx=10)
    f4.grid(row=6, column=1,sticky=E,padx=10)
    f5.grid(row=7, column=1,sticky=E,padx=10)
    f6.grid(row=8, column=1,sticky=E,padx=10)
    f7.grid(row=9, column=1,sticky=E,padx=10)


    Button(master1, text='Add crime',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#2C2827', command=add_to_database,height = 1, width = 15).grid(row=10,column=0,sticky=W,pady=30,padx=10)
    Button(master1, text='Cancel',fg='#FFFFFF',font=("Segoe UI Light", 15),bg='#2C2827', command=quit2,height = 1, width = 15).grid(row=10,column=1,sticky=W,pady=30,padx=10)

      
        
def hotspots():
    os.startfile('Predict.py')

def stats():
    # data to plot
    N = 5
    ViolentMeans = (20, 35, 30, 35, 27)
    NonViolentMeans = (25, 32, 34, 20, 25)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.40       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, ViolentMeans, width,color='r')
    p2 = plt.bar(ind, NonViolentMeans, width,color='mediumslateblue',
                 bottom=ViolentMeans)
    
    plt.xlabel('Police Division',fontsize=12)
    plt.ylabel('Crime Rates',fontsize=12)
    plt.title('Crime rates from previous day')
    plt.xticks(ind, ('Northern', 'Bayview', 'Richmond', 'Central', 'Southern'))
    plt.yticks(np.arange(0, 81, 10))
    plt.legend((p1[0], p2[0]), ('Violent Crimes', 'Non-Violent Crimes'))

    plt.show()


def about():
    about_window=Tk()
    about_window.title("About")
    about_window.configure(background = '#656565')
    about_window.resizable(False, False)
    Label(about_window, text="About",fg='#FFFFFF',font=("Segoe UI Light",30),bg='#656565').grid(row=0,sticky=W,padx=20,pady=20)
    Label(about_window, text="San Francisco Crime Prediction",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=1,sticky=W,padx=20,pady=0)
    Label(about_window, text="Version 10.1604.21020.0",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=2,sticky=W,padx=20,pady=0)
    Label(about_window, text="Developed by QCRI",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=3,sticky=W,padx=20,pady=0)
    Label(about_window, text="© Copyright 2017 QCRI",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=4,sticky=W,padx=20,pady=0)
    Label(about_window, text="All rights reserved.",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=5,sticky=W,padx=20,pady=0)
    Label(about_window, text=" ",fg='#FFFFFF',font=("Segoe UI Light",15),bg='#656565').grid(row=6,sticky=W,padx=20,pady=0)



    
image_addcrime = PIL.Image.open("Report_crime.png")
photo_addcrime = ImageTk.PhotoImage(image_addcrime)


image_hotspots = PIL.Image.open("Hotspots.png")
photo_hotspots = ImageTk.PhotoImage(image_hotspots)

image_statistics = PIL.Image.open("Statistics.png")
photo_statistics = ImageTk.PhotoImage(image_statistics)

image_about = PIL.Image.open("About.png")
photo_about = ImageTk.PhotoImage(image_about)

    
B1 = Button(master, text='Report Crime',fg='#3498DB',font=("Segoe UI Semibold", 16),bg='#494949', command=report_crime,height = 150, width = 150,image=photo_addcrime,compound="top",borderwidth=0)
B1.grid(row=1,columnspan=1,sticky=W,padx=111,pady=30)
B2 = Button(master, text='View Hotspots',fg='#3498DB',font=("Segoe UI Semibold", 16),bg='#494949', command=hotspots,height = 150, width = 150,image=photo_hotspots,compound="top",borderwidth=0)
B2.grid(row=1,columnspan=1,sticky=E,padx=0,pady=10)
B3 = Button(master, text='Statistics',fg='#3498DB',font=("Segoe UI Semibold", 16),bg='#494949',command=stats,height = 150, width = 150,image=photo_statistics,compound="top",borderwidth=0)
B3.grid(row=2,columnspan=1,sticky=W,padx=111,pady=10)
B4 = Button(master, text='About',fg='#3498DB',font=("Segoe UI Semibold", 16),bg='#494949', command=about,height = 150, width = 150,image=photo_about,compound="top",borderwidth=0)
B4.grid(row=2,columnspan=1,sticky=E,padx=0,pady=10)
mainloop()
