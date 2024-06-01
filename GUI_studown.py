import tkinter as tk
import os

def shutdown_computer():
    os.system("shutdown /s /t 1")  # Shutdown command

root = tk.Tk()
root.title("Shutdown Computer")

# Create a button to initiate shutdown
shutdown_button = tk.Button(root, text="Shutdown", command=shutdown_computer)
shutdown_button.pack(pady=20)

root.mainloop()