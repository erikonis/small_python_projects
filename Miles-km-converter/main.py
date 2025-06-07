
from tkinter import *

#TODO: 1 - Create window+layout.
#TODO: 2 - Create functionality
#TODO: 3 - Create Functions and Conversion

MILES_COLUMN = 3
MILES_ROW = 1
KM_COLUMN = 3
KM_ROW = 2
FONT = ("Arial", 13, "bold")

def convert():
    if mile_to_km_conversion:
        converted_label.config(text=int(input.get())*1.6)
    else:
        converted_label.config(text=int(input.get())/1.6)

def switch():
    global mile_to_km_conversion
    if mile_to_km_conversion:
        converted_label.config(text="None")
        miles_label.grid(column=KM_COLUMN, row=KM_ROW)
        km_label.grid(column=MILES_COLUMN, row=MILES_ROW)
        mile_to_km_conversion = False
    else:
        converted_label.config(text="None")
        miles_label.grid(column=MILES_COLUMN, row=MILES_ROW)
        km_label.grid(column=KM_COLUMN, row=KM_ROW)
        mile_to_km_conversion = True

window = Tk()
window.title("Miles-Km Converter")
window.minsize(width=300,height=100)
window.config(padx=20,pady=20)

mile_to_km_conversion = True

input = Entry(width=10)
input.grid(column=2, row=1)

miles_label = Label(text="Miles", font=FONT)
miles_label.grid(column=MILES_COLUMN, row=MILES_ROW)
miles_label.config(padx=10)

km_label = Label(text="Km", font=FONT)
km_label.grid(column=KM_COLUMN, row=KM_ROW)

equal_label = Label(text="is equal to", font=FONT)
equal_label.grid(column=1, row=2)
equal_label.config(padx=10, pady=5)

converted_value = 0
converted_label = Label(text=converted_value, font=FONT)
converted_label.grid(column=2, row=2)

calculation_button = Button(text="Calculate", command=convert)
calculation_button.grid(column=2, row=3)

switch_button = Button(text="Switch", command=switch)
switch_button.grid(column=3, row=3)

window.mainloop()