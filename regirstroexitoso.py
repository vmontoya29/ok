import tkinter as tk
from colores import *

class RegistroExitoso(tk.Tk):

    def __init__(self, ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.title("Gestion Obleas Mars")
        self.geometry("500x500")
        self.resizable(width=False, height=False)
        self.iconbitmap("imagenes/Logo.ico")
        self.fondo = tk.PhotoImage(file="imagenes/17.png")
        self.fondo1 = tk.Label(self,bg='#ffffff',image=self.fondo).place(x=0, y=0, relwidth=1, relheight=1)
       
        # Label titulo
        self.registrese = tk.Label(self,
                                     text="El usuario se ha registrado exitosamente.",
                                     bg=fondo_blanco,
                                     font=("Comc sans MS ", 17, "bold")
                                     )
        self.registrese.place(x=20, y=200)

        # Boton Cancelar
        self.botonContinuar = tk.Button(self,
                                       text="Continuar",
                                       command=self.continuar,
                                       cursor="hand2",
                                       bg=fondo_trigo,
                                       width=16,
                                       height=2,
                                       foreground=fondo_negro,
                                       relief="flat",
                                       font=("Comc sans MS ", 13, "bold"))
        self.botonContinuar.place(x=160, y=380)

    def continuar(self):
        self.destroy()
        self.ventana_anterior.update()
        self.ventana_anterior.deiconify()