import tkinter as tk


window = tk.Tk()
label = tk.Label(
    text="Python label with text",
    fg="white",
    bg="black",
    height="300"
    )
label.pack()

window.mainloop()