from tkinter import *
from tkinter import messagebox
import random
from random import randint
import time
import threading

root=Tk()
root.withdraw()
root.attributes("-alpha", 0)
root.overrideredirect(1)
root.attributes("-topmost", 1)

messagebox.showerror('System Error', 'Application that you tried to open crashed')
def placewindows():
 while True:
          win = Toplevel(root)
          win.geometry("300x60+" + str(randint(0, root.winfo_screenwidth() - 300)) + "+" + str(randint(0, root.winfo_screenheight() - 60)))
          win.overrideredirect(1)
          Label(win, text="You Are Hacked", bg='black', fg="red").place(relx=.38, rely=.3)
          win.lift()
          win.attributes("-topmost", True)
          win.attributes("-topmost", False)
          root.lift()
          root.attributes("-topmost", True)
          root.attributes("-topmost", False)
         # time.sleep(.05)

threading.Thread(target=placewindows).start()

root.mainloop()

root.deiconify()
root.destroy()
root.quit()
