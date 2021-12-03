import CRUD
import os



#*****Menu*****
def Menu():
    os.system('cls')
    while True:
        
        print("")
        print("========Empresa 1.0========\n")

        print("1.-Revisar Datos de la Empresa")
        print("2.-Ingresar Datos de la Empresa")
        print("3.-Actualizar Datos de la Empresa")
        print("4.-Eliminar Datos de la Empresa")
        print("6.-Salir")

        opcion = int(input("Seleccione Una Opción: "))


        if opcion == 1:
            print("¿Que datos desea revisar?: ")
            print("1.-Proveedor")
            print("2.-Productos")
            print("3.-Clientes")
            op = int(input("Ingresa la opción:"))
            if op==1:
                datos = CRUD.mostrarDatos(1)
                if len(datos)>=1:
                   print(datos)
                   print(type(datos))
                   print(len(datos))
                else:
                    print("No se encuentran datos registrados")
            elif op==2:
                CRUD.mostrarDatos(2)
            elif op ==3:
                CRUD.mostrarDatos(3)
            else:
                print("Opcion erronea")
        elif opcion == 2:
            print("¿Donde desea ingresar datos?")
            print("1.-Proveedor")
            print("2.-Productos")
            print("3.-Clientes")
            op = int(input("Ingresa la opción:"))
            if op==1:
                CRUD.insertarDatosProveedor()
            elif op==2:
                CRUD.insertarDatosProducto()
            elif op ==3:
                CRUD.insertarDatosCliente()
            else:
                print("Opcion erronea")

        
        elif opcion ==6:
            print("Adios!")
            break
        else:
            print("Opcion erronea")


#*******************Ejecutar*********************
Menu()


