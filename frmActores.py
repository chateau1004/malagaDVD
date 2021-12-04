from _typeshed import Self
import re
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysqlconn
from mysql.connector.errors import ProgrammingError

# Creacion de la ventana Principal del programa
root = Tk()
root.iconbitmap("./graficos/python.ico")
root.title("FrmUsuarios")

# Creación del Frame donde se van a colocar todos los widgets
frmPrincipal = Frame(root, width=500, height=450)
frmPrincipal.pack()

# ----Definición de las variables
idActor = StringVar()
nomActor = StringVar()
nacActor = StringVar()
sexActor = StringVar()

# Creación de los labels y los cuadros de texto del formulario
lblIDActor = Label(frmPrincipal, text="ID Actor")
lblIDActor.grid(column=0, row=0, columnspan=2, padx=10, pady=10, sticky=W)
txtIDActor = Entry(frmPrincipal, width=5, justify="right",
                   fg="red", state="readonly", textvariable=idActor)
txtIDActor.grid(column=2, row=0, columnspan=2, padx=10,
                pady=10, ipadx=2, ipady=2, sticky=E)
lblNomActor = Label(frmPrincipal, text="Nombre de Actor")
lblNomActor.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky=W)
txtNomActor = Entry(frmPrincipal, fg="red", width=35, textvariable=nomActor)
txtNomActor.grid(column=2, row=1, columnspan=2,
                 padx=10, pady=10, ipadx=2, ipady=2)
lblNacActor = Label(frmPrincipal, text="Apellido")
lblNacActor.grid(column=0, row=2, columnspan=2, padx=10, pady=10, sticky=W)
txtNacActor = Entry(frmPrincipal, fg="red", width=35, textvariable=nacActor)
txtNacActor.grid(column=2, row=2, columnspan=2,
                 padx=10, pady=10, ipadx=2, ipady=2)
lblSexActor = Label(frmPrincipal, text="Dirección")
lblSexActor.grid(column=0, row=3, columnspan=2, padx=10, pady=10, sticky=W)
txtSexActor = Entry(frmPrincipal, fg="red", width=35, textvariable=sexActor)
txtSexActor.grid(column=2, row=3, columnspan=2,
                 padx=10, pady=10, ipadx=2, ipady=2)

# Se define la clase actor que se va a utilizar en el programa


class actores():
    def __init__(self, idActor, nomActor, nacActor, sexActor):
        self.idActor = idActor
        self.nomActor = nomActor
        self.nacActor = nacActor
        self.sexActor = sexActor

    def get_idActor(self):
        return self.get_idActor()

    def get_nomActor(self):
        return self.get_nomActor()

    def get_nacActor(self):
        return self.get_nacActor

    def get_sexActor(self):
        return self.get_sexActor

    # ------Se Definen todas la funciones que se van a utlizar en el programa
    # Funcion que permite centrar la ventana de la aplicación

    def centrarVentana(ancho, alto):
        ancho_ventana = ancho
        alto_ventana = alto
        x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
            "+" + str(x_ventana) + "+" + str(y_ventana)
        root.geometry(posicion)
        root.resizable(0, 0)

    def salirFrmActores():
        # valor = messagebox.askquestion("Salir", "Deseas salir de la aplicación")
        # if valor == "yes":
        valor = messagebox.askokcancel(
            "Salir", "Deseas salir del formulario de actores")
        if valor:
            root.destroy()

    def datosCompletos():
        if nomActor.get() == "" or nomActor.get().isspace() or nomActor.get() == None:
                txtNomActor.focus()
                return False
            elif nacActor.get() == "" or nacActor.get().isspace() or nacActor.get() == None:
                txtNacActor.focus()
                return False
            elif sexActor.get() == "" or sexActor.get().isspace() or sexActor.get() == None:
                txtSexActor.focus()
                return False
            else:
                return True
