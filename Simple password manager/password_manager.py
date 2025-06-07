import json
from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox

EMAIL = "default@email.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import randint, choice, shuffle
import pyperclip
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list += ([choice(letters) for char in range(randint(8, 10))])
    password_list += ([choice(symbols) for char in range(randint(2, 4))])
    password_list += ([choice(numbers) for char in range(randint(2, 4))])
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = web_entry.get().lower()
    email = username_email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Empty fields detected", message="Do not leave any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Typed details:\nEmail/Username: {email}\nPassword: {password}\nSave?")
        if is_ok:
            new_data = {
                website:{
                    "email":email,
                    "password":password
                }
            }
            try:
                with open(file="data.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open(file="data.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open(file="data.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                password_entry.delete(0, END)
                web_entry.delete(0, END)
                web_entry.focus()
# ------------------------- WEBSITE SEARCH ---------------------------- #
def search():
    website = web_entry.get().lower()
    if len(website) == 0:
        messagebox.showinfo(title="Error", message="Can't search for a an invisible website, sorry.")
    else:
        try:
            with open(file="data.json", mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="Data file not found.\nIn other words, no passwords saved yet.")
        else:
            try:
                messagebox.showinfo(title=website, message=f"Email: {data[website]["email"]}\nPassword: {data[website]["password"]}")
            except KeyError:
                messagebox.showinfo(title="Error", message=f"Website `{website}` not found.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
#window.minsize(width=500, height=400)
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

#--------Labels:
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
#-------Entries:
web_entry = Entry(width=35)
web_entry.grid(column=1, row=1, sticky="EW")
web_entry.focus()
username_email_entry = Entry()
username_email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
username_email_entry.insert(0, EMAIL)
password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")
#-------Buttons:
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add", command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")
search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="EW")


window.mainloop()