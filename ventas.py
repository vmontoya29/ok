import tkinter as tk
import sys

import colores
from colores import *
from sesion import Sesion
from tkinter import messagebox

class Ventas(tk.Toplevel):

    def __init__(self, ventana_principal):
        tk.Toplevel.__init__(self)
        self.ventana_principal = ventana_principal
        self.construirse()

    def construirse(self):
        self.title("Geriatic Advance")
        self.geometry("1280x650+1+-3")
        self.resizable(width=True, height=True)
        '''
        canvas = tk.Canvas(self, width=400, height=400)
        canvas.create_oval(10, 10, 20, 20, fill="red")
        canvas.create_oval(200, 200, 220, 220, fill="blue")
        canvas.place(x=300, y=200)

        scroll_x = tk.Scrollbar(canvas, orient="horizontal", command=canvas.xview)
        scroll_x.grid(row=1, column=0, sticky="ew")

        scroll_y = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
        scroll_y.grid(row=0, column=1, sticky="ns")

        canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        canvas.configure(scrollregion=canvas.bbox("all"))
        '''

        frame = tk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=1)

        canvas = tk.Canvas(frame, bg='#ffffff')
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        frame2 = tk.Frame(canvas,width='1000',height='469', bg='#ffffff', relief=tk.FLAT)
        canvas.create_window(700, 300, window=frame2)

        self.fondo = tk.PhotoImage(file="imagenes/1.png")
        fondo_label = tk.Label(frame2, image=self.fondo)
        fondo_label.place(bordermode=tk.INSIDE)

        self.cabecera = tk.Label(canvas,
                                 text="Usuario conectado: " + Sesion.usuario,
                                 bg=fondo_blanco,
                                 fg=fondo_aqua,
                                 font=("Comc sans MS ", 10, "bold")
                                 )
        canvas.create_window(1000, 5, window=self.cabecera)

        '''
        widget = tk.Label(canvas, text='Spam', fg='white', bg='black')
        widget.pack()
        canvas.create_window(100, 100, window=widget)
        '''


        botonVolver2 = tk.Button(canvas,
                                 text="⬅",
                                 cursor="hand2",
                                 command=self.regresar,
                                 bg=fondo_aqua,
                                 width=3,
                                 foreground=fondo_negro,
                                 relief="flat",
                                 font=("Comc sans MS ", 15, "bold"))
        botonVolver2.pack()
        canvas.create_window(80, 90, window=botonVolver2)

        # Creación del formulario para el ingreso de medicamentos en frame2
        # variables definidas
        self.medicamento = tk.StringVar()
        self.cantidad = tk.StringVar()
        self.fecha = tk.StringVar()
        self.hora = tk.StringVar()

        self.entradaMedicamento = tk.Entry(frame2,
                                      textvariable=self.medicamento,
                                      relief="flat",
                                      bg=fondo_blanco,
                                      font=("Comc sans MS ", 12, "bold"))
        self.entradaMedicamento.place(height=45, width=360)
        self.entradaMedicamento.place(x=287, y=132)

        self.entradaCantidad = tk.Entry(frame2,
                                           textvariable=self.cantidad,
                                           relief="flat",
                                           bg=fondo_blanco,
                                           font=("Comc sans MS ", 12, "bold"))
        self.entradaCantidad.place(height=45, width=360)
        self.entradaCantidad.place(x=287, y=190)

        self.entradaFecha = tk.Entry(frame2,
                                        textvariable=self.fecha,
                                        relief="flat",
                                        bg=fondo_blanco,
                                        fg=fondo_aqua,
                                        font=("Comc sans MS ", 12, "bold"))
        self.entradaFecha.place(height=45, width=360)
        self.entradaFecha.place(x=287, y=247)
        self.entradaFecha.insert(0, "año/mes/día  0000/00/00")

        self.entradaHora = tk.Entry(frame2,
                                     textvariable=self.hora,
                                     relief="flat",
                                     bg=fondo_blanco,
                                     fg=fondo_aqua,
                                     font=("Comc sans MS ", 12, "bold"))
        self.entradaHora.place(height=45, width=360)
        self.entradaHora.place(x=287, y=304)
        self.entradaHora.insert(0, "hora:minutos:AM/PM  00:00:AM/PM")

        # Botones
        self.botonEliminar = tk.Button(frame2,
                                       text="Eliminar",
                                       cursor="hand2",
                                       # command=self.regresar,
                                       bg=fondo_aqua,
                                       width=7,
                                       foreground=fondo_negro,
                                       relief="flat",
                                       font=("Comc sans MS ", 14, "bold"))
        self.botonEliminar.pack()
        self.botonEliminar.place(x=75, y=395)

        self.botonIngresar = tk.Button(frame2,
                                        text="Ingresar",
                                        cursor="hand2",
                                        command=self.ingresarMedicamento,
                                        bg=fondo_aqua,
                                        width=7,
                                        foreground=fondo_negro,
                                        relief="flat",
                                        font=("Comc sans MS ", 14, "bold"))
        self.botonIngresar.pack()
        self.botonIngresar.place(x=240, y=395)

        self.botonConsultar = tk.Button(frame2,
                                       text="Consultar",
                                       cursor="hand2",
                                       # command=self.regresar,
                                       bg=fondo_aqua,
                                       width=7,
                                       foreground=fondo_negro,
                                       relief="flat",
                                       font=("Comc sans MS ", 14, "bold"))
        self.botonConsultar.pack()
        self.botonConsultar.place(x=410, y=395)

        self.botonActualizar = tk.Button(frame2,
                                         text="Actualizar",
                                         cursor="hand2",
                                         # command=self.regresar,
                                         bg=fondo_aqua,
                                         width=7,
                                         foreground=fondo_negro,
                                         relief="flat",
                                         font=("Comc sans MS ", 14, "bold"))
        self.botonActualizar.pack()
        self.botonActualizar.place(x=575, y=395)


        # Código para mostrar el listado
        self.LabelId = tk.Label(canvas,
                                 text="ID",
                                 bg=fondo_negro,
                                 fg=fondo_blanco,
                                 font=("Comc sans MS ", 20, "bold")
                                 )
        canvas.create_window(100, 600, window=self.LabelId)

        self.LabelMedicamento = tk.Label(canvas,
                                text="MEDICAMENTO",
                                bg=fondo_negro,
                                fg=fondo_blanco,
                                font=("Comc sans MS ", 20, "bold")
                                )
        canvas.create_window(300, 600, window=self.LabelMedicamento)

        self.LabelCantidad = tk.Label(canvas,
                                         text="CANTIDAD",
                                         bg=fondo_negro,
                                         fg=fondo_blanco,
                                         font=("Comc sans MS ", 20, "bold")
                                         )
        canvas.create_window(600, 600, window=self.LabelCantidad)

        self.LabelFecha = tk.Label(canvas,
                                      text="FECHA",
                                      bg=fondo_negro,
                                      fg=fondo_blanco,
                                      font=("Comc sans MS ", 20, "bold")
                                      )
        canvas.create_window(800, 600, window=self.LabelFecha)

        self.LabelHora = tk.Label(canvas,
                                   text="HORA",
                                   bg=fondo_negro,
                                   fg=fondo_blanco,
                                   font=("Comc sans MS ", 20, "bold")
                                   )
        canvas.create_window(1000, 600, window=self.LabelHora)

        try:
            with open("datos/medicamentos/medicamentos.txt", 'r') as f:  # Leyendo todos los medicamentos
                filas = f.readlines()  # crea una lista de usuarios

            medicamentos = []  # creamos una lista vacia de usuarios

            for fila in filas:
                medicamento = fila.split(";")
                medicamentos.append(medicamento)
            f.close()

            distanciaVertical = 630
            for medicamento in medicamentos:
                self.datoId = tk.Label(canvas,
                                        text=medicamento[0],
                                        bg=fondo_blanco,
                                        fg=fondo_aqua,
                                        font=("Comc sans MS ", 15)
                                        )
                canvas.create_window(100, distanciaVertical, window=self.datoId)

                self.datoMedicamento = tk.Label(canvas,
                                                 text=medicamento[2],
                                                 bg=fondo_blanco,
                                                 fg=fondo_aqua,
                                                 font=("Comc sans MS ", 15)
                                                 )
                canvas.create_window(300, distanciaVertical, window=self.datoMedicamento)

                self.datoCantidad = tk.Label(canvas,
                                              text=medicamento[3],
                                              bg=fondo_blanco,
                                              fg=fondo_aqua,
                                              font=("Comc sans MS ", 15)
                                              )
                canvas.create_window(600, distanciaVertical, window=self.datoCantidad)

                self.datoFecha = tk.Label(canvas,
                                           text=medicamento[5],
                                           bg=fondo_blanco,
                                           fg=fondo_aqua,
                                           font=("Comc sans MS ", 15)
                                           )
                canvas.create_window(800, distanciaVertical, window=self.datoFecha)

                self.datoHora = tk.Label(canvas,
                                          text=medicamento[5],
                                          bg=fondo_blanco,
                                          fg=fondo_aqua,
                                          font=("Comc sans MS ", 15)
                                          )
                canvas.create_window(1000, distanciaVertical, window=self.datoHora)

                distanciaVertical += 30

        except Exception as ex:
            print(ex)







    def regresar(self):
        self.destroy()
        self.ventana_principal.ir_Ventana2()


    def ingresarMedicamento(self):

        # Código para validar la entrada de medicamentos
        if not self.entradaMedicamento.get() or self.entradaMedicamento.get() == "Ingrese el Medicamento":
            self.entradaMedicamento.delete(0, tk.END)
            self.entradaMedicamento.insert(0, "Ingrese el Medicamento")
            self.entradaMedicamento.config(bg="gray")


        # Código para validar la entrada de la cantidad
        if (not self.entradaCantidad.get()
            or self.entradaCantidad.get() == "Ingrese la Cantidad"
            or self.entradaCantidad.get() == "Ingrese una cantidad mayor a 0"
        ):
            self.entradaCantidad.delete(0, tk.END)
            self.entradaCantidad.insert(0, "Ingrese la Cantidad")
            self.entradaCantidad.config(bg="gray")

        try:
            if int(self.entradaCantidad.get()) <= 0:
                self.entradaCantidad.delete(0, tk.END)
                self.entradaCantidad.insert(0, "Ingrese una cantidad mayor a 0")
                self.entradaCantidad.config(bg="gray")
        except ValueError:
            self.entradaCantidad.delete(0, tk.END)
            self.entradaCantidad.insert(0, "Ingrese un número para la cantidad")
            self.entradaCantidad.config(bg="gray")


        # Código para validar la entrada de la Fecha
        try:
            año, mes, dia = self.entradaFecha.get().split("/")
            if int(año) < 2022 or int(año) > 2050:
                self.entradaFecha.delete(0, tk.END)
                self.entradaFecha.insert(0, año+"/"+mes+"/"+dia+" Año incorrecto: "+año)
                self.entradaFecha.config(bg="gray", fg="black")

            if int(mes) < 1 or int(mes) > 12:
                self.entradaFecha.delete(0, tk.END)
                self.entradaFecha.insert(0, año+"/"+mes+"/"+dia+" Mes incorrecto: "+mes)
                self.entradaFecha.config(bg="gray", fg="black")

            if int(dia) < 1 or int(dia) > 31:
                self.entradaFecha.delete(0, tk.END)
                self.entradaFecha.insert(0, año+"/"+mes+"/"+dia+" Día incorrecto: "+dia)
                self.entradaFecha.config(bg="gray", fg="black")

        except ValueError:
            self.entradaFecha.delete(0, tk.END)
            self.entradaFecha.insert(0, "Ingresar: año/mes/día")
            self.entradaFecha.config(bg="gray", fg="black")


        # Código para validar la entrada de la hora
        try:
            hora, minutos, jornada = self.entradaHora.get().split(":")

            if int(hora) < 1 or int(hora) > 12:
                self.entradaHora.delete(0, tk.END)
                self.entradaHora.insert(0, hora+":"+minutos+":"+jornada+" Hora incorrecta: "+hora)
                self.entradaHora.config(bg="gray", fg="black")

            if int(minutos) < 00 or int(minutos) > 59:
                self.entradaHora.delete(0, tk.END)
                self.entradaHora.insert(0, hora+":"+minutos+":"+jornada+" Minutos incorrectos: "+minutos)
                self.entradaHora.config(bg="gray", fg="black")

            if jornada not in ("AM","PM"):
                self.entradaHora.delete(0, tk.END)
                self.entradaHora.insert(0, hora+":"+minutos+":"+jornada+" Jornada incorrecta: "+jornada)
                self.entradaHora.config(bg="gray", fg="black")

        except ValueError:
            self.entradaHora.delete(0, tk.END)
            self.entradaHora.insert(0, "Ingresar: hora:minutos:AM o PM")
            self.entradaHora.config(bg="gray", fg="black")

        if (
            self.entradaMedicamento.get() and
            self.entradaCantidad.get() and
            self.entradaFecha.get() and
            self.entradaHora.get()
        ):
            try:

                f = open("datos/medicamentos/clave.txt", "r")  # Consultando la clave actual
                clave_actual = f.read()
                f.close()

                clave_nueva = int(clave_actual) + 1  # Aumentando en 1 la clave

                f = open("datos/medicamentos/clave.txt", "w")
                f.write(str(clave_nueva))  # Actualizando la nueva clave
                f.close()

                f = open("datos/medicamentos/medicamentos.txt", "a")
                f.write(
                    str(clave_nueva) + ";" +
                    Sesion.id + ";"+
                    self.entradaMedicamento.get() + ";" +
                    self.entradaCantidad.get() + ";" +
                    self.entradaFecha.get() + ";" +
                    self.entradaHora.get() + ";\n"
                )
                f.close()

                messagebox.showinfo(message="El medicamento:\n" + self.entradaMedicamento.get() + ".\n"
                                    "Ha sido registrado exitosamente.\n",
                                    title="Medicamento ingresado")

                # Limpiar el formulario

                self.entradaMedicamento.delete(0, tk.END)
                self.entradaMedicamento.insert(0, "")
                self.entradaMedicamento.config(bg="white")

                self.entradaCantidad.delete(0, tk.END)
                self.entradaCantidad.insert(0, "")
                self.entradaCantidad.config(bg="white")

                self.entradaFecha.delete(0, tk.END)
                self.entradaFecha.insert(0, "")
                self.entradaFecha.config(bg="white")

                self.entradaHora.delete(0, tk.END)
                self.entradaHora.insert(0, "")
                self.entradaHora.config(bg="white")

                self.destroy()
                self.ventana_principal.ir_Ventana_Medicamentos()




            except Exception as ex:
                exception_type, exception_object, exception_traceback = sys.exc_info()
                filename = exception_traceback.tb_frame.f_code.co_filename
                line_number = exception_traceback.tb_lineno

                print("Exception type: ", exception_type)
                print("File name: ", filename)
                print("Line number: ", line_number)





