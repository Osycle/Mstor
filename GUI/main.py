from tkinter import *
import sys


import requests
import sys
from bs4 import BeautifulSoup as BS


color_1 = "#202b60"
color_2 = "#7fffd4"
color_3 = "#282934"

sys.stdout.reconfigure(encoding='utf-8')

root = Tk()

def btn_click():
  # quest  = quest.get()
  print("Нажал на кнопку")
  r = requests.get("https://marketing.uz/brend-goda-2021/")
  html = BS(r.content, "html.parser")
  sys.stdout.reconfigure(encoding='utf-8')
  row = 0
  col = 0
  for el in html.select(".votign-items > figure:not([class])"):
    cap = el.select(".cap-content span")[0].text
    row += 1
    if(row >= 5):
      col += 1
      row = 0
    cap_frame = Label(first_frame, text=cap, bg=color_1, font=15, fg=color_2,)
    cap_frame.grid(row=row, column=col)
    print(cap)

root['bg'] = color_3
root.title("Обзор Макона")
root.wm_attributes("-alpha", 1)
# root.wm_overrideredirect = 0
root.geometry("800x600")

# canvas = Canvas(root, height=800, width=600)
# canvas.pack()

title_frame = Label(root, text="Makon marketing", bg="gray", font=40, width=100)
textinput_frame = Entry(root, bg="white")
first_frame = Frame(root, bg=color_3)
first_frame.place(rely=0.20, relwidth=0.5, relheight=0.8)

button_frame = Button(root, 
  text="Вывести", 
  fg=color_1,
  bg="#ffffff", 
  command=btn_click)


title_frame.pack()
textinput_frame.pack()
button_frame.pack(side=BOTTOM)


root.mainloop()