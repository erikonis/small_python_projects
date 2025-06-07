from tkinter import *
import Sound
from color import *
import database

# ---------------------------- CONSTANTS ------------------------------- #

WORK_MIN = 50    #50
SHORT_BREAK_MIN = 10 #10
LONG_BREAK_MIN = 15 #15
rep = 0
counter = ""
cycles = 0
do_count = False
reset_status = True
timer = None
mode = True
pause = False

data = database.Database()
record = data.read('pomos')

# ------------------------ CHANGE BG COLOR -------------------#
def change_bg(color):
    label.config(bg=color)
    tomato_count_label.config(text=counter, bg=color)
    window.config(bg=color)
    canvas.config(bg=color)
    records.config(bg=color)

# ---------------------------- TIMER MECHANISM ------------------------------- #
def reset_timer():
    global rep, counter, do_count, timer, reset_status

    reset_status = True
    do_count = False

    try:
        window.after_cancel(timer) #In the initiation it might fail, so we ignore it
    except ValueError:
        pass

    counter = ""    #reseting everything
    tomato_count_label.config(text=counter)
    rep = 0 # resetting the cycle
    label.config(text="Timer", fg=GREEN)
    change_bg(YELLOW)   #default color
    canvas.itemconfig(timer_label, text=f"{WORK_MIN}:00")

def begin_cycle():
    global rep, counter, cycles, record
    if rep > 8:
        cycles += 1
        counter = ""
        for i in range(cycles):
            counter += "🏆"
        rep = 1

    if rep > 0:
        record += 1
        data.write('pomos', record)
        records.config(text=f"Total: {record}")

    rep += 1


    if rep in (1, 3, 5, 7):
        count_down(WORK_MIN*60)
        label.config(text="WORK", fg=WORK_TEXT_COLOR)
        change_bg(WORK_COLOR)
        play.start()
    elif rep in (2, 4, 6):
        count_down(SHORT_BREAK_MIN*60)
        label.config(text="REST", fg=TEXT_COLOR)
        counter += "⭐"
        change_bg(REST_COLOR)
        play.finish()
    elif rep == 8:
        count_down(LONG_BREAK_MIN*60)
        label.config(text="REST", fg=TEXT_COLOR)
        change_bg(LONG_REST_COLOR)
        play.finish()

def count_down(count):
    global timer, current_count
    current_count = count
    if do_count:
        minutes = int(count/60)
        if count%60 < 10:
            seconds = f"0{count%60}"
        else:
            seconds = count%60

        if count < 6:
            play.countdown()

        canvas.itemconfig(timer_label, text=f"{minutes}:{seconds}")
        if count > -1:
            timer = window.after(1000, count_down, count-1)

        if count < 0:
            play.countdown_finish()
            begin_cycle()

#--------------------- CHANGE MODE -----------------#
def change():
    global mode, WORK_MIN, SHORT_BREAK_MIN
    if mode:
        WORK_MIN = 25
        SHORT_BREAK_MIN = 5
        reset_timer()
    else:
        WORK_MIN = 50
        SHORT_BREAK_MIN = 10
        reset_timer()
    mode = not mode

#--------------------- BUTTON EVENTS -------------#
def start_pause_pressed():
    global do_count, reset_status, current_count, start_pause_button
    play.button_click()

    do_count = not do_count
    if do_count and not reset_status:   #Resuming logic
        start_pause_button.config(text="Pause")
        count_down(current_count)
    elif do_count and reset_status:     #Resuming logic
        begin_cycle()
        start_pause_button.config(text="Pause")
        reset_status = False
    else:                               #Pause
        start_pause_button.config(text="Start")
        window.after_cancel(timer)


def mode_pressed():
    play.button_click()
    change()

def reset_pressed():
    play.reset()  #Sound
    reset_timer()

# ---------------------------- UI SETUP ------------------------------- #
def initiation():
    global play, window
    play = Sound.Sound()
    window = Tk()
    window.config(padx=100, pady=50, bg=YELLOW)
    window.title("Pomodoro Timer")

def visuals():
    global canvas, label, tomato_count_label, timer_label, tomato_img, records
    canvas = Canvas(height=224, width=200, highlightthickness=0)
    canvas.config(bg=YELLOW)
    tomato_img = PhotoImage(file="data/tomato.png")
    canvas.create_image(100, 112, image=tomato_img)

    timer_label = canvas.create_text(100, 130, text=f"{WORK_MIN}:00", fill="white", font=(FONT_NAME, 35, "bold"))
    canvas.grid(column=2, row=2)

    label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
    label.grid(column=2, row=1)

    tomato_count_label = Label(text="", bg=YELLOW, fg=PURPLE, font=(FONT_NAME, 16, "bold"))
    tomato_count_label.grid(column=2, row=4)

    records = Label(text=f"Total: {record}",  bg=YELLOW, font=(FONT_NAME, 12))
    records.grid(column=1, row=4)

def buttons():
    global start_pause_button, mode_button, reset_button
    start_pause_button = Button(text="Start", command=start_pause_pressed, width=8)
    start_pause_button.grid(column=1, row=3)

    mode_button = Button(text="Change", command=mode_pressed, width=8)
    mode_button.grid(column=2, row=3)

    reset_button = Button(text="Reset", command=reset_pressed, width=8)
    reset_button.grid(column=3, row=3)

#WORKSPACE:
initiation()
visuals()
buttons()
window.mainloop()