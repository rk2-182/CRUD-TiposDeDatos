import mysql.connector

class DAO():

    def conexion():

        def __init__(self):
            try:
                self.midb= mysql.connector.connect(
                host='localhost',
                user='root',
                password='root',
                database='empresa'
            )
            except NameError as ex:
                print("Error al intentar la conexion: {0}".format(ex))
                #Objeto para poder ejecutar instrucciones sql
                self.cursor = self.midb.cursor()

                #retorna dos valores 0 = midb y cursor = 1
                return [self.midb,self.cursor]
