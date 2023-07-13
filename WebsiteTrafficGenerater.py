import tkinter as tk
from tkinter import font
from tkinter.scrolledtext import ScrolledText
import subprocess
import threading

def generate_views():
    website = website_entry.get()
    threads = 10
    max_clicks = max_clicks_entry.get()
    min_clicks = 2
    proxy_file = 'proxies.txt'
    timeout = 60
    max_offset = 10


    # Construct the command with the provided inputs
    command = f"python main.py -d {website} --forever --threads {threads} --max-clicks {max_clicks} --min-clicks {min_clicks} --forever --proxy-file {proxy_file} --timeout {timeout} --max-offset {max_offset}"

    # Execute the command in a separate thread
    threading.Thread(target=execute_command, args=(command,), daemon=True).start()

    # Clear the entry fields
    website_entry.delete(0, tk.END)
    max_clicks_entry.delete(0, tk.END)
    bounce_rate_entry.delete(0, tk.END)
    time_spent_entry.delete(0, tk.END)


def execute_command(command):
    # Execute the command
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
        text=True
    )

    # Read and display the output in the text area
    while process.poll() is None:
        line = process.stdout.readline()
        terminal_output.insert(tk.END, line)
        terminal_output.see(tk.END)


visited_count = 0
new_count = 0

root = tk.Tk()
root.title("Website Views Generator")
root.configure(bg="#f0f0f0")

title_font = font.Font(family="Arial", size=16, weight="bold")
label_font = font.Font(family="Calibri", size=12)
button_font = font.Font(family="Helvetica", size=12, weight="bold")

# Create and position the desired bounce rate label and entry
bounce_rate_label = tk.Label(root, text="Desired Bounce Rate:", font=title_font, fg="purple", bg="#f0f0f0")
bounce_rate_label.pack()
bounce_rate_entry = tk.Entry(root, font=label_font, bg="white")
bounce_rate_entry.pack()

# Create and position the time spent label and entry
time_spent_label = tk.Label(root, text="Time Spent on Each Visited Site:", font=title_font, fg="purple", bg="#f0f0f0")
time_spent_label.pack()
time_spent_entry = tk.Entry(root, font=label_font, bg="white")
time_spent_entry.pack()

website_label = tk.Label(root, text="Website:", font=title_font, fg="purple", bg="#f0f0f0")
website_label.pack()
website_entry = tk.Entry(root, font=label_font, bg="white")
website_entry.pack()

max_clicks_label = tk.Label(root, text="Maximum Number of Clicks:", font=title_font, fg="purple", bg="#f0f0f0")
max_clicks_label.pack()
max_clicks_entry = tk.Entry(root, font=label_font, bg="white")
max_clicks_entry.pack()

generate_button = tk.Button(root, text="Generate Views", font=button_font, command=generate_views, fg="white", bg="green")
generate_button.place(x=10, y=50)  # Adjust the coordinates to position the button

instructions = tk.Button(root, text="Please read instructions", font=button_font, command=lambda: subprocess.Popen(["python", "instructions.py"], shell=True), fg="white", bg="green")
instructions.place(x=10, y=100)  # Adjust the coordinates to position the button

terminal_frame = tk.Frame(root, bg="#f0f0f0")
terminal_frame.pack(fill=tk.BOTH, expand=True)

terminal_label = tk.Label(terminal_frame, text="Terminal Output:", font=title_font, fg="purple", bg="#f0f0f0")
terminal_label.pack()

terminal_output = ScrolledText(terminal_frame, font=label_font, bg="white")
terminal_output.pack(fill=tk.BOTH, expand=True)

emulate_button = tk.Button(root, text="Emulate Mouse Moves", font=button_font, command=lambda: subprocess.Popen(["python", "MouseX.py"], shell=True),bg="blue")
emulate_button.place(x=10, y=10)  # Position the button at the top-left corner

root.mainloop()
