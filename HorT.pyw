import random as rd
import tkinter as tk
import time

with open('count.txt', 'r+') as f:
    try:
        count = f.read()
        count = int(count)
    except Exception as e:
        print(e)
        count = 0

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    res = (rd.randint(0,1))
    if res == 0:
        resL = tk.Label(frame, text='Heads')
    else:
        resL = tk.Label(frame, text='Tails')
    resL.pack()

    count += 1
    CLab = tk.Label(frame, text='Times rolled: ' + str(count))
    CLab.pack()

    f.seek(0)
    f.truncate(0)
    f.write(str(count))

    root.after(2000, root.destroy)
    root.mainloop()