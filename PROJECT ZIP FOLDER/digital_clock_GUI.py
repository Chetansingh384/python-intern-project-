import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from time import strftime

class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")

        # Set full screen and hacker theme
        self.root.attributes("-fullscreen", True)
        self.root.configure(bg="black")

        self.is_24_hour_format = True

        self.create_widgets()
        self.update_clock()

    def create_widgets(self):
        # Create and place time label in the center
        self.time_label = ttk.Label(self.root, font=("DS-Digital", 120), background="black", foreground="green")
        self.time_label.pack(expand=True)

        # Create and place date label in the center
        self.date_label = ttk.Label(self.root, font=("DS-Digital", 48), background="black", foreground="green")
        self.date_label.pack(expand=True)

        # Create toggle button for time format
        self.toggle_button = ttk.Button(self.root, text="Toggle 12/24 Hour", command=self.toggle_time_format, style="Hacker.TButton")
        self.toggle_button.pack()

        # Create buttons to set time and date
        self.set_time_button = ttk.Button(self.root, text="Set Time", command=self.set_time, style="Hacker.TButton")
        self.set_time_button.pack()

        self.set_date_button = ttk.Button(self.root, text="Set Date", command=self.set_date, style="Hacker.TButton")
        self.set_date_button.pack()

        # Define the hacker theme style
        self.root.style = ttk.Style()
        self.root.style.configure("Hacker.TButton", foreground="green", background="black", font=("DS-Digital", 24))

    def toggle_time_format(self):
        self.is_24_hour_format = not self.is_24_hour_format

    def set_time(self):
        new_time = simpledialog.askstring("Set Time", "Enter time (HH:MM:SS):")
        if new_time:
            try:
                new_time_struct = strftime(new_time)
                self.time_label.config(text=new_time_struct)
            except ValueError:
                tk.messagebox.showerror("Invalid Time", "Please enter time in HH:MM:SS format")

    def set_date(self):
        new_date = simpledialog.askstring("Set Date", "Enter date (Weekday, Month DD, YYYY):")
        if new_date:
            try:
                new_date_struct = strftime(new_date)
                self.date_label.config(text=new_date_struct)
            except ValueError:
                tk.messagebox.showerror("Invalid Date", "Please enter date in 'Weekday, Month DD, YYYY' format")

    def update_clock(self):
        if self.is_24_hour_format:
            current_time = strftime("%H:%M:%S")
        else:
            current_time = strftime("%I:%M:%S %p")

        self.time_label.config(text=current_time)

        current_date = strftime("%A, %B %d, %Y")
        self.date_label.config(text=current_date)

        self.root.after(1000, self.update_clock)

if __name__ == "__main__":
    root = tk.Tk()
    clock = DigitalClock(root)
    root.mainloop()
