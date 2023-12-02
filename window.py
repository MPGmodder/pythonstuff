import tkinter
import tkinter as tk

window = tk.Tk()
window.title("hello")
label = tkinter.Label(window, text="you can type here.", font = ('arial', 18))
label.pack()
TB = tk.Text(window, font=('arial', 18))
TB.pack()
window.geometry("250x250")
window.mainloop()