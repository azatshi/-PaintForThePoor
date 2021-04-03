from tkinter import *

canvas_width = 700
canvas_height = 500
brush_size = 3
color = "black"

def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    w.create_oval(x1, y1, x2, y2,
                  fill=color, outline=color)

def brish_size_change(new_size):
    global brush_size
    brush_size = new_size

def color_change (new_color):
    global color
    color = new_color

def up_change_size (next_size):
    global brush_size
    brush_size += next_size

def down_change_size (next_size):
    global brush_size
    if brush_size > 6:
        brush_size -= next_size
    
def paste_text():
    global object_id

    object_id = w.create_text(30, 10, text = text.get())

def click(event):
    if object_id is not None:
        w.coords(object_id, event.x, event.y)
    
root = Tk()
root.title("Paint для бедных")

w = Canvas(root,
           width=canvas_width,
           height=canvas_height,
           bg="white")
w.bind("<B1-Motion>", paint)

red_btn = Button(text ="Красный", width=10,
                 command=lambda: color_change("red"))

black_btn = Button(text ="Черный", width=10,
                 command=lambda: color_change("black"))

blue_btn = Button(text ="Синий", width=10,
                 command=lambda: color_change("blue"))

white_btn = Button(text ="Ластик", width=10,
                 command=lambda: color_change("white"))

clear_btn = Button(text="Удалить всё", width=10,
                   command=lambda: w.delete("all"))

size_down_btn = Button(text="Изменить <", width=10,
                  command=lambda: down_change_size(5))

size_up_btn = Button(text="Изменить >", width=10,
                  command=lambda: up_change_size(5))

text = StringVar()
e1 = Entry(width=50, textvariable=text)
text_btn = Button(text="Текст", width=10,
                  command=paste_text)

w.bind("<Button-3>", click)

w.grid(row=2, column=0,
       columnspan=7, padx=5,
       pady=5, sticky=E+W+S+N)
w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)

red_btn.grid(row=0, column=0)
black_btn.grid(row=0, column=1)
blue_btn.grid(row=0, column=2)
clear_btn.grid(row=0, column=3)
size_down_btn.grid(row=1, column=0)
size_up_btn.grid(row=1, column=1)
white_btn.grid(row=1, column=2)
text_btn.grid(row=1, column=3)
e1.grid(row=1, column=4)
root.mainloop()
