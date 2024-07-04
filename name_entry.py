import tkinter as tk

window = tk.Tk()
window.title("App")
window.geometry("400x250")

font = ("Arial", 18)
padx = 10
pady = 10

title = tk.Label(
    text="Enter your name",
    font=font,
    padx=padx,
    pady=pady
)
title.pack()


def showName():
    greeting["text"] = "Hello " + entry.get() + "!"
    # greeting["text"] = f"Hello {entry.get()}!"


entry = tk.Entry(
    font=font
)
entry.pack(padx=padx, pady=pady)

button = tk.Button(
    text="SUBMIT",
    font=font,
    command=showName,
    padx=padx,
    pady=pady
)
button.pack()

greeting = tk.Label(
    text="",
    font=font,
    padx=padx,
    pady=pady
)
greeting.pack()

window.mainloop()
