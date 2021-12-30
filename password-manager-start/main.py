from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
EMAIL = "test@gmail.com"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    user_website = website_entry.get()
    user_email = email_entry.get()
    user_password = password_entry.get()
    new_data = {
        user_website: {
            "email": user_email,
            "password": user_password,
        }
    }

    if len(user_website) == 0 or len(user_email) == 0 or len(user_password) == 0:
        messagebox.showinfo(title="Warning!", message="Fields cannot be empty!")

    else:
        try:
            with open("data.json", mode="r") as file:
                #Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", mode="w") as file:
                #Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #

def find_password():
    user_website = website_entry.get()
    try:
        with open("data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error!", message=f"data.json is not found! Create some entries first!")
    else:
        if user_website in data:
            email = data[user_website]["email"]
            password = data[user_website]["password"]
            messagebox.showinfo(title="Login Info", message=f"Your login info for {user_website} is:"
                                                            f"\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error!", message=f"No data exists for {user_website} yet!")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row =1)
website_entry = Entry(width=25)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()

search_button = Button(text="Search", command=find_password, width=15)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row =2)
email_entry = Entry(width=44)
email_entry.grid(column=1, row=2, columnspan=2)
# inserts pre-populated email
email_entry.insert(0, EMAIL)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=25)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=generate_password, width=15)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", command=save, width=34)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()