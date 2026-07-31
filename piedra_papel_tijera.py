from tkinter import *
from tkinter import messagebox


ventana_principal = Tk()
ventana_principal.title("Piedra, Papel o Tijeras")
ventana_principal.geometry("380x400")
ventana_principal.config(bg="gray15")


PUNTAJE = {"Jugador": 0, "CPU": 0}
OPCIONES = {"Piedra": "🪨", "Papel": "📄", "Tijeras": "✂️"}


frame_marcador = Frame(ventana_principal)
frame_marcador.config(bg="gray15", width=380, height=80)
frame_marcador.place(x=0,y=0)


marcador = Label(frame_marcador, text="Jugador: 0 | 0 :Cpu")
marcador.config(bg="gray25", fg="white",font=("Arial",10,"bold"))
marcador.place(x=130,y=20)

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="gray55", width=380, height=150)
frame_resultados.place(x=0,y=80)

haz_tu_eleccion = Label(frame_resultados, text="¡Haz tu elección!")
haz_tu_eleccion.config(bg="gray25",fg="white",font=("Arial",16,"bold"))
haz_tu_eleccion.place(x=110,y=100)





ventana_principal.mainloop()