import re
from tkinter import *
from tkinter import messagebox
import mysql.connector as mysqlconn
from mysql.connector.errors import ProgrammingError
import sqlite3
import tkinter.font as tkFont
import tktabl
from paphra_tktable import table

# Se define el frame principal
root = Tk()
root.iconbitmap("../MalagaDVD/imagenes/python.ico")
root.title("frmPrincipal")

# Se obtiene el acho y el alto de la pantalla del sistema
ancho = root.winfo_screenwidth()
alto = root.winfo_screenheight()

# Creación del Frame donde se van a colocar todos los widgets
frmPrincipal = Frame(root, width=ancho, height=alto)
frmPrincipal.config(bg='green', bd=15, width=1500, height=800, padx=10)
frmPrincipal.grid(column=1, row=0, sticky=NSEW, ipadx=10)

frmGrilla = Frame(frmPrincipal, width=1650, height=900)
frmGrilla.config(bg='red', bd=12)
frmGrilla.grid(column=1, row=0, sticky=N+S)


# Se define la clase principal


class principal():
    # Función para centrar ventana
    def centrarVentana(ancho, alto):
        ancho_ventana = ancho
        alto_ventana = alto
        x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + \
            "+" + str(x_ventana) + "+" + str(y_ventana)
        root.geometry(posicion)
        root.resizable(0, 0)

    def numColTablas(tabla):
        try:
            datos = []
            mydb = mysqlconn.connect(
                host="localhost",
                user="root",
                password="hola",
                database="malagadvd"
            )
            mycursor = mydb.cursor()
            sql = "SELECT COUNT(*) AS numColumnas FROM information_schema.columns WHERE table_name = %s"
            mycursor.execute(sql, (tabla,))
            datos = mycursor.fetchone()
            mydb.commit()
            mydb.close()

            messagebox.showinfo("Contador columnas actores",
                                "La consulta sql ha sido satisfactoria")
        except mysqlconn.ProgrammingError as e:
            messagebox.showwarning("Error Base de datos", e)

    def numRowTablas(tabla):
        try:
            datos = []
            mydb = mysqlconn.connect(
                host="localhost",
                user="root",
                password="hola",
                database="malagadvd"
            )
            mycursor = mydb.cursor()
            sql = "SELECT COUNT(*) FROM " + tabla
            mycursor.execute(sql)
            datos = mycursor.fetchone()
            mydb.commit()
            mydb.close()

            messagebox.showinfo("Contador columnas actores",
                                "La consulta sql ha sido satisfactoria")
        except mysqlconn.ProgrammingError as e:
            messagebox.showwarning("Error Base de datos", e)

    def mostrarTablaGrilla(tabla):
        try:
            datos = []
            mydb = mysqlconn.connect(
                host="localhost",
                user="root",
                password="hola",
                database="malagadvd"
            )
            mycursor = mydb.cursor()
            sql = "SELECT * FROM " + tabla
            mycursor.execute(sql)
            datos = mycursor.fetchall()
            print(datos)
            mydb.commit()
            mydb.close()

            totalRows = len(datos)
            totalCols = len(datos[0])

            encabezado = ["Id Actor", "Nombre Actor", "Nacionalidad", "Sexo"]
            grilla = tktabl.Table(
                frmGrilla, col=totalCols, row=totalRows, headers=encabezado)
            # code for creating table
            for i in range(totalRows-1):
                for j in range(totalCols):
                    grilla = Entry(frmGrilla, width=20,
                                   fg='blue', font=('tahoma', 8, 'bold'))
                    grilla.grid(row=i, column=j)
                    grilla.insert(END, datos[i][j])

            '''key_list = ['Id Actor', 'Nombre Actor', 'Nacionalidad', 'Sexo']
            value_list = datos
            dict_from_list = {k: v for k, v in zip(key_list, value_list)}
            print("El diccionario es: ")
            print(dict_from_list)'''

            # Scrool Vertical grilla
            '''scrollVert = Scrollbar(frmGrilla, command=grilla)
            scrollVert.grid(row=0, column=5, sticky=NSEW)
            grilla.config(yscrollcommand=scrollVert.set)'''

        except mysqlconn.ProgrammingError as e:
            messagebox.showwarning("Error Base de datos", e)


    # Instrucciones para establecer la barra de menu
barraMenu = Menu(root)
root.config(menu=barraMenu)

tipoLetra = ('Tahoma', 12, 'bold')
mnubarClientes = Menu(barraMenu, tearoff=0, font=tipoLetra)
barraMenu.add_cascade(label="Clientes", menu=mnubarClientes)
mnubarClientes.add_command(label="Formulario Clientes")

mnubarActores = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Actores", menu=mnubarClientes)
mnubarActores.add_command(label="Formulario Actores")

mnubarProtagonistas = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Protagonistas", menu=mnubarClientes)
mnubarProtagonistas.add_command(label="Formulario Protagonistas")

mnubarDirectores = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Directores", menu=mnubarClientes)
mnubarDirectores.add_command(label="Formulario Directores")

mnubarEjemplares = Menu(barraMenu, tearoff=0)
barraMenu.add_cascade(label="Ejemplares", menu=mnubarClientes)
mnubarEjemplares.add_command(label="Formulario Ejemplares")

# Creacion de los Botones
frmBotones = Frame(frmPrincipal)
frmBotones.configure(bg="light blue")
frmBotones.grid(sticky=W+N+S, column=0, row=0, padx=20)

imgClientes = PhotoImage(file=r"../MalagaDVD/imagenes/clientes.png")
btnClientes = Button(frmBotones, image=imgClientes, text="Clientes", compound="center",
                     width=100, height=100, command=lambda: principal.numColActores("clientes"))
btnClientes.grid(column=0, row=0, padx=20, pady=20)

btnActores = Button(frmBotones, text="Actores", width=12, height=5,
                    command=lambda: principal.mostrarTablaGrilla("actores"))
btnActores.grid(column=0, row=1, padx=20, pady=20)

btnProtagonistas = Button(frmBotones, text="Protagonistas", width=12,
                          height=5, command=lambda: principal.numRowTablas("clientes"))
btnProtagonistas.grid(column=0, row=2, padx=20, pady=20)

imgDirectores = PhotoImage(file=r"../MalagaDVD/imagenes/director.png")
btnDirectores = Button(frmBotones, image=imgDirectores, text="Directores", compound="center",
                       width=100, height=100, command=lambda: principal.mostrarTablaGrilla("actores"))
btnDirectores.grid(column=0, row=3, padx=20, pady=20)

btnEjemplares = Button(frmBotones, text="Ejemplares", width=12, height=5)
btnEjemplares.grid(column=0, row=4, padx=20, pady=20)

btnInformes = Button(frmBotones, text="Informes", width=12, height=5)
btnInformes.grid(column=0, row=5, padx=20, pady=20)

principal.centrarVentana(ancho, alto)

root.mainloop()
