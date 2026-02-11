import tkinter as tk    
from tkinter import messagebox,ttk, simpledialog
import calendario
import datetime


ahora = datetime.datetime.now()
print ("fecha y hora actual:", ahora)

hoy = datetime.datetime.today()



#ventana de inicio
def ventana_inicio_sesion():
    print("Inicio de sesión")
    ventana_principal_maestro = tk.Tk()
    app = calendario.Calendario(ventana_principal_maestro, ahora.year, ahora.month, "#C7FCEF", "#BDBDBD")

    

#venana login
def abrir_login(rol):
    ventana_inicial.destroy()
    login=tk.Tk()
    
    login.title(f'login - {rol}')
    login.geometry("300x200")

    
    tk.Label(login, text=f"Entrar como {rol}", font=("Arial, 14")).pack(pady=5)
    tk.Label(login, text="usuario").pack(pady=8)
    usuario_entry=tk.Entry(login)
    usuario_entry.pack()


    tk.Label(login, text="contraseña").pack(pady=8)
    usuario_contra=tk.Entry(login, show="*")
    usuario_contra.pack()

    #validación de datos
    def validar():
        usuario = usuario_entry.get()
        contra = usuario_contra.get()

        if usuario == "admin" and contra == "admin":
            login.destroy()
            ventana_inicio_sesion()
        else:
            print("Lo siento, usuario incorrecto")

        print(usuario)
        print(contra)

    tk.Button(
        login, 
        text="Iniciar sesión", 
        command=validar
).pack(pady=15)



    login.mainloop()
    




#ventana inicial
ventana_inicial=tk.Tk()
ventana_inicial.title("punto educativo")
ventana_inicial.geometry("350x400")

tk.Label(ventana_inicial, text="Bienvenido al sistema de punto educativo", font=("Arial",12)).pack(pady=60)


tk.Button(
    ventana_inicial,
    text="Iniciar como estudiante",
    width=60,
    height=5,
    command= lambda: abrir_login("estudiante")
).pack(pady=5)


tk.Button(
    ventana_inicial, 
    text="Iniciar como maestro",
    width=60,
    height=5,
    command= lambda: abrir_login("  Maestro")
).pack(pady=5)

tk.Label(ventana_inicial, text="Elaborado por Luis", font=("Arial", 10)).pack(pady=5)
ventana_inicial.mainloop()
