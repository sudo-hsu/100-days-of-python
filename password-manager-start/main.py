from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=1)

window.mainloop()