from tkinter import * #importamos la librería tkinter, * significa importar todo

#creamos la ventana principal
app = Tk()
#titulo de la ventana
app.title("Mi primera app con Tkinter")
#tamaño de la ventana
app.geometry("400x300")

#crear un objeto frame
frame = Frame(app) #el frame es un contenedor dentro de la ventana principal
frame.grid(row=0,column=0) #ubicamos el frame en la ventana con grid




#mostramos la ventana
app.mainloop() #mantiene la ventana abierta y en espera de eventos
