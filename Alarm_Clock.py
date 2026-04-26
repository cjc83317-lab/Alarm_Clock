import tkinter as tk
import time
import datetime
import threading


class AlarmClock:
    def __init__(self, master):
        self.master = master
        self.master.title("Alarm Clock")
        self.master.geometry("350x180")

        tk.Label(master, text="ALARM CLOCK", font=("Arial", 18, "bold"),fg="Green").pack(pady=10)

        frame = tk.Frame(master)
        frame.pack(pady=5)

        tk.Label(frame, text="Hour (00-23):").grid(row=0, column=0, padx=5)
        self.hour_entry = tk.Entry(frame, width=5)
        self.hour_entry.grid(row=0, column=1)
        
        tk.Label(frame, text="Minute (00-59):").grid(row=0, column=2, padx=5)
        self.minute_entry = tk.Entry(frame, width=5)
        self.minute_entry.grid(row=0, column=3)
        
        tk.Label(frame, text="Second (00-59):").grid(row=0, column=4, padx=5)
        self.second_entry = tk.Entry(frame, width=5)
        self.second_entry.grid(row=0, column=5)


        tk.Button(master, text="Set Alarm", command=self.start_thread, font=("Arial", 12)).pack(pady=15)
        
        # Status
        self.status_label = tk.Label(master, text="", font=("Arial", 12), fg="green")
        self.status_label.pack()
    
    def start_thread(self):
        t = threading.Thread(target=self.alarm)
        t.daemon = True
        t.start()
    
    def alarm(self):
        set_time = f"{self.hour_entry.get()}:{self.minute_entry.get()}:{self.second_entry.get()}"
        self.status_label.config(text=f"Alarm set for {set_time}")
        
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            if current_time == set_time:
                self.status_label.config(text="Wake up! Alarm ringing...")
                # Cross-platform beep
                self.master.bell()
                break
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmClock(root)
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("Program interrupted. Closing gracefully...")


    
        

