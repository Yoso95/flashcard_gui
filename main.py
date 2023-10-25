from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
BLACK = "#0E130F"
word_list = {}

#------------------- CREATE NEW FLASH CARDS ----------------------#
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    word_list = original_data.to_dict(orient='records')
else:
    word_list = data.to_dict(orient='records')

word_choice = random.choice(word_list)

def new_french_word():
    global time, word_choice
    word_choice = random.choice(word_list)
    window.after_cancel(time)
    canvas.itemconfig(word, text=word_choice['French'])
    canvas.itemconfig(card_view, image=front_card)
    canvas.itemconfig(language, text='French', fill='black')
    canvas.itemconfig(word, text=word_choice['French'], fill='black')
    time = window.after(3000, flip_card)


#-------------------------- FLIPPING THE CARD ------------------------#
def flip_card():
    canvas.itemconfig(card_view, image=back_card)
    canvas.itemconfig(language, text='English', fill='white')
    canvas.itemconfig(word, text=word_choice['English'], fill='white')


def known_word():
    word_list.remove(word_choice)
    word__data = pandas.DataFrame(word_list)
    word__data.to_csv("./data/words_to_learn.csv")
    new_french_word()


#-------------------------- UI SETUP ------------------------#
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

time = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = PhotoImage(file='./images/card_front.png')
back_card = PhotoImage(file='./images/card_back.png')
card_view = canvas.create_image(400, 262, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)

x_img = PhotoImage(file='./images/false.png')
x_button = Button(image= x_img, highlightthickness=0, command=new_french_word)
x_button.grid(column=0, row=1)

check_img = PhotoImage(file='./images/true.png')
check_button = Button(image= check_img, highlightthickness=0, command=known_word)
check_button.grid(column=1, row=1)

language = canvas.create_text(400, 150, text="French", font=('Arial', 40, 'italic'))
word = canvas.create_text(400, 263, text=word_choice['French'], font=('Arial', 60, 'bold'))

window.mainloop()
