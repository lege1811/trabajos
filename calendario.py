import tkinter as tk
from tkinter import simpledialog
import calendar



class Calendario:
    def __init__(self, root, year, month, bgcolor, bglcolor):
        self.root = root
        self.root.title("Calendario - Febrero 2026")

        self.year = year
        self.month = month
        self.eventos = {(2026, 2, 9): "Tarea 1"}
        self.bgcolor = bgcolor
        self.bglcolor = bglcolor

        self.cal = calendar.monthcalendar(self.year, self.month)

        self.frame = tk.Frame(self.root, padx=10, pady=10, bg=self.bgcolor)
        self.frame.pack()

        self.crear_calendario()

    def crear_calendario(self):
        # Título
        titulo = f"{calendar.month_name[self.month]} {self.year}"
        tk.Label(self.frame, text=titulo, font=("Arial", 16, "bold"),bg=self.bgcolor).grid(row=0, column=0, columnspan=7, pady=10)

        # Días de la semana
        dias = ["L", "M", "M", "J", "V", "S", "D"]
        for col, dia in enumerate(dias):
            tk.Label(self.frame, text=dia, font=("Arial", 10, "bold"),bg=self.bgcolor).grid(row=1, column=col)

        # Días del mes
        for fila, semana in enumerate(self.cal, start=2):
            for col, dia in enumerate(semana):
                if dia == 0:
                    tk.Label(self.frame, text="", bg=self.bgcolor).grid(row=fila, column=col)
                else:
                    texto = str(dia)
                    if (self.year, self.month, dia) in self.eventos:
                        texto += f"\n{self.eventos[(self.year, self.month, dia)]}"
                    btn = tk.Button(
                        self.frame,
                        text=texto,
                        width=10,
                        height=3,
                        bg = self.bglcolor,
                        command=lambda d=dia: self.agregar_evento(d)
                        
                    )
                    btn.grid(row=fila, column=col, padx=2, pady=2)

    def agregar_evento(self, dia):
        evento = simpledialog.askstring("Evento", f"Evento para el día {dia}:")
        if evento:
            self.eventos[(self.year, self.month, dia)] = evento
            self.frame.destroy()
            self.frame = tk.Frame(self.root, padx=10, pady=10,)
            self.frame.pack()
            self.crear_calendario()


        
        





