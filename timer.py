import tkinter as tk
from tkinter import messagebox
import time

def start_countdown():
    try:
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers")
        return

    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set(f"{hours:02d}")
        minute.set(f"{mins:02d}")
        second.set(f"{secs:02d}")

        root.update()
        time.sleep(1)

        if temp == 0:
            messagebox.showinfo("Time Countdown", "Time's up!")
        temp -= 1

root = tk.Tk()
root.geometry("300x150")
root.title("Countdown Timer")

hour = tk.StringVar()
minute = tk.StringVar()
second = tk.StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hour_entry = tk.Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
hour_entry.place(x=80, y=20)

minute_entry = tk.Entry(root, width=3, font=("Arial", 18, ""), textvariable=minute)
minute_entry.place(x=130, y=20)

second_entry = tk.Entry(root, width=3, font=("Arial", 18, ""), textvariable=second)
second_entry.place(x=180, y=20)

start_button = tk.Button(root, text='Start', bd='5', command=start_countdown)
start_button.place(x=120, y=80)

root.mainloop()
