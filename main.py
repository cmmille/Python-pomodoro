from tkinter import *
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1)

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    header.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text = "00:00")
    tracker.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    track_checks(reps)

    if reps % 8 == 0:
        header.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN*60)
    elif reps % 2 != 0:
        header.config(text="Work", fg=GREEN)
        count_down(WORK_MIN*60)
    else:
        header.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN*60)


def track_checks(reps):
    text = ""
    if reps %2 == 0:
        for n in range(0, reps, 2):
            text+="✓"
        tracker.config(text=text)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def format_time(var):
    if var < 10:
        return f"0{var}"
    else:
        return var

def count_down(count):
    minutes = int(count/60)
    seconds = int(count%60)
    display_time = f"{format_time(minutes)}:{format_time(seconds)}"

    canvas.itemconfig(timer_text, text = display_time)
    if count > 0:
        global timer
        timer =window.after(1000, count_down, count-1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=100, bg=YELLOW)

# Header
header = Label(text="Timer",
               font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
header.grid(row=0, column=1)
# Tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 16, "bold"))
canvas.grid(row=1, column=1)

# Buttons
btn_start = Button(text="Start", font=("Arial", 10), bg="white", command=start_timer)
btn_start.grid(row=2, column=0)

btn_reset = Button(text="Reset", font=("Arial", 10), bg= "white", command= reset_timer)
btn_reset.grid(row=2, column=2)
# Tracker
tracker = Label(text="", font=("Arial", 16, "bold"), fg=GREEN, bg=YELLOW)
tracker.grid(row = 3, column=1)


window.mainloop()
