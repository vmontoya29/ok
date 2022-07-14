import tkinter as tk
from colores import *
from tkinter import messagebox

class RecuperarConseña(tk.Tk):

    def __init__(self, ventana_anterior):
        tk.Toplevel.__init__(self)
        self.ventana_anterior = ventana_anterior
        self.title("Gestion Obleas Mars")
        self.geometry("500x500")
        self.resizable(width=False, height=False)
        self.iconbitmap("imagenes/Logo.ico")
        self.fondo = tk.PhotoImage(file="imagenes/16.png")
        self.fondo1 = tk.Label(self,bg='#ffffff',image=self.fondo).place(x=0, y=0, relwidth=1, relheight=1)
       

        # Label titulo
        self.registrese = tk.Label(self,
                                     text="Recuperar Contraseña",
                                     bg=fondo_blanco,
                                     font=("Comc sans MS ", 20, "bold")
                                     )
        self.registrese.place(x=100, y=120)

        # variables definidas
        self.usuario = tk.StringVar()

        # Label usuario
        self.labelUsuario = tk.Label(self,
                                     text="Usuario",
                                     bg=fondo_blanco,
                                     font=("Comc sans MS ", 10, "bold")
                                     )
        self.labelUsuario.place(x=220, y=170)
        # entradas usuario
        self.entradaUsuario = tk.Entry(self,
                                textvariable=self.usuario,
                                relief="solid",
                                bg=fondo_blanco,
                                font=("Comc sans MS ", 10, "bold"))
        self.entradaUsuario.place(height=30, width=200)
        self.entradaUsuario.place(x=150, y=200)

        # Preguntas de validación para recuperar contraseña
        # variables definidas
        self.preguntaValidacion1 = tk.StringVar()
        self.preguntaValidacion2 = tk.StringVar()
        self.preguntaValidacion3 = tk.StringVar()

        # Label pregunta 1
        self.labelPregunta1 = tk.Label(self,
                                    text="¿Cuál es tu Comida Favorita?",
                                    bg=fondo_blanco,
                                    font=("Comc sans MS ", 10, "bold")
                                    )
        self.labelPregunta1.place(x=150, y=230)
        # entradas pregunta 1
        self.entradaPregunta1 = tk.Entry(self,
                                      textvariable=self.preguntaValidacion1,
                                      relief="solid",
                                      bg=fondo_blanco,
                                      font=("Comc sans MS ", 10, "bold"))
        self.entradaPregunta1.place(height=30, width=200)
        self.entradaPregunta1.place(x=150, y=260)

        # Label pregunta 2
        self.labelPregunta2 = tk.Label(self,
                                       text="¿Cuál es tu Color Favorito?",
                                       bg=fondo_blanco,
                                       font=("Comc sans MS ", 10, "bold")
                                       )
        self.labelPregunta2.place(x=150, y=290)
        # entradas pregunta 2
        self.entradaPregunta2 = tk.Entry(self,
                                         textvariable=self.preguntaValidacion2,
                                         relief="solid",
                                         bg=fondo_blanco,
                                         font=("Comc sans MS ", 10, "bold"))
        self.entradaPregunta2.place(height=30, width=200)
        self.entradaPregunta2.place(x=150, y=320)

        # Label pregunta 3
        self.labelPregunta3 = tk.Label(self,
                                       text="¿Cuál es tu Trabajo Ideal?",
                                       bg=fondo_blanco,
                                       font=("Comc sans MS ", 10, "bold")
                                       )
        self.labelPregunta3.place(x=150, y=350)
        # entradas pregunta 3
        self.entradaPregunta3 = tk.Entry(self,
                                         textvariable=self.preguntaValidacion3,
                                         relief="solid",
                                         bg=fondo_blanco,
                                         font=("Comc sans MS ", 10, "bold"))
        self.entradaPregunta3.place(height=30, width=200)
        self.entradaPregunta3.place(x=150, y=380)

        # Boton Volver
        self.botonVolver = tk.Button(self,
                                       text="←",
                                       command=self.volver,
                                       cursor="hand2",
                                       bg=fondo_trigo,
                                       foreground=fondo_negro,
                                       relief="flat",
                                       font=("Comc sans MS ", 13, "bold"))
        self.botonVolver.place(x=381, y=23)

        # Boton Recuperar
        self.botonRecuperar = tk.Button(self,
                                       text="Recuperar",
                                       command=self.recuperar,
                                       cursor="hand2",
                                       bg=fondo_trigo,
                                       foreground=fondo_negro,
                                       relief="flat",
                                       font=("Comc sans MS ", 13, "bold"))
        self.botonRecuperar.place(x=205, y=435)


    def volver(self):
        self.destroy()
        self.ventana_anterior.update()
        self.ventana_anterior.deiconify()

    def recuperar(self):

        if not self.entradaUsuario.get() or self.entradaUsuario.get() == "Ingrese el Usuario":
            self.entradaUsuario.delete(0, tk.END)
            self.entradaUsuario.insert(0, "Ingrese el Usuario")
            self.entradaUsuario.config(bg="gray")

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
            (self.entradaUsuario.get() and self.entradaUsuario.get() != "Ingrese el Usuario") and
            (self.entradaPregunta1.get() and self.entradaPregunta1.get() != "Ingresa el nombre de tu abuelo") and
            (self.entradaPregunta2.get() and self.entradaPregunta2.get() != "Ingresa el nombre de tu mascota") and
            (self.entradaPregunta3.get() and self.entradaPregunta3.get() != "Ingresa el nombre de tu traga")
          ):

            try:
                with open("datos/usuarios/usuarios.txt", 'r') as f: # Leyendo a todos los usuarios
                    filas = f.readlines()  # crea una lista de usuarios

                usuarios = []  #creamos una lista vacia de usuarios

                for fila in filas: # llenamos la lista con todos los usuarios de los registros del archivo
                    usuario = fila.split(";") # Tomamos registro por registro y lo separamos por el ';'
                    usuarios.append(usuario) # Lo agregamos como una lista

                f.close() # Cerramos el archivo

                #Variable para recuperar la contraseña
                contraseña = ""

                #Variable para controlar si se recupero la contraseña
                recuperada = False

                # Recorremos todos los usuarios para buscar y comparar los datos de recuperación
                for usuario in usuarios:
                    if (
                        self.entradaUsuario.get() == usuario[2] and
                        self.entradaPregunta1.get() == usuario[4] and
                        self.entradaPregunta2.get() == usuario[5] and
                        self.entradaPregunta3.get() == usuario[6]
                    ):
                        contraseña = usuario[3] # si los datos son correctos
                        recuperada = True

                #Si los datos ingresados son correctos se recupera la contraseña
                if recuperada:

                    messagebox.showinfo(message="Su contraseña es: "+contraseña+"", title="Contraseña Recuperada")

                else:
                    messagebox.showinfo(message="Los datos ingresados son incorrectos \nIntente nuevamente.\n"
                                                "Verifique que el usuario sea el correcto.\n"
                                                "Verifique que las respuestas sean correctas.", title="Dados inválidos")
            except Exception as ex:
                print(ex)











