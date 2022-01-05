import mysql.connector

#funcion conectar
def conectar():
    #conexion
    midb = mysql.connector.connect(
        host ='localhost',
        user ='root',
        password = 'root',
        database = 'empresa'
    )

    #objeto para poder ejecutar instrucciones sql
    cursor = midb.cursor()
    #retorna dos valores 0 = midb y cursor = 1
    return [midb, cursor]