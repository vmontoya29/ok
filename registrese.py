import tkinter as tk
from colores import *
from tkinter import messagebox
from regirstroexitoso import RegistroExitoso

class Registrese(tk.Toplevel):

    def __init__(self, ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.title("Gestion Obleas Mars")
        self.geometry("500x500")
        self.resizable(width=False, height=False)
        self.iconbitmap("imagenes/Logo.ico")
        self.fondo = tk.PhotoImage(file="imagenes/14.png")
        self.fondo1 = tk.Label(self,bg='#ffffff',image=self.fondo).place(x=0, y=0, relwidth=1, relheight=1)
        

        # Label titulo
        self.registrese = tk.Label(self,
                                     text="Regístrese",
                                     bg=fondo_blanco,
                                     font=("Comc sans MS ", 20, "bold")
                                     )
        self.registrese.place(x=170, y=120)

        # variables definidas
        self.nombreCompleto = tk.StringVar()
        self.usuario = tk.StringVar()
        self.password = tk.StringVar()


        # Label nombre completo
        self.labelNombre = tk.Label(self,
                                     text="Nombre Completo",
                                     bg=fondo_blanco,
                                     font=("Comc sans MS ", 10, "bold")
                                     )
        self.labelNombre.place(x=20, y=160)
        # entradas nombre completo
        self.entradaNombre = tk.Entry(self,
                                       textvariable=self.nombreCompleto,
                                       relief="solid",
                                       bg=fondo_blanco,
                                       font=("Comc sans MS ", 13, "bold"))
        self.entradaNombre.place(height=30, width=195)
        self.entradaNombre.place(x=20, y=190)

        # Label usuario
        self.labelUsuario = tk.Label(self,
                                     text="Usuario",
                                     bg=fondo_blanco,
                                     font=("Comc sans MS ", 10, "bold")
                                     )
        self.labelUsuario.place(x=20, y=220)
        # entradas usuario
        self.entradaUsuario = tk.Entry(self,
                                textvariable=self.usuario,
                                relief="solid",
                                bg=fondo_blanco,
                                font=("Comc sans MS ", 10, "bold"))
        self.entradaUsuario.place(height=30, width=195)
        self.entradaUsuario.place(x=20, y=250)

        # Label contraseña
        self.labelContraseña = tk.Label(self,
                                        text="Contraseña",
                                        bg=fondo_blanco,
                                        font=("Comc sans MS ", 10, "bold")
                                        )
        self.labelContraseña.place(x=20, y=280)
        # entrada contraseña
        self.entradaContraseña = tk.Entry(self,
                                          textvariable=self.password,
                                          show="•",
                                          relief="solid",
                                          bg=fondo_blanco,
                                          font=("Comc sans MS ", 10, "bold"))
        self.entradaContraseña.place(height=30, width=195)
        self.entradaContraseña.place(x=20, y=310)

        # Boton Cancelar
        self.botonIngresar = tk.Button(self,
                                       text="Cancelar",
                                       command=self.cancelar,
                                       cursor="hand2",
                                       bg=fondo_trigo,
                                       foreground=fondo_negro,
                                       relief="flat",
                                       font=("Comc sans MS ", 13, "bold"))
        self.botonIngresar.place(x=340, y=370)

        # Preguntas de validación para recuperar contraseña
        # variables definidas
        self.preguntaValidacion1 = tk.StringVar()
        self.preguntaValidacion2 = tk.StringVar()
        self.preguntaValidacion3 = tk.StringVar()

        # Label pregunta 1
        self.labelPregunta1 = tk.Label(self,
                                    text="¿Cual es Comida Favorita?",
                                    bg=fondo_blanco,
                                    font=("Comc sans MS ", 10, "bold")
                                    )
        self.labelPregunta1.place(x=280, y=160)
        # entradas pregunta 1
        self.entradaPregunta1 = tk.Entry(self,
                                      textvariable=self.preguntaValidacion1,
                                      relief="solid",
                                      bg=fondo_blanco,
                                      font=("Comc sans MS ", 10, "bold"))
        self.entradaPregunta1.place(height=30, width=195)
        self.entradaPregunta1.place(x=280, y=190)

        # Label pregunta 2
        self.labelPregunta2 = tk.Label(self,
                                       text="¿Cuál es tu Color Favorito?",
                                       bg=fondo_blanco,
                                       font=("Comc sans MS ", 10, "bold")
                                       )
        self.labelPregunta2.place(x=280, y=220)
        # entradas pregunta 2
        self.entradaPregunta2 = tk.Entry(self,
                                         textvariable=self.preguntaValidacion2,
                                         relief="solid",
                                         bg=fondo_blanco,
                                         font=("Comc sans MS ", 10, "bold"))
        self.entradaPregunta2.place(height=30, width=195)
        self.entradaPregunta2.place(x=280, y=250)

        # Label pregunta 3
        self.labelPregunta3 = tk.Label(self,
                                       text="¿Cuál es tu Trabajo ideal?",
                                       bg=fondo_blanco,
                                       font=("Comc sans MS ", 10, "bold")
                                       )
        self.labelPregunta3.place(x=280, y=280)
        # entradas pregunta 3
        self.entradaPregunta3 = tk.Entry(self,
                                         textvariable=self.preguntaValidacion3,
                                         relief="solid",
                                         bg=fondo_blanco,
                                         font=("Comc sans MS ", 10, "bold"))
        self.entradaPregunta3.place(height=30, width=195)
        self.entradaPregunta3.place(x=280, y=310)

        # Boton Regístrese
        self.botonRegistrese = tk.Button(self,
                                       text="Regístrese",
                                       command=self.registrece,
                                       cursor="hand2",
                                       bg=fondo_trigo,
                                       foreground=fondo_negro,
                                       relief="flat",
                                       font=("Comc sans MS ", 13, "bold"))
        self.botonRegistrese.place(x=70, y=370)



    def cancelar(self):
        self.destroy()
        self.ventana_anterior.update()
        self.ventana_anterior.deiconify()

    def registrece(self):

        if not self.entradaNombre.get() or self.entradaNombre.get() == "Ingrese el Nombre":
            self.entradaNombre.delete(0, tk.END)
            self.entradaNombre.insert(0, "Ingrese el Nombre")
            self.entradaNombre.config(bg="gray")

        if not self.entradaUsuario.get() or self.entradaUsuario.get() == "Ingrese el Usuario":
            self.entradaUsuario.delete(0, tk.END)
            self.entradaUsuario.insert(0, "Ingrese el Usuario")
            self.entradaUsuario.config(bg="gray")

        if not self.entradaContraseña.get() or self.entradaContraseña.get() == "Ingrese la contraseña":
            self.entradaContraseña.delete(0, tk.END)
            self.entradaContraseña.insert(0, "Ingrese la contraseña")
            self.entradaContraseña.config(bg="gray", show="")

        if len(self.entradaContraseña.get()) < 8:
            self.entradaContraseña.delete(0, tk.END)
            self.entradaContraseña.insert(0, "Debe ser de minimo 8 caracteres")
            self.entradaContraseña.config(bg="gray", show="")

        if not self.entradaPregunta1.get() or self.entradaPregunta1.get() == "Ingresa el nombre de tu abuelo":
            self.entradaPregunta1.delete(0, tk.END)
            self.entradaPregunta1.insert(0, "Ingresa el nombre de tu abuelo")
            self.entradaPregunta1.config(bg="gray")

        if not self.entradaPregunta2.get() or self.entradaPregunta2.get() == "Ingresa el nombre de tu mascota":
            self.entradaPregunta2.delete(0, tk.END)
            self.entradaPregunta2.insert(0, "Ingresa el nombre de tu mascota")
            self.entradaPregunta2.config(bg="gray")

        if not self.entradaPregunta3.get() or self.entradaPregunta3.get() == "Ingresa el nombre de tu traga":
            self.entradaPregunta3.delete(0, tk.END)
            self.entradaPregunta3.insert(0, "Ingresa el nombre de tu traga")
            self.entradaPregunta3.config(bg="gray")

        if (
            (self.entradaNombre.get() and self.entradaNombre.get() != "Ingrese el Nombre")and
            (self.entradaUsuario.get() and self.entradaUsuario.get() != "Ingrese el Usuario")and
            (self.entradaContraseña.get() and
             self.entradaContraseña.get() != "Ingrese la contraseña" and
             self.entradaContraseña.get() != "Debe ser de minimo 8 caracteres"
            )and
            (self.entradaPregunta1.get() and self.entradaPregunta1.get() != "Ingresa el nombre de tu abuelo")and
            (self.entradaPregunta2.get() and self.entradaPregunta2.get() != "Ingresa el nombre de tu mascota")and
            (self.entradaPregunta3.get() and self.entradaPregunta3.get() != "Ingresa el nombre de tu traga")
          ) :

            try:
                with open("datos/usuarios/usuarios.txt", 'r') as f: # Leyendo a todos los usuarios
                    filas = f.readlines()  # crea una lista de usuarios

                usuarios = []  #creamos una lista vacia de usuarios

                usuarioLogins = []

                contraseñasLogins = []

                for fila in filas:
                    usuario = fila.split(";")
                    usuarios.append(usuario)
                f.close()

                for usuario in usuarios:
                    usuarioLogins.append(usuario[2])
                    contraseñasLogins.append(usuario[3])

                if ( self.entradaUsuario.get() not in usuarioLogins or
                    self.entradaContraseña not in contraseñasLogins ):

                    f = open("datos/usuarios/clave.txt", "r")  # Consultando la clave actual
                    clave_actual = f.read()
                    f.close()

                    clave_nueva = int(clave_actual) + 1 # Aumentando en 1 la clave

                    f = open("datos/usuarios/clave.txt", "w")
                    f.write(str(clave_nueva))    # Actualizando la nueva clave
                    f.close()

                    f = open("datos/usuarios/usuarios.txt", "a")
                    f.write(
                        str(clave_nueva)+";"+
                        self.entradaNombre.get()+";"+
                        self.entradaUsuario.get()+";"+
                        self.entradaContraseña.get()+";"+
                        self.entradaPregunta1.get()+";"+
                        self.entradaPregunta2.get()+";"+
                        self.entradaPregunta3.get()+";\n"
                    )
                    f.close()
                    self.destroy()
                    RegistroExitoso(self.ventana_anterior)
                else:
                    messagebox.showinfo(message="Intente con otro usuario \ny con otra contreseña.\n"
                                                "Ya existe este usuario.\n"
                                                "Ya existe esta contraseña", title="Dados inválidos")

            except Exception as ex:
                print(ex)











