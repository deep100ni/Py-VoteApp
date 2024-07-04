import tkinter as tk

window = tk.Tk()

post="Head boy"
candidates=["Alpha", "Beta", "Gamma"]

font = ("Arial", 18)
padx = 10
pady = 10

title = tk.Label(
    text=f"Vote your {post}",
    font=font,
    padx=padx,
    pady=pady
)
title.pack()


def setChoice(c):
    choice["text"] = c


for candidate in candidates:
    button = tk.Button(
        text=candidate,
        font=font,
        command=lambda c=candidate: setChoice(c),
        padx=padx,
        pady=pady
    )
    button.pack()


choice = tk.Label(
    text="",
    font=font,
    padx=padx,
    pady=pady
)
choice.pack()


window.mainloop()