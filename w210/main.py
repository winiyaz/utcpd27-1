# Creating the various elements


from tkinter import *

# intiialize window
window = Tk()
window.title('Lesson w210')
window.minsize(width=600, height=300)

# --- Header Section
header_label = Label(text='Lesson 210', font=('Arial', 24, "bold"))
header_label.pack()


# --- button
def bu1_click():
	print("Got Click")
	new_text = input1.get()  # Get input from entry
	header_label.config(text=new_text)


bu1 = Button(text="CLICKME", command=bu1_click)
bu1.pack()

# -- Text Entry
input1 = Entry(width=50, font=('Arial', 20), justify="center")
input1.pack(pady=10)

# -- default loop
window.mainloop()
