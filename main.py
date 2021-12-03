import CRUD
import os



#*****Menu*****
def Menu():
    os.system('cls')
    print("========Empresa 1.0========\n")

    print("1.-Revisar Datos de la Empresa")
    print("2.-Ingresar Datos a la Empresa")

    opcion = int(input("Seleccione Una Opción: "))


    if opcion == 1:
        print("¿Que datos desea revisar?: ")
        print("1.-Proveedor")
        print("2.-Productos")
        print("3.-Clientes")
        op = int(input("Ingresa la opción:"))
        if op==1:
            CRUD.mostrarDatos(1)
        elif op==2:
            CRUD.mostrarDatos(2)
        elif op ==3:
            CRUD.mostrarDatos(3)
        else:
            print("Opcion erronea")
    else:
        print("Opcion erronea")


Menu()


