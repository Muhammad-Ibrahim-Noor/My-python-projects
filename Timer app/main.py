import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
GREEN_DARK = '#3E8E7E'
DARK_BLUE = '#041C32'
STORM_BLUE = '#4C3F91'
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    screen.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    our_title.config(text='Timer')
    check_mark.config(text="")
    global REPS
    REPS = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    REPS += 1

    in_seconds = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_brake = LONG_BREAK_MIN * 60
    # count_down(in_seconds)
    if REPS % 8 == 0:
        count_down(long_brake)
        our_title.config(text='25 Minutes Break', fg=GREEN_DARK, bg=DARK_BLUE)
    elif REPS % 2 == 0:
        count_down(short_break)
        our_title.config(text='5 Minutes Break', fg=GREEN_DARK, bg=DARK_BLUE)
    else:
        count_down(in_seconds)
        our_title.config(text='Work', fg=GREEN_DARK, bg=DARK_BLUE)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time):
    count_minute = math.floor(time / 60)
    count_seconds = time % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")

    if time > 0:
        global timer
        timer = screen.after(1000, count_down, time - 1)  # screen.after(milliseconds, function, *args)

    else:
        start_timer()
        mark = ''
        work_sessions = math.floor(REPS / 2)
        for each_item in range(work_sessions):
            mark += '✔'
        check_mark.config(text=mark)  # use config() to update


# ---------------------------- UI SETUP ------------------------------- #
screen = tk.Tk()
screen.title("Timer")
screen.config(padx=100, pady=100, bg=DARK_BLUE)
canvas = tk.Canvas(width=200, height=224, bg=STORM_BLUE, highlightthickness=0)
our_image = tk.PhotoImage(file="clock-icons-noun-project-645655.png")
our_title = tk.Label(text='TIMER', fg=GREEN_DARK, bg=DARK_BLUE, font=(FONT_NAME, 30, 'bold'))
our_title.grid(column=1, row=0)
canvas.create_image(100, 112, image=our_image)
timer_text = canvas.create_text(102, 150, text="00:00", font=(FONT_NAME, 15, 'bold'))

canvas.grid(column=1, row=1)

# Buttons:
start_button = tk.Button(text='START', command=start_timer, bg=DARK_BLUE, fg=GREEN_DARK, font=(FONT_NAME, 15, 'bold'))
start_button.grid(column=0, row=2)
reset_button = tk.Button(text='RESET', command=reset_timer, bg=DARK_BLUE, fg=GREEN_DARK, font=(FONT_NAME, 15, 'bold'))
reset_button.grid(column=2, row=2)
# CheckMarks:
check_mark = tk.Label(bg=DARK_BLUE, fg=GREEN_DARK, font=(FONT_NAME, 15, 'bold'))
check_mark.grid(column=1, row=3)

screen.mainloop()
