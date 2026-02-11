import tkinter as tk   


def asignaciones ():
    ventana_asign = tk.Tk()

    frame_detalles = tk.Frame(ventana_asign)
    frame_detalles.pack(side=tk.TOP, fill=tk.X, pady=15)


    tarea = tk.Label(frame_detalles, text="tarea", width=100).pack()
    tarea_entry = tk.Entry(frame_detalles, text="nombre de la tarea", width=100).pack()


    descripcion = tk.Label(frame_detalles, text="descripcion", width=100).pack()
    descripcion_entry = tk.Entry(frame_detalles, text="detalles", width=100).pack()


    punteo = tk.Label(frame_detalles, text="Ponderación", width=100).pack()
    punteo_entry = tk.Entry(frame_detalles, text="0-100", width=100).pack()

    ventana_asign. mainloop()

asignaciones()