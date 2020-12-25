BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random
eng_word = ""
eng = None
card = None

#-------------------reac_file--------------#

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError or IndexError:
    data = pandas.read_csv("./data/french_words.csv")
    data_dict = data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


def get_word():
    global eng_word, eng, card
    eng = window.after(3000, show_Eng)
    try:
      card = random.choice(data_dict)
    except IndexError:
        window.after_cancel(eng)
        canvas.itemconfig(bg_img, image=card_front)
        canvas.itemconfig(title, text="Well Done", fill="red")
        canvas.itemconfig(word, text="You've memorized every card in this set.", fill="black", font=("Arial", 25))
        wrong.config(state=DISABLED)
        correct.config(state=DISABLED)
    else:
        new_word = card["French"]
        canvas.itemconfig(bg_img, image=card_front)
        canvas.itemconfig(title, text="French", fill="black")
        canvas.itemconfig(word, text=new_word, fill="black")
        eng_word = card["English"]

#-------------------checked--------------#
def remove_word():
   data_dict.remove(card)
   data=pandas.DataFrame(data_dict)
   data.to_csv("./data/words_to_learn.csv", index=False)
   get_word()
   print(len(data_dict))
#-------------------French_English--------------#
def show_Eng():
    window.after_cancel(eng)
    canvas.itemconfig(bg_img, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=eng_word, fill="white")
#-------------------UI--------------#

window = Tk()
window.title("Flashly")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back = PhotoImage(file="./images/card_back.png")
card_front = PhotoImage(file="./images/card_front.png")
bg_img = canvas.create_image(400, 263, image=card_front)
title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

#Button
wrong_img = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_img,  highlightthickness=0, command=get_word)
wrong.grid(column=0, row=2)
right_img = PhotoImage(file="./images/right.png")
correct = Button(image=right_img,  highlightthickness=0, command=remove_word)
correct.grid(column=1, row=2)


get_word()
window.mainloop()