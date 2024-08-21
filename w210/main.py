# Creating the various elements


from tkinter import *

# intiialize window
window = Tk()
window.title('Lesson w210')
window.minsize(width=600, height=300)
window.config(padx=100, pady=100)

# --- Header Section
header_label = Label(text='Lesson 210', font=('Arial', 24, "bold"))
# header_label.pack()
header_label.grid(column=0, row=0)

# --- button
def bu1_click():
	print("Got Click")
	new_text = input1.get()  # Get input from entry
	header_label.config(text=new_text)


bu1 = Button(text="CLICKME", command=bu1_click, font=("Courier New", 11))
bu1.grid(column=2, row=2)

bu2 = Button(text="Enter", font=("Arial", 15))
bu2.grid(column=4,row=4)

# -- Text Entry
input1 = Entry(font=('Arial', 20))
# input1.place(x=0, y=100)
# input1.pack(pady=10)
input1.grid(column=3, row=0)

# -- default loop
window.mainloop()
