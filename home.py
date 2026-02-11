import tkinter as tk
import calendario

#ventana de inicio
def ventana_inicio():
    print("Home")
    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana principal")

    frame_botones = tk.Frame(ventana_principal)
    frame_botones.pack(side=tk.TOP, fill=tk.X, pady=5)


    boton_1 = tk.Button(frame_botones, text="Inicio", height=2, width=45, bg="skyblue").pack(side=tk.LEFT, pady= 5)
    boton_2 = tk.Button(frame_botones, text="Asignador de tareas", height=2, width=45, bg="skyblue").pack(side= tk.LEFT, padx=5, pady=5)
    boton_3 = tk.Button(frame_botones,text="Bandeja de dudas", height=2, width=45, bg="skyblue").pack(side=tk.LEFT, padx=10, pady=5)
    boton_4 = tk.Button(frame_botones, text="Generador de actividades", height=2, width=45, bg="skyblue").pack(side=tk.LEFT, padx=15, pady=5)

    

    app = calendario.Calendario(ventana_principal, 2026, 2, "#595A5A", "#BDBDBD")


    ventana_principal.mainloop()

ventana_inicio()
