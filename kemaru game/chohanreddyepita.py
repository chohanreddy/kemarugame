# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from functools import partial
import tkinter as tk
import tkinter.font as TkFont
import tkinter.messagebox
import random
from tkinter import *


interface = Tk()
interface.title("Kemaru Game")
interface.geometry("900x650")
changingnumber = 1
PLUS = 1
MINUS = 0
start = 11
oway = 1
button_identities = []
attempts = 0
helpp = 0
radiobutt = IntVar()
radiobutt.set(1)

def retrieve(widget, hi):
    global oway
    if hi == '1':
        widget.grid(row=oway, column=0)
        oway += 1
    elif hi == 'buttonlevel':
        widget.grid(row=4, column=15)
    elif hi == 'labellevel':
        widget.grid(row=2, column=14)
    elif hi == 'buttonlevel1':
        widget.grid(row=5, column=15)
    elif hi == 'label':
        widget['text'] = "pick a number to  Change"
        widget.grid(row=0, column=0)
    if oway > 5:
        oway = 1

def changlevel(m):
    global list21
    global list20
    global button_identities
    global attempts
    global helpp
    if m == 0:
        if helpp == 0:
            tkinter.messagebox.showinfo("Game Rule", "Please note that every help will increase your attempts by 50")
        if helpp > 0:
            attempts += 50
            labellevel["text"] = "No Attemps " + str(attempts)
        else:
            labellevel["text"] = "No Attemps " + str(attempts)
            helpp += 1
        rand13 = list(range(0, 80))
        indexes = random.sample(rand13, k=13)
        for i in indexes:
            list20[i] = list21[i]
        for i in range(len(list20)):
            e = list20[i]
            but = button_identities[i]
            if e > 0:
                but['text'] = list20[i]
            elif e == 0:
                but['text'] = ""
    if m == 11:
        attempts = 0
        labellevel["text"] = "Total Attemps " + str(attempts)
        retrieve(button1, "1")
        retrieve(button2, '1')
        retrieve(button3, '1')
        retrieve(button4, '1')
        retrieve(button5, '1')
        retrieve(labellevel, 'labellevel')
        retrieve(label, 'label')
        retrieve(buttonlevel1, 'buttonlevel1')
        # retrieve(buttonlevel, 'buttonlevel')
        for i in range(len(list17)):  # put zero in all the elements of list20  or RESET IT list17
            but = button_identities[i]
            list17[i] = 0
            but['text'] = ""
        attempts = 0
        rand13 = list(range(0, 80))
        indexes = random.sample(rand13, k=13)
        for i in indexes:
            list17[i] = list18[i]
        for i in range(len(list17)):
            e = list17[i]
            but = button_identities[i]
            if e > 0:
                but['text'] = list17[i]
            elif e == 0:
                but['text'] = ""

    if m == 1:
        # a['text']="hi how"
        for i in range(81):
            a = button_identities[i]
            b = list18[i]
            a['text'] = b
        
def forget(widget):    
    widget.grid_forget()


def changnum():
    global changingnumber
    changingnumber = radiobutt.get()
    
def change(n):
    global changingnumber
    global attempts
    global list17
    global list18
    # function to get the index and the identity (bname)
    bname = (button_identities[n])
    # print(button_identities[n])
    bname["text"] = str(changingnumber)
    attempts += 1
    labellevel["text"] = "Total Attemps " + str(attempts)

    list17[n] = changingnumber
    print(list17[n])
    if list17 == list18:
        tkinter.messagebox.showinfo("You Won the Game", 'Congrates You win the Game!')
    else:
        attempts += 1
    bname["fg"] = '#11670a'


def exitb():
    interface.destroy()


labellevel = Label(interface,width=12, height=1, text="Total Attemps ")
labellevel.grid(row=2, column=14)
buttonlevel01 = Button(interface, width=10, height=2, text=' New Game ', command=partial(changlevel, start))
buttonlevel = Button(interface, width=10, height=2, text=' check result ', command=partial(changlevel, PLUS))
buttonlevel1 = Button(interface, width=10, height=2, text=' Help ', command=partial(changlevel, MINUS))
buttonlevelexit = Button(interface, width=10, height=2, text=' Exit ', command=exitb)
buttonlevel01.grid(row=3, column=15)
buttonlevel.grid(row=4, column=15)
buttonlevel1.grid(row=5, column=15)
buttonlevelexit.grid(row=6, column=15)

label = Label(interface, text="Please press Start button", font=("Helvetica", 10,))
label.grid(row=0, column=0)
button1 = Radiobutton(interface, text='1', font=(['Bold']), variable=radiobutt, value=1, command=changnum)
button2 = Radiobutton(interface, text='2', font=(['Bold']), variable=radiobutt, value=2, command=changnum)
button3 = Radiobutton(interface, text='3', font=(['Bold']), variable=radiobutt, value=3, command=changnum)
button4 = Radiobutton(interface, text='4', font=(['Bold']), variable=radiobutt, value=4, command=changnum)
button5 = Radiobutton(interface, text='5', font=(['Bold']), variable=radiobutt, value=5, command=changnum)

button1.grid(row=1, column=0)
button2.grid(row=2, column=0)
button3.grid(row=3, column=0)
button4.grid(row=4, column=0)
button5.grid(row=5, column=0)

butt = ""
columnn = 2
roww = 3

list1 = [0, 1, 9, 18, 19]
list2 = [2, 3, 4, 10, 11]
list3 = [5, 13, 14, 22, 23]
list4 = [6, 7, 8, 15, 16]
list5 = [17, 24, 25, 26]
list6 = [27, 28, 36, 37, 38]
list7 = [20, 21, 29, 30, 39]
list8 = [31, 32, 40, 41, 42]
list9 = [33, 34, 35, 43, 44];
list10 = [45, 46, 47, 48, 54]
list11 = [49, 50, 51, 52, 53]
list12 = [63, 64, 72, 73, 55]
list13 = [56, 57, 65]
list14 = [58, 67, 68, 76, 77]
list15 = [59, 60, 69, 61, 62]
list16 = [70, 71, 78, 79, 80]
list17 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
          0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 0,0, 0, 0, 0, 0, 0, 0, ]

list18 = [2, 1, 3, 4, 5, 1, 3, 4, 2,
          2, 4, 3, 1, 5, 4, 3, 1, 2,
          3, 1, 2, 4, 2, 1, 2, 4, 3,
          2, 4, 3, 1, 3, 5, 3, 1, 2,
          1, 5, 2, 4, 2, 1, 2, 4, 3,
          4, 3, 1, 3, 5, 4, 3, 5, 1,
          1, 2, 4, 2, 1, 2, 1, 4, 3,
          4, 5, 1, 3, 4, 5, 3, 2, 1,
          3, 2, 4, 2, 1, 1, 2, 3, 4]

# helv36 = TkFont.Font(family='Helvetica', size=36, weight=tkFont.BOLD)
for i in range(81):
    columnn += 1
    butt = "button" + str(i + 1)
    butt = Button(interface, height=2, width=4, text=i + 1, font=("Helvetica", 12, ['bold']),
                  command=partial(change, i),relief = 'solid',activebackground = 'blue',)
    butt.grid(row=roww, column=columnn)
    button_identities.append(butt)
    if i in list1:
        butt['bg'] = '#e198da'         
        butt['bd'] = 2       
    elif i in list2:
        butt['bg'] = '#beb3bf'
        butt['bd'] = 2
    elif i in list3:
        butt['bg'] = '#dfbd8a'
        butt['bd'] = 2
    elif i in list4:
        butt['bg'] = '#86cbe5'
        butt['bd'] = 2
    elif i in list5:
        butt['bg'] = '#3cff10'
        butt['bd'] = 2
    elif i in list6:
        butt['bg'] = '#b510ff'
        butt['bd'] = 2
    elif i in list7:
        butt['bg'] = '#7a8d85'
        butt['bd'] = 2
    elif i in list8:
        butt['bg'] = '#ff6410'
        butt['bd'] = 2
    elif i in list9:
        butt['bg'] = '#ffad10'
        butt['bd'] = 2
    elif i in list10:
        butt['bg'] = '#FFFF10'
        butt['bd'] = 2
    elif i in list11:
        butt['bg'] = '#b5ff10'
        butt['bd'] = 2
    elif i in list12:
        butt['bg'] = '#ff10b9'
        butt['bd'] = 2
    elif i in list13:
        butt['bg'] = '#FF7070'
        butt['bd'] = 2
    elif i in list14:
        butt['bg'] = '#9ac930'
        butt['bd'] = 2
    elif i in list15:
        butt['bg'] = '#30c997'
        butt['bd'] = 2
    elif i in list16:
        butt['bg'] = '#0FF1FF'
        butt['bd'] = 2
    if (columnn == 11):
        columnn = 2
        roww += 1


# remove all the unnecessory wigdets from the
forget(button1)
forget(button2)
forget(button3)
forget(button4)
forget(button5)
forget(labellevel)
forget(buttonlevel1)
forget(buttonlevel)

# this widget will automatically retrive but calling changelevel(11) function underneath
radiobutt.set(1)
interface.configure(background='AntiqueWhite1')
changlevel(11)
forget(
    buttonlevel)
interface.mainloop()
