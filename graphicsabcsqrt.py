from tkinter import *


counter = 0
w = Tk()
w.geometry('1920x1080')
can = Canvas(w, width = 1920, height = 1080, bg = 'black')
can.pack()
k_a = Entry()
k_a.place(x = 100, y = 900, width = 20)
k_b = Entry()
k_b.place(x = 100, y = 920, width = 20)
k_c = Entry()
k_c.place(x = 100, y = 940, width = 20)
can.create_line(960, 0, 960, 1080, fill = 'white', width = 2)
can.create_line(0, 540, 1920, 540, fill = 'white', width = 2)
can.create_text(75, 910, text= 'insert a', fill = 'white')
can.create_text(75, 930, text= 'insert b', fill = 'white')
can.create_text(75, 950, text= 'insert c', fill = 'white')
for i in range(1000):
    if i % 30 == 0:
        can.create_line(950, i, 970, i, fill = 'white')
for i in range(10000):
    if i % 30 == 0:
        can.create_line(i, 530, i, 550, fill = 'white')
    
    
def clear():
    global counter
    counter = 0
    can.delete('all')
    can.create_line(960, 0, 960, 1080, fill = 'white', width = 2)
    can.create_line(0, 540, 1920, 540, fill = 'white', width = 2)
    for i in range(1000):
        if i % 30 == 0:
            can.create_line(950, i, 970, i, fill = 'white')
    for i in range(10000):
        if i % 30 == 0:
            can.create_line(i, 530, i, 550, fill = 'white')
    can.create_text(75, 910, text= 'insert a', fill = 'white')
    can.create_text(75, 930, text= 'insert b', fill = 'white')
    can.create_text(75, 950, text= 'insert c', fill = 'white')


def click_button():
    global counter
    if counter == 3:
        clear()
        counter = 0
    if counter == 0:
        ctextx = 1500
        ctexty = 900
        col = 'white'
    elif counter == 1:
        ctextx = 1500
        ctexty = 200
        col = 'pink'
    elif counter == 2:
        ctextx = 200
        ctexty = 200
        col = 'cyan'
    counter += 1
    closer = True
    a = float(k_a.get())
    b = float(k_b.get())
    c = float(k_c.get())
    print(counter)
    if a != 0:
        xv = -(b / (2 * a))
        yv = a*xv**2 + xv * b + c
        can.create_text(ctextx, ctexty, text= 'x вершины: ' + str(xv) + '\n' + 'y вершины: ' + str(yv), fill = col)
        x0 = str((-(b) + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))
        x01 = str((-(b) - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))
        can.create_text(ctextx, ctexty - 50, text= 'точка пересечения с 0Y: ' + str(c), fill = col)
    for i in range(-10000, 10000):
        x = i / 1000
        y = a*x**2 + x * b + c
        can.create_oval(960 + x * 30, 540 - y * 30, x * 30 + 961, 541 - y * 30, fill = col, outline = col)
        if (yv > 0 and y < 0) or (yv < 0 and y > 0)  and closer:
            closer = False
            can.create_text(ctextx, ctexty - 30, text='точка пересечения с 0X: '  + str(x0) + ', ' + str(x01), fill = col)


btn = Button(text='CREATE CHART', background='#000', foreground='#0c0',
             padx='20', pady='8', font='16', highlightcolor = '#0cc', command=click_button)
btn.place(x = 200, y = 900)
btn_clear = Button(text='CLEAR', background='#000', foreground='#f00',
             padx='20', pady='8', font='16', highlightcolor = '#0cc', command=clear)
btn_clear.place(x = 200, y = 950)

w.mainloop()
