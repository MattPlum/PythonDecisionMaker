import tkinter as tk
import os
from random import choice
from turtle import clear
import random

choices = []

def getChoices():
    choices.append(entry.get())
    
def clear_text():
    entry.delete(0,tk.END)

def addChoice():
    choices.append(entry.get())
    clear_text()
            
def makeDecision():
    label2.config(text=random.choice(choices))
    



root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")   #make can
canvas.pack()   #attach canvas to root

frame = tk.Frame(root, bg="white") 
frame.place(relwidth=0.8, relheight=0.8, relx = 0.1, rely=0.1)

label1 = tk.Label(root, text= "Enter your choices")
canvas.create_window(200, 130, window=label1)

entry = tk.Entry (root) 
canvas.create_window(200, 160, window=entry)

label2 = tk.Label(root, text= "")
canvas.create_window(200, 220, window=label2)

addButton = tk.Button(root, text="Add Choice", padx=10, pady=5, fg="white", bg="#263D42", command=addChoice)
canvas.create_window(200, 190, window=addButton)

makeDecisionButton = tk.Button(root, text="Make Decision", padx=10, pady=5, fg="white", bg="#263D42", command=makeDecision)
makeDecisionButton.pack()

root.mainloop()
