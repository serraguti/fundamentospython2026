import oracledb

class OracleEmpleados:
    def __init__(self):
        self.connection = oracledb.connect(user="system", password="oracle"
                              , dsn="localhost/FREEPDB1")
    
    def eliminarEmpleado(self, idEmpleado):
        cursor = self.connection.cursor()
        sql = "delete from EMP where EMP_NO=:emp"
        cursor.execute(sql, (idEmpleado,))
        self.connection.commit()
        registros = cursor.rowcount
        cursor.close()
        return registros