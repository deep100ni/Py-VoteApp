import json
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def read_candidates(file_path='candidates.json'):
    with open(file_path, 'r') as file:
        candidates = json.load(file)
    return candidates


# Post -> Candidate dict
data = read_candidates()

# To save user votes
selected = {}

# Denotes current page
curr = -1

# Create Tkinter window
window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width / 2 - 500 / 2)
center_y = int(screen_height / 2 - 500 / 2)
window.geometry(f"500x500+{center_x}+{center_y}")

# Main frame
frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# General settings
font = ("Arial", 18)
padx = 10
pady = 10

# Global variables to use in functions
adm_no_entry: tk.Entry
title_lbl: tk.Label
choices_fr: tk.Frame
buttons_fr: tk.Frame

# admission number range
adm_no_start = 1
adm_no_end = 4000

# current adm_no
adm_no = 0


def show_adm_no_input():
    global frame, adm_no_entry

    clear_window()

    # Title
    enter_lbl = tk.Label(
        master=frame,
        text="Enter your admission no.",
        font=font,
        padx=padx,
        pady=pady
    )
    enter_lbl.pack()

    # Entry for adm_no
    adm_no_entry = tk.Entry(
        master=frame,
        font=font
    )
    adm_no_entry.pack(padx=padx, pady=pady)

    start_btn = ttk.Button(master=frame, text="START", command=start)
    start_btn.pack(padx=padx, pady=pady)


def adm_no_valid():
    global adm_no

    adm_no = int(adm_no_entry.get())

    if adm_no not in range(adm_no_start, adm_no_end + 1):
        messagebox.showerror("Invalid", "Admission number is invalid")
        return False

    adm_nos = json.load(open("adm_nos.json", "r"))
    already_voted = adm_no in adm_nos

    if already_voted:
        messagebox.showerror("Illegal", "You have already voted")
        return False

    return True


# Starts / Restarts the vote
def start():
    global selected, curr

    if not adm_no_valid(): return

    # Reset progress
    selected = {}
    curr = -1

    clear_window()

    display_base_layout()
    display_buttons_layout()

    # shows first page
    next_page()


def display_base_layout():
    global window, frame, title_lbl, choices_fr, buttons_fr

    # Shows "Vote your {post}"
    title_lbl = tk.Label(
        master=frame,
        font=font,
        padx=padx,
        pady=pady
    )
    title_lbl.pack()

    # To show candidate buttons
    choices_fr = tk.Frame(frame)
    choices_fr.pack(padx=padx, pady=pady, fill=tk.Y)

    # To show prev, next & submit buttons
    buttons_fr = tk.Frame(frame)
    buttons_fr.pack(padx=padx, pady=pady)


def next_page():
    global curr, data

    # Get current post
    posts = list(data.keys())

    # Incomplete check
    if curr > -1 and posts[curr] not in selected:
        messagebox.showerror("Incomplete", "Please vote first!")
        return False

    curr = curr + 1
    post = posts[curr]
    candidates = data[post]
    display(post, candidates)


def prev_page():
    global curr, data

    posts = list(data.keys())
    curr = curr - 1
    post = posts[curr]
    candidates = data[post]
    display(post, candidates)


def display_buttons_layout():
    global buttons_fr

    # Clear buttons frame
    for child in buttons_fr.winfo_children():
        child.destroy()

    # Find out last page
    last = len(data.keys()) - 1

    # Show prev_btn if not on first page
    if curr > 0:
        prev_btn = ttk.Button(master=buttons_fr, text="<<", command=prev_page)
        prev_btn.grid(row=0, column=0, sticky="nsew", padx=padx, pady=pady)

    # Show next_btn if not on last page
    if curr < last:
        next_btn = ttk.Button(master=buttons_fr, text=">>", command=next_page)
        next_btn.grid(row=0, column=1, sticky="nsew", padx=padx, pady=pady)

    # Show submit_btn if last page
    elif curr == last:
        submit_btn = ttk.Button(master=buttons_fr, text="SUBMIT", command=submit)
        submit_btn.grid(row=0, column=2, sticky="nsew", padx=padx, pady=pady)


def display(post, candidates):
    global title_lbl, choices_fr

    # Set title
    title_lbl["text"] = f"Vote your {post}"

    # To select a candidate
    def setChoice(c):
        for i, child in enumerate(choices_fr.winfo_children()):
            if i == c:
                # Save vote
                selected[post] = child["text"]
                child["background"] = "blue"
                child["foreground"] = "white"
            else:
                child["background"] = "white"
                child["foreground"] = "black"

    # Clear previous post's candidates
    for child in choices_fr.winfo_children():
        child.destroy()

    # Get already voted candidate
    vote = ""
    if post in selected:
        vote = selected[post]

    # Display candidates
    for i, candidate in enumerate(candidates):
        if vote == candidate:
            background = "blue"
            foreground = "white"
        else:
            background = "white"
            foreground = "black"

        # Button for candidate
        button = tk.Button(
            master=choices_fr,
            text=candidate,
            font=font,
            command=lambda c=i: setChoice(c),
            padx=padx,
            pady=pady,
            background=background,
            foreground=foreground
        )
        button.pack(padx=5, pady=5, fill=tk.X)

    display_buttons_layout()


def save_zero_votes():
    votes = {}
    for (post, candidates) in data.items():
        votes[post] = {}
        for candidate in candidates:
            votes[post][candidate] = 0
    json.dump(votes, open("votes.json", "w"))


def submit():
    post = list(data.keys())[curr]

    # Incomplete check
    if post not in selected:
        messagebox.showerror("Incomplete", "Please vote first!")
        return False

    votes = json.load(open("votes.json", "r"))
    for (post, vote) in selected.items():
        no_of_votes = votes[post][vote]
        votes[post][vote] = no_of_votes + 1

    json.dump(votes, open("votes.json", "w"), indent=4)

    finish_vote()


def save_adm_no():
    adm_nos = json.load(open("adm_nos.json", "r"))
    adm_nos.append(adm_no)
    json.dump(adm_nos, open("adm_nos.json", "w"))


def finish_vote():
    global frame

    clear_window()

    save_adm_no()

    thanks_lbl = tk.Label(
        master=frame,
        text="Thank you",
        font=font,
        padx=padx,
        pady=pady
    )
    thanks_lbl.pack()

    start_btn = ttk.Button(master=frame, text="START AGAIN", command=show_adm_no_input)
    start_btn.pack()


def clear_window():
    for child in frame.winfo_children():
        child.destroy()


show_adm_no_input()

window.mainloop()
