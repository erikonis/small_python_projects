BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

# -----------------GUI------------------#
screen = Tk()
screen.config(bg=BACKGROUND_COLOR, pady=50, padx=50)
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

#-----------------FILE READ------------------#
import pandas
from random import *

with open(file="./data/words_to_learn.csv", mode="r") as file:
    data = pandas.read_csv(file)
    words_dict = data.to_dict(orient="records")
language = "French"
current_card = choice(words_dict)
current_word = current_card[language]

def reset():
    global language, current_card, current_word
    with open(file="./data/french_words.csv", mode="r") as file:
        data = pandas.read_csv(file)
        words_dict = data.to_dict(orient="records")
    language = "French"
    current_card = choice(words_dict)
    current_word = current_card[language]

#---------------FUNCTIONS------------------#
def new_word():
    global words_dict, language, current_word, current_card, countdown
    screen.after_cancel(countdown)
    language = "French"
    current_card = choice(words_dict)
    current_word = current_card[language]
    canvas.itemconfig(word, text=current_word, fill="black")
    canvas.itemconfig(title, text=language, fill="black")
    canvas.itemconfig(flashcard, image=card_front_image)

    countdown = screen.after(3000, flip_card)

def flip_card():
    global words_dict, language, current_word, current_card

    language = "English"
    current_word = current_card[language]
    canvas.itemconfig(word, text=current_word, fill="white")
    canvas.itemconfig(title, text=language, fill="white")
    canvas.itemconfig(flashcard, image=card_back_image)

def correct():
    words_dict.remove(current_card)
    if len(words_dict) == 0:
        reset()
    else:
        new_word()

def false():
    new_word()

#------------FLASHCARDS------------------#
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)
flashcard = canvas.create_image(400, 263, image=card_front_image)
title = canvas.create_text(400,150, text=language, font=("Ariel", 40, "italic"))
word = canvas.create_text(400,263, text=current_word, font=("Ariel", 60, "bold"))

#----------------Buttons---------------#
right_button = Button(image=right_image, highlightthickness=0, command=correct)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=false)
wrong_button.grid(column=0, row=1)

countdown = screen.after(3000, flip_card)
screen.mainloop()

# -------------SAVE DATA---------------#
words_to_learn = pandas.DataFrame(words_dict)
words_to_learn.to_csv("./data/words_to_learn.csv", index=False)

