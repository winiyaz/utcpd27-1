# Tkinter main here

# import tkinter as tk
from tkinter import *

# Intialize window
window = Tk()
window.title('Lesson 209')
window.minsize(width=600, height=300)

# Adding Labels
header_label = Label(text='Lesson 209', font=('Arial', 24, "bold"))
header_label.pack()


# Update the label
# header_label.config(text="Panty")

# Even listener
def bu1_click():
	print("Got Click")
	new_text = input1.get()  # Get input from entry
	header_label.config(text=new_text)


# Creating a button
bu1 = Button(text="ClickMe", command=bu1_click)
bu1.pack()

# Entry Input Component
input1 = Entry(width=50, font=('Arial', 20), justify="center")
input1.pack(pady=10)

# --- Required for keeping window open---
window.mainloop()
