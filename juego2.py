import random
import tkinter as tk

# 1. CREAMOS LA VENTANA PRINCIPAL (Antes llamada 'root')
ventana_principal = tk.Tk()
ventana_principal.title("Piedra, Papel o Tijeras")
ventana_principal.geometry("380x400")
ventana_principal.configure(bg="gray15")

PUNTAJE = {"Jugador": 0, "CPU": 0}
OPCIONES = {"Piedra": "🪨", "Papel": "📄", "Tijeras": "✂️"}

# FRAME 1: MARCADOR (Va metido dentro de 'ventana_principal')
frame_marcador = tk.Frame(ventana_principal, bg="gray25", pady=10)
frame_marcador.pack(fill="x", padx=10, pady=10)

texto_puntos = tk.Label(
    frame_marcador, 
    text="Jugador: 0  |  CPU: 0", 
    font=("Arial", 14, "bold"), 
    bg="gray25", 
    fg="azure"
)
texto_puntos.pack()

# FRAME 2: MESA DE JUEGO (Va metida dentro de 'ventana_principal')
frame_resultado = tk.Frame(ventana_principal, bg="gray15")
frame_resultado.pack(pady=15)

texto_versus = tk.Label(
    frame_resultado, 
    text="❓ vs ❓", 
    font=("Arial", 30), 
    bg="gray15", 
    fg="white"
)
texto_versus.pack()

texto_mensaje = tk.Label(
    frame_resultado, 
    text="¡Haz tu jugada!", 
    font=("Arial", 12), 
    bg="gray15", 
    fg="light gray"
)
texto_mensaje.pack(pady=5)

# LÓGICA DEL JUEGO
def jugar(eleccion_jugador):
    eleccion_cpu = random.choice(list(OPCIONES.keys()))
    texto_versus.config(text=f"{OPCIONES[eleccion_jugador]} vs {OPCIONES[eleccion_cpu]}")

    if eleccion_jugador == eleccion_cpu:
        res, col = "¡Empate!", "gold"
    elif (eleccion_jugador == "Piedra" and eleccion_cpu == "Tijeras") or \
        (eleccion_jugador == "Papel" and eleccion_cpu == "Piedra") or \
        (eleccion_jugador == "Tijeras" and eleccion_cpu == "Papel"):
        res, col = "¡Ganaste!", "lawn green"
        PUNTAJE["Jugador"] += 1
    else:
        res, col = "Gana CPU", "tomato"
        PUNTAJE["CPU"] += 1

    texto_mensaje.config(text=res, fg=col)
    texto_puntos.config(text=f"Jugador: {PUNTAJE['Jugador']}  |  CPU: {PUNTAJE['CPU']}")

# FRAME 3: BOTONES (Va metido dentro de 'ventana_principal')
frame_botones = tk.Frame(ventana_principal, bg="gray15")
frame_botones.pack(pady=10)

for nombre, emoji in OPCIONES.items():
    boton = tk.Button(
        frame_botones, 
        text=f"{emoji}\n{nombre}", 
        font=("Arial", 10, "bold"), 
        width=8, 
        bg="slate gray", 
        fg="white", 
        activebackground="sky blue", 
        command=lambda n=nombre: jugar(n)
    )
    boton.pack(side="left", padx=5)

# INICIAMOS EL BUCLE DE LA VENTANA
ventana_principal.mainloop()