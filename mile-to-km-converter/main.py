from tkinter import *

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=400, height=150)
window.config(padx=20, pady=20)


def convert_to_km():
    miles = float(miles_input.get())
    km = round((miles * 1.609), 2)
    answer_label.config(text=f"{km}")


# Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)


# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equals_label = Label(text="is equal to")
equals_label.grid(column=0, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

answer_label = Label(text="0")
answer_label.grid(column=1, row=1)


# Button
calc_button = Button(text="Calculate", command=convert_to_km)
calc_button.grid(column=1, row=2)


window.mainloop()