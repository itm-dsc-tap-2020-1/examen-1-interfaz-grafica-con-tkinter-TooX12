import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
from tkinter import scrolledtext


def salir():
    ventana.quit()
    ventana.destroy
    exit()

def label(text,row, column):
        ttk.Label(ventana, text=text).grid(row=row, column=column)
        
def calificarEx():
    if(p1.get() and p2.get() and p3.get() and p4.get()):
        label(" Completo ",10,0)
        cont=0
        if(p1.get()=="Miguel"): cont+=20
        if(p2.get()=="Quijote"): cont+=20
        if(p3.get()=="1"): cont+=20
        if(p4.get()=="2"): cont+=20
        if(p5_1.get()==1 or p5_2.get()==1 and p5_3.get()==0 and p5_4.get()==0 and p5_5.get()==0): cont+=20
        label("Calificacion"+str(cont),11,0)
    else:
        label("Imcompleto",10,0)
ventana = tk.Tk()
ventana.title('Sistema')
tabControl=ttk.Notebook(ventana)

barra_menu=Menu(ventana)
ventana.config(menu=barra_menu)
opciones_menu=Menu(barra_menu)
opciones_menu.add_command(label="Salir", command= salir)
barra_menu.add_cascade(label="Principal", menu=opciones_menu)
#Label
label("¿Autor del libro Don QUijote?",0,0)
label("¿Principal persona del libro Don QUijote?",1,0)
label('Cantidad de autores en el libro Don Quijote:',2,0)
label('Cantidad de paginas del libro Don Quijore',4,0)
label('Menciona 1 o 2 personajes del libro Don Quijote',6,0)
p1 = tk.StringVar()
p1_c= ttk.Entry(ventana, width=24, textvariable=p1)
p1_c.grid(row=0, column=1)

p2 = tk.StringVar()
p2_c= ttk.Entry(ventana, width=24, textvariable=p2)
p2_c.grid(row=1, column=1)

p3=tk.StringVar()
radiop3_1=tk.Radiobutton(ventana, text="1", variable=p3, value="1")
radiop3_1.grid(row=3, column=0)

radiop3_2=tk.Radiobutton(ventana, text="2", variable=p3, value="2")
radiop3_2.grid(row=3, column=1)

radiop3_3=tk.Radiobutton(ventana, text="3", variable=p3, value="3")
radiop3_3.grid(row=3, column=2)

radiop3_3.select()

p4=tk.StringVar()
radiop4_1=tk.Radiobutton(ventana, text="785", variable=p4, value="785")
radiop4_1.grid(row=5, column=0)

radiop4_2=tk.Radiobutton(ventana, text="945", variable=p4, value="945")
radiop4_2.grid(row=5, column=1)

radiop4_3=tk.Radiobutton(ventana, text="1150", variable=p4, value="1150")
radiop4_3.grid(row=5, column=2)

radiop4_1.select()

p5_1= tk.IntVar()
checkb1=tk.Checkbutton(ventana, text="Quijote", variable=p5_1, state='normal')
checkb1.grid(row=7, column=0)
checkb1.select()
p5_2=tk.IntVar()
checkb2=tk.Checkbutton(ventana, text="Sancho", variable=p5_2, state="normal")
checkb2.grid(row=7, column=1)
checkb2.deselect()
p5_3=tk.IntVar()
checkb3=tk.Checkbutton(ventana, text="Celestina", variable=p5_3, state='normal')
checkb3.grid(row=7, column=2)
checkb3.deselect()
p5_4=tk.IntVar()
checkb3=tk.Checkbutton(ventana, text="Artemis", variable=p5_4, state='normal')
checkb3.grid(row=7, column=3)
checkb3.deselect()
p5_5=tk.IntVar()
checkb3=tk.Checkbutton(ventana, text="Zed", variable=p5_5, state='normal')
checkb3.grid(row=7, column=4)
checkb3.deselect()

calificar=ttk.Button(ventana, text="Calificar", command=calificarEx).grid(row=8, column=1)

ventana.mainloop()