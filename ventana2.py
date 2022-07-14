import tkinter as tk
from colores import *
from ventas import Ventas
from inventario import Inventario
from domicilios import Domicilios
from sesion import Sesion


class Ventana2(tk.Toplevel):

    def __init__(self,ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.construirse()

    def construirse(self):
        self.title("Gestion Obleas Mars")
        self.geometry("500x500")
        self.resizable(width=False, height=False)
        self.iconbitmap("imagenes/Logo.ico")
        self.fondo = tk.PhotoImage(file="imagenes/11.png")
        self.fondo1 = tk.Label(self,bg='#ffffff',image=self.fondo).place(x=0, y=0, relwidth=1, relheight=1)

        self.cabecera = tk.Label(self,
                                     text="Usuario conectado: "+Sesion.usuario,
                                     bg=fondo_blanco,
                                     fg=fondo_negro,
                                     font=("Comc sans MS ", 10, "bold")
                                     )
        self.cabecera.place(x=195,y=15)

        # Botones
        self.boton_ventas = tk.Button(self,
                                      text="Ventas",
                                      command=self.ventas,
                                      cursor="hand2",
                                      bg=fondo_trigo,
                                      width=12,
                                      height=1,
                                      foreground=fondo_negro,
                                      relief="flat",
                                      font=("Comc sans MS ", 15, "bold"))
        self.boton_ventas.place(x=185, y=143)
                       
        self.botoninventario = tk.Button(self,
                                    text="Inventario",
                                    command=self.inventario,
                                    cursor="hand2",
                                    width=12,
                                    height=1,
                                    bg=fondo_trigo,
                                    foreground=fondo_negro,
                                    relief="flat",
                                    font=("Comc sans MS ", 15, "bold"))
        self.botoninventario.place(x=185, y=233)

        self.botondomicilios = tk.Button(self,
                                           text="Domicilios",
                                           command=self.domicilios,
                                           cursor="hand2",
                                           width=12,
                                           height=1,
                                           bg=fondo_trigo,
                                           foreground=fondo_negro,
                                           relief="flat",
                                           font=("Comc sans MS ", 15, "bold"))
        self.botondomicilios.place(x=185, y=315)

        self.botonVolver = tk.Button(self,
                                     text="←",
                                     cursor="hand2",
                                     command=self.regresar,
                                     bg=fondo_trigo,
                                    foreground=fondo_negro,
                                     relief="flat",
                                     font=("Comc sans MS ", 14, "bold"))
        self.botonVolver.place(x=381, y=24)

    def regresar(self):
        self.destroy()
        self.ventana_anterior.update()
        self.ventana_anterior.deiconify()
    
    def domicilios(self):
        Domicilios(self.ventana_anterior)
        self.destroy()
    
    def inventario(self):
        Inventario(self.ventana_anterior)
        self.destroy()


    def ventas(self):
        Ventas(self.ventana_anterior)
        self.destroy()

