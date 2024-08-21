# Building Prgram

from tkinter import *

# WindowSetup
window = Tk()
window.title('Temp Converter')
window.minsize(width=600, height=400)
window.configure(bg="#020617", padx=20, pady=20)

# Main label
main_label = Label(text="Temperature Converter", fg="#eab308", bg="black", font=("Arial", 20, 'bold'))
main_label.grid(column=2, row=0)

# Enter Farenheight
far_entry = Entry(bg="black", fg="yellow", font=("Courier", 20), justify="center", insertbackground="hotpink")
far_entry.grid(column=2, row=1, pady=20)
far_entry_label = Label(text="Farenheit", bg="black", fg="yellow", font=("Courier", 20))
far_entry_label.grid(column=3, row=1)


# Function to highlight the Entry widget when focused
def on_focus_in(event):
	far_entry.config(bg="#052e16", fg="#ecfccb")


def on_focus_out(event):
	far_entry.config(bg="black", fg="yellow")


# Bind focus events to the Entry widget
far_entry.bind("<FocusIn>", on_focus_in)
far_entry.bind("<FocusOut>", on_focus_out)

# Celcius label
celcius_text = "0"
celcius_label = Label(text="0", bg="black", fg="#84cc16", font=('Arial', 25, "italic"))
celcius_label.grid(column=2, row=2, pady=20)
celcius_label_describe = Label(text="isEqualTo", bg="black", fg="#84cc16", font=('Arial', 25))
celcius_label_describe.grid(column=1, row=2, pady=20)


# Button and function


def converter_click():
	try:
		fahrenheit = float(far_entry.get())
		celsius = (fahrenheit - 32) * 5.0 / 9.0
		celcius_label.config(text=f"{celsius:.2f} °C")
	except ValueError:
		celcius_label.config(text="Invalid input")


converter_button = Button(text="Convert", bg="black", fg="white", font=("Arial", 20), command=converter_click)
converter_button.grid(column=2, row=3, pady=20)

# --- Window loop
window.mainloop()
