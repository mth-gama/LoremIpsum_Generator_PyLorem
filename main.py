from tkinter import *
import tkinter as tk
from Functions import *
import pyautogui as pg
import lorem

# Variables
color01 = '#5D5D5D'  # grey
color02 = '#7EC81A'  # green
color03 = '#FEFEFE'  # white
# ////////////////////////////////END
# Windowns config
root = Tk()
root.geometry(center(root, 700, 600))
root.config(bg=color01)
root.title('PyLorem')
root.resizable(False, False)
# ////////////////////////////////END
# Variables
img_logo = PhotoImage(file=r'img\img_logo.png')
img_button = PhotoImage(file=r'img\img_button_gerator.png')
# ////////////////////////////////END
# Functions


def gerate_lorem():
    s = lorem.sentence()
    p = lorem.paragraph()
    t = lorem.text()
    tx_campo_text.delete("1.0", "end")
    tx_campo_text.insert(tk.END, p)


# Containers
fr_container01_top = Frame(
    root,
    bg=color01,
    width=700,
    height=100
)
fr_container02_mid = Frame(
    root,
    bg=color01,
    width=700,
    height=400
)
fr_container03_bot = Frame(
    root,
    bg=color01,
    width=700,
    height=100
)
fr_container01_top.grid_propagate(0)
fr_container02_mid.grid_propagate(0)
fr_container03_bot.grid_propagate(0)
fr_container01_top.grid(row=0, column=0)
fr_container02_mid.grid(row=1, column=0)
fr_container03_bot.grid(row=2, column=0)

# ////////////////////////////////END
# Labels
# Container 01
lb_title = Label(
    fr_container01_top,
    image=img_logo,
    bg=color01
)
lb_title.grid(row=0, column=0, padx=135, pady=40)
# ////////////////////////////////END
# Container 02
btn_gerate = Button(
    fr_container02_mid,
    image=img_button,
    bd=0,
    bg=color01,
    activebackground=color01,
    command=gerate_lorem
)
fr_row_top = Frame(
    fr_container02_mid,
    width=452,
    height=2,
    bg=color02
)
tx_campo_text = Text(
    fr_container02_mid,
    width=50,
    height=15,
    font='Bebas 12',
    bg=color03,
    bd=0,

)
fr_row_bot = Frame(
    fr_container02_mid,
    width=452,
    height=2,
    bg=color02
)

btn_gerate.grid(row=3, column=0, sticky=E, pady=15, padx=135)
fr_row_top.grid(row=0, column=0, padx=135, pady=2)
tx_campo_text.grid(row=1, column=0, padx=135)
fr_row_bot.grid(row=2, column=0, padx=135, pady=2)
# ////////////////////////////////END
# Container 03
lb_boot = Label(
    fr_container03_bot,
    text='Developed by: mth_gama',
    bg=color01,
    fg=color02,
    font='Calibri 12 italic'
)
lb_boot.grid(row=0, column=0, padx=135, sticky=N)
# root in mainloop
tk.mainloop()
