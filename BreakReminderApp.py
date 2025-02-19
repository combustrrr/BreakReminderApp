import time
import threading
import winsound
from tkinter import Tk, Label, Button, Toplevel, Entry
import json

DEFAULT_INTERVAL = 20
DEFAULT_COUNTDOWN_DURATION = 20


class BreakReminderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("CVS Reminder")
        self.master.geometry("300x150")
        self.master.resizable(False, False)

        # Timer state attributes
        self.running = False
        self.timer_thread = None

        # UI setup
        self.setup_ui()

        self.load_settings()
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)

    def setup_ui(self):
        """Setup all UI elements for the app."""
        self.label = Label(self.master, text="Periodic Break Reminder", font=("Arial", 14))
        self.label.pack(pady=10)

        self.interval_entry = Entry(self.master)
        self.interval_entry.insert(0, str(DEFAULT_INTERVAL))
        self.interval_entry.pack(pady=5)

        self.start_button = Button(self.master, text="Start", command=self.start_timer, width=10, bg="green",
                                   fg="white")
        self.start_button.pack(pady=5)

        self.stop_button = Button(self.master, text="Stop", command=self.stop_timer, width=10, bg="red", fg="white",
                                  state="disabled")
        self.stop_button.pack(pady=5)

        self.pause_button = Button(self.master, text="Pause", command=self.pause_timer, width=10, bg="orange",
                                   fg="white", state="disabled")
        self.pause_button.pack(pady=5)

        self.resume_button = Button(self.master, text="Resume", command=self.resume_timer, width=10, bg="blue",
                                    fg="white", state="disabled")
        self.resume_button.pack(pady=5)

    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_button.config(state="disabled")
            self.stop_button.config(state="normal")
            self.pause_button.config(state="normal")
            self.resume_button.config(state="disabled")
            self.timer_thread = threading.Thread(target=self.run_timer)
            self.timer_thread.daemon = True
            self.timer_thread.start()

    def stop_timer(self):
        self.running = False
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.pause_button.config(state="disabled")
        self.resume_button.config(state="disabled")

    def pause_timer(self):
        self.running = False
        self.pause_button.config(state="disabled")
        self.resume_button.config(state="normal")

    def resume_timer(self):
        self.running = True
        self.resume_button.config(state="disabled")
        self.pause_button.config(state="normal")
        self.timer_thread = threading.Thread(target=self.run_timer)
        self.timer_thread.daemon = True
        self.timer_thread.start()

    def run_timer(self):
        interval = int(self.interval_entry.get()) * 60
        while self.running:
            time.sleep(interval)
            if self.running:
                self.master.after(0, self.show_reminder)

    def show_reminder(self):
        reminder_window = Toplevel(self.master)
        reminder_window.title("Time for a Break!")
        reminder_window.geometry("400x300")
        reminder_window.resizable(False, False)

        label = Label(reminder_window, text="Look at something 20 feet away\nfor 20 seconds!", font=("Arial", 16),
                      wraplength=380, justify="center")
        label.pack(pady=20)

        countdown_label = Label(reminder_window, text=f"{DEFAULT_COUNTDOWN_DURATION} seconds remaining",
                                font=("Arial", 14), fg="blue")
        countdown_label.pack()

        def countdown():
            for i in range(DEFAULT_COUNTDOWN_DURATION, 0, -1):
                countdown_label.config(text=f"{i} seconds remaining")
                reminder_window.update()
                time.sleep(1)
            reminder_window.destroy()

        self.master.after(0, countdown)
        winsound.Beep(1000, 500)

    def save_settings(self):
        settings = {"interval": self.interval_entry.get()}
        with open("settings.json", "w") as f:
            json.dump(settings, f)

    def load_settings(self):
        try:
            with open("settings.json", "r") as f:
                settings = json.load(f)
                self.interval_entry.delete(0, "end")
                self.interval_entry.insert(0, settings["interval"])
        except FileNotFoundError:
            pass

    def on_close(self):
        self.save_settings()
        self.master.destroy()


if __name__ == "__main__":
    root = Tk()
    app = BreakReminderApp(root)
    root.mainloop()