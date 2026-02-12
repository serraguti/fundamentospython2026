import oracledb

class OracleEnfermos:
    #Declarar las propiedades en el Constructor
    def __init__(self):
        self.connection = oracledb.connect(user="system", password="oracle"
                              , dsn="localhost/FREEPDB1")
    
    #Los metodos que deseemos.
    def eliminarEnfermo(self, inscripcion):
        #Creamos un nuevo cursor: Entrar
        cursor = self.connection.cursor()
        sql = "delete from ENFERMO where INSCRIPCION=:ins"
        cursor.execute(sql, (inscripcion,))
        registros = cursor.rowcount
        self.connection.commit()
        #Cerramos el cursor: Salimos
        cursor.close()
        return registros
        
    
    