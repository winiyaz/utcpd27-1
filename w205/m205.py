# Using tkinter here

# Importing the tkinter built in lib
import tkinter

# Setting up the window
window = tkinter.Tk()

# -- Actual Logic --

window.title('PantySmell')  # Window size
window.minsize(width=800, height=300)  # Window minimum size

# Change the background color of the window
window.configure(bg="lightgray")

# Label
my_label = tkinter.Label(text="BootyDancer", font=('Arial', 24, "bold"),  bg="lightblue", fg="darkred")
my_label.pack(side="left")

# --- Required to keep the window open logic should be above ---
# Whileloop to keep window open for interaction
window.mainloop()
