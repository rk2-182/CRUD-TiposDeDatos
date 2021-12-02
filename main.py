import os
import db #importamos archivo con la conexion
import datetime

#creamos una instancia del archivo que contiene la conexion y su funcion
connect = db.conexion()

#valores retornados de la funcion
bd = connect[0]
cursor = connect[1]


#Funion para mostrar datos de las tablas
def mostrarDatos(opcion):
    if opcion == 1:
        cursor.execute("select * from proveedor")
        resultado = cursor.fetchall()
        os.system('cls')
        print("Tabla Proveedor")
        print("---------------")
        for i in resultado:
            print(i)
    elif opcion == 2:
        cursor.execute("select * from productos")
        resultado = cursor.fetchall()
        os.system('cls')
        print("Tabla Productos")
        print("---------------")
        for i in resultado:
            print(i)

def insertarDatosProveedor():
    sql = 'insert into proveedor (nombre,direccion) values (%s,%s)'
    valores = ('losperros banquetera','Napoles N°999')
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
    fechaNac = datetime.date(año,mes,dia)
    telefono = input("Ingrese tu numero telefonico: ")

    sql = 'insert into cliente (dni,nombre,fechaNac,telefono) values (%s,%s,%s,%s)'
    datos = (dni,nombre,fechaNac,telefono)
    cursor.execute(sql,datos)
    bd.commit()

    if cursor.rowcount == 1:
        print("Datos ingresados")
    else:
        print("Error al ingresar datos")




print("----------Empresa 1.0----------\n")
print("1.-Proveedor")
print("2.-Productos")
opcion=int(input("¿Que datos desea revisar?: "))

if opcion==1:
    mostrarDatos(1)
elif opcion==2:
    mostrarDatos(2)
else:
    print("Opcion erronea")


print("Ingresando datos cliente")
insertarDatosCliente()



