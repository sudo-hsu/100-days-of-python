from tkinter import *
import random
import pandas

BACKGROUND_COLOR = "#B1DDC6"

# Read data from .csv and generate random word from list
random_word = {}
try:
    language_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    language_data_list = original_data.to_dict(orient="records")
else:
    language_data_list = language_data.to_dict(orient="records")


def translate():
    canvas.itemconfig(card_background, image=flashcard_back)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(word, text=random_word["English"], fill="white")


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(language_data_list)
    print(random_word)
    canvas.itemconfig(card_background, image=flashcard_front)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(word, text=random_word["French"], fill="black")
    flip_timer = window.after(3000, func=translate)


def is_known():
    language_data_list.remove(random_word)
    data = pandas.DataFrame(language_data_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# App Window
window = Tk()
window.title("Language Frequency Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=translate)

# Flashcard Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front = PhotoImage(file="images/card_front.png")
flashcard_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=flashcard_front)
canvas.grid(column=0, row=0, columnspan=2)
language = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))

# Buttons
checkmark_img = PhotoImage(file="images/right.png")
wrong_img= PhotoImage(file="images/wrong.png")

checkmark = Button(image=checkmark_img, command=is_known, highlightthickness=0)
checkmark.grid(column=1, row=1)

wrong = Button(image=wrong_img, command=next_card, highlightthickness=0)
wrong.grid(column=0, row=1)


next_card()





window.mainloop()
