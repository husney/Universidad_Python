from conexion import Conexion
from logBase import logger

class CursorPool:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None

    #Inicio de with        
    def __enter__(self):
        self.__conexion = Conexion.getConexion()
        self.__cursor = self.__conexion.cursor()
        logger.info("Inicio de with")
        return self.__cursor 

    def __exit__(self, exception_type, exception_value, exception_traceback):
        logger.info("Ejecutando el fin del with")
        if exception_type:
            self.__conexion.rollback()
            logger.warn(f"Se realiza roll back error {exception_type}")
        else:
            self.__conexion.commit()
            logger.info("Se realiza commit en la DB")
        self.__cursor.close()
        Conexion.leaveConexion(self.__conexion)

if __name__ == '__main__':
    conexion = CursorPool()
    with conexion as c:
        sql = "SELECT * FROM personas"
        c.execute(sql)
        datos = c.fetchall()
        for persona in datos:
            print(persona)
        
    
    