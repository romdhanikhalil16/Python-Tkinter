from tkinter import *



fenetre = Tk()
Label(fenetre,text="Hello world",bg="yellow").pack()


poids=Entry(fenetre,text="entrez votre poids")
poids.pack()


taille=Entry(fenetre,text="entrez votre taille")
taille.pack()

res = DoubleVar()
resultat=Label(fenetre,text="la IMC :",textvariable=res)
resultat.pack()

message=StringVar()
Label(fenetre,text="note : ",textvariable=message).pack()


def calcul():
    
    totale = float(poids.get())/float(taille.get())
    res.set(totale)
    if totale<18.5:
        message.set("Insuffisance pondérale (maigreur)")
    elif totale>= 18.5 and totale<=25:
        message.set("corpulence normale")
    elif totale>25 and totale<=30:
        message.set("surpoids")
    elif totale> 30 and totale<=35:
        message.set("Obésité modérée")
    elif totale>35 and totale<=40:
        message.set("Obésité sévère")
    elif totale>40:
        message.set("Obésité morbide ou massive")
        
    


        
btn = Button(fenetre,text="calculer",command=calcul)
btn.pack()



fenetre.mainloop()
