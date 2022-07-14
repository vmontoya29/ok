import tkinter as tk
from colores import *
from ventana2 import Ventana2
from registrese import Registrese
from tkinter import messagebox
from recuperarConstraseña import RecuperarConseña
from sesion import Sesion


class Ventana1(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion Obleas Mars")
        self.geometry("500x500")
        self.resizable(width=False, height=False)
        self.iconbitmap("imagenes/Logo.ico")
        self.fondo = tk.PhotoImage(file="imagenes/10.png")
        self.fondo1 = tk.Label(self,bg='#ffffff',image=self.fondo).place(x=0, y=0, relwidth=1, relheight=1)


        # variables definidas
        self.usuario = tk.StringVar()
        self.password = tk.StringVar()

        # Label usuario
        self.labelUsuario = tk.Label(self,
                                text="Usuario",
                                bg=fondo_blanco,
                                font=("Comc sans MS ", 13, "bold")
                                )
        self.labelUsuario.place(x=145, y=192)
        # entradas usuario
        self.Entrada = tk.Entry(self,
                           textvariable=self.usuario,
                           relief="solid",
                           bg=fondo_blanco,
                           font=("Comc sans MS ", 12, "bold"))
        self.Entrada.place(height=30, width=210)
        self.Entrada.place(x=145, y=214)

        # Label contraseña
        self.labelContraseña = tk.Label(self,
                                   text="Contraseña",
                                   bg=fondo_blanco,
                                   font=("Comc sans MS ", 13, "bold")
                                   )
        self.labelContraseña.place(x=145, y=250)
        # entrada contraseña
        self.entradaContraseña = tk.Entry(self,
                                     textvariable=self.password,
                                     show="•",
                                     relief="solid",
                                     bg=fondo_blanco,
                                     font=("Comc sans MS ", 12, "bold"))
        self.entradaContraseña.place(height=30, width=210)
        self.entradaContraseña.place(x=145, y=280)

        # Boton Ingresar
        self.botonIngresar = tk.Button(self,
                          text="Ingresar",
                          command=self.login,
                          cursor="hand2",
                          bg=fondo_trigo,
                          width=10,
                          height=1,
                          foreground=fondo_negro,
                          relief="flat",
                          font=("Comc sans MS ", 13, "bold"))
        self.botonIngresar.place(x=195, y=330)

        # Botones Registrarse
        self.botonRegistrarse = tk.Button(self,
                          text="Registrese",
                          command=self.registrese,
                          cursor="hand2",
                          bg=fondo_trigo,
                          width=10,
                          height=1,
                          foreground=fondo_negro,
                          relief="flat",
                          font=("Comc sans MS ", 13, "bold"))
        self.botonRegistrarse.place(x=195, y=384)

        #Botón para recuperar contraseña
        self.botonRecuperar = tk.Button(self,
                          text="¿Olvido su contraseña?",
                          command=self.recuperar_contraseña,
                          cursor="hand2",
                          width=17,
                          bg=fondo_blanco,
                          foreground=fondo_negro,
                          relief="flat",
                          font=("Comc sans MS ", 12, "bold"))
        self.botonRecuperar.place(x=160, y=450)

        #boton para salir
        self.botonSalir = tk.Button(self,
                                        text="Salir",
                                        command=self.salir,
                                        cursor="hand2",
                                        width=5,
                                        height=1,
                                        bg=fondo_negro,
                                        foreground=fondo_blanco,
                                        relief="flat",
                                        font=("Comc sans MS ", 8, "bold"))
        self.botonSalir.place(x=455, y=700)
        self.mainloop()

    # Funciones de botones
    def login(self):
        nombre = self.usuario.get()
        contraseña = self.password.get()

        if nombre and contraseña:

            try:
                with open("datos/usuarios/usuarios.txt", 'r') as f:  # Leyendo a todos los usuarios
                    filas = f.readlines()  # crea una lista de usuarios

                usuarios = []  # creamos una lista vacia de usuarios

                for fila in filas:
                    usuario = fila.split(";")
                    usuarios.append(usuario) # Llenamos la lista usuarios contodos los usuarios

                f.close()

                usuarioHallado = False

                for usuario in usuarios:
                    if nombre == usuario[2] and contraseña == usuario[3]:
                        Sesion.id = usuario[0]
                        Sesion.nombre = usuario[1]
                        Sesion.usuario = usuario[2]
                        usuarioHallado = True
                        break

                if usuarioHallado :
                        self.ir_Ventana2()
                        self.Entrada.delete(0, 'end')
                        self.entradaContraseña.delete(0, 'end')
                else:
                    messagebox.showinfo(message="No existe este usuario.\n"
                                                "NO existe esta contraseña.\n"
                                                "Intente nuevamente.", title="Dados inválidos")
            except Exception as ex:
                print(ex)

        else:
            messagebox.showinfo(message="Debe ingresar un usuario.\n"
                                        "Debe ingresar una contraseña.\n"
                                        "Intente nuevamente.", title="Dados inválidos")

    def ir_Ventana2(self):
        self.withdraw()
        Ventana2(self)

    def salir(self):
        Sesion.id = None
        Sesion.nombre = None
        Sesion.usuario = None
        self.destroy()

    def registrese(self):
        self.withdraw()
        Registrese(self)

    def recuperar_contraseña(self):
        self.withdraw()
        RecuperarConseña(self)

    

Ventana1()



