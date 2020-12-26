from ConexionPool import ConexionPool
from LogBase import logger

class Cursor:

    def __init__(self):
        self.__conexion = None
        self.__cursor = None

    def __enter__(self):
        try:
            self.__conexion = ConexionPool.getConexion()
            self.__cursor =  self.__conexion.cursor()
            return self.__cursor
        except Exception as ex:
            logger.error(f"No se ha podido regresar el cursor {ex}")


    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type:
                self.__conexion.rollback()
                logger.error(f"No se guardaron los cambios en la Base de Datos {exc_type}")
            else:
                self.__conexion.commit()
            self.__cursor.close()
            ConexionPool.leaveConexion(self.__conexion)
        except Exception as ex:
            logger.log(f"Error: {ex}")


