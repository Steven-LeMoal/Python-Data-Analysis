# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 09:06:20 2021

@author: chendeb
"""

from tkinter import *

fenetre = Tk()
fenetre.title('Calculatrice')
#fenetre.geometry("400x400")

e = Entry(fenetre, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def Bouton_Saisi(nbre):
	nouveau_nombre = e.get() + str(nbre)
	e.delete(0, END)
	e.insert(0, nouveau_nombre)

def Bouton_Effacer():
	e.delete(0, END)

def Bouton_Add(first_number):
	global f_num
	global monOperation
	monOperation = "addition"
	f_num = first_number
	#e.insert(0, first_number)
	e.delete(0, END)

#methode à completer pour soustraction, multiplication et division

def Bouton_Egal(second_number):
	num_1 = f_num
	if monOperation == "addition":
		e.delete(0, END)
		e.insert(0, int(num_1) + int(second_number))
    #à completer pour autre type d'operation

bouton_1 = Button(fenetre, text="1", padx=40, pady=20, command=lambda: Bouton_Saisi(1))
bouton_2 = Button(fenetre, text="2", padx=40, pady=20, command=lambda: Bouton_Saisi(2))
bouton_3 = Button(fenetre, text="3", padx=40, pady=20, command=lambda: Bouton_Saisi(3))
bouton_4 = Button(fenetre, text="4", padx=40, pady=20, command=lambda: Bouton_Saisi(4))
bouton_5 = Button(fenetre, text="5", padx=40, pady=20, command=lambda: Bouton_Saisi(5))
bouton_6 = Button(fenetre, text="6", padx=40, pady=20, command=lambda: Bouton_Saisi(6))
bouton_7 = Button(fenetre, text="7", padx=40, pady=20, command=lambda: Bouton_Saisi(7))
bouton_8 = Button(fenetre, text="8", padx=40, pady=20, command=lambda: Bouton_Saisi(8))
bouton_9 = Button(fenetre, text="9", padx=40, pady=20, command=lambda: Bouton_Saisi(9))
bouton_0 = Button(fenetre, text="0", padx=40, pady=20, command=lambda: Bouton_Saisi(0))
bouton_effacer = Button(fenetre, text="Clear", padx=79, pady=20, command=Bouton_Effacer)
bouton_add = Button(fenetre, text="+", padx=39, pady=20, command=lambda: Bouton_Add(e.get()))
bouton_egal = Button(fenetre, text="=", padx=91, pady=20, command=lambda: Bouton_Egal(e.get()))


bouton_1.grid(row=3, column=0)
bouton_2.grid(row=3, column=1)
bouton_3.grid(row=3, column=2)

bouton_4.grid(row=2, column=0)
bouton_5.grid(row=2, column=1)
bouton_6.grid(row=2, column=2)

bouton_7.grid(row=1, column=0)
bouton_8.grid(row=1, column=1)
bouton_9.grid(row=1, column=2)

bouton_0.grid(row=4, column=0)
bouton_effacer.grid(row=4, column=1, columnspan=2)

bouton_add.grid(row=5, column=0)

bouton_egal.grid(row=5, column=1, columnspan=2)

fenetre.mainloop()