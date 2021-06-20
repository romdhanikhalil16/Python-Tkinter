from tkinter import *
import random

app = Tk()
Label(app,text="exercice 2").pack()

aleaNumber = random.randint(1,6)

val=DoubleVar()
Label(app,textvariable=val).pack()
def fct():
    val.set(aleaNumber)
btn=Button(app,text="nombre aleatoire",command=fct).pack()
btn=Button(app,text="exit",command=app.destroy).pack()

app.mainloop()
