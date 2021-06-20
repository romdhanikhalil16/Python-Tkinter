from tkinter import *
from tkinter import messagebox

app=Tk()
Label(app,text="saisie votre mot de passe").pack()

mdp = Entry(app)
mdp.pack()
def fctVerif():
    val = mdp.get()
    if val == "isetmdp":
        print("great")
        messagebox.askquestion("question","veuillez vous continuer ?")
    else:
        print("no please")
        messagebox.showinfo("verifier","veuillez verifier votre mot de passe s'il vous plait")
Button(app,text="verifier",command=fctVerif).pack()
app.mainloop()
