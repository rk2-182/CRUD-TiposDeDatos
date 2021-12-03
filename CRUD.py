import db #importamos archivo con la conexion
import datetime
import os

#creamos una instancia del archivo que contiene la conexion y su funcion
connect = db.conexion()

#valores retornados de la funcion
bd = connect[0]
cursor = connect[1]



#Mostrar Datos
def mostrarDatos(opcion):
    if opcion == 1:
        cursor.execute("select * from proveedor")
        resultado = cursor.fetchall()
        os.system('cls')
        print("Tabla Proveedor")
        print("---------------")
        return resultado
    elif opcion == 2:
        cursor.execute("select * from productos")
        resultado = cursor.fetchall()
        os.system('cls')
        print("Tabla Productos")
        print("---------------")
        for i in resultado:
            print(i)
    elif opcion == 3:
        cursor.execute("select * from cliente")
        resultado = cursor.fetchall()
        os.system('cls')
        print("Tabla Clientes")
        print("---------------")
        for i in resultado:
            print("Rut:",i[0])
            print("Nombre:",i[1])
            print("Fecha Nacimiento: ",i[2])
            print("Telefono: ",i[3])
            print("--------------------")
            print(" ")

#Insertar Datos
def insertarDatosProveedor():
    nombreProveedor = input("Ingrese el nombre del proveedor: ")
    direccion = input("Ingrese la direccion: ")
    sql = 'insert into proveedor (nombre,direccion) values (%s,%s)'
    valores = (nombreProveedor,direccion)
    cursor.execute(sql,valores) #recibe 2argumentos: las instrucciones sql y los valores
    bd.commit()

    if cursor.rowcount == 1:
        print("Datos ingresados")
    else:
        print("Error al ingresar datos")

def insertarDatosCliente():
    dni=int(input("Ingrese el DNI: "))
    nombre = input("Ingrese su nombre: ")
    año=int(input("Ingrese su año de nacimiento: "))
    mes=int(input("Ingresa tu mes de nacimiento: "))
    dia=int(input("Ingresa el dia de nacimiento: "))
    fechaNacimiento = datetime.date(año,mes,dia)
    telefono = input("Ingrese tu numero telefonico: ")

    sql = 'insert into cliente (dni,nombre,fechaNac,telefono) values (%s,%s,%s,%s)'
    datos = (dni,nombre,fechaNacimiento,telefono)
    cursor.execute(sql,datos)
    bd.commit()

    if cursor.rowcount == 1:
        print("Datos ingresados")
    else:
        print("Error al ingresar datos")

def insertarDatosProducto():
    pass