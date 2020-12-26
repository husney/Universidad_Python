from Conexion import Conexion
from LogBase import logger

class Cursor:

    def __init__(self):
        self.__conexion = None
        self.__cursor = None

    def __enter__(self):
        try:
            self.__conexion = Conexion.getConexion()
            self.__cursor = self.__conexion.cursor()
            return self.__cursor
        except Exception as ex:
            logger.error(f"Error al regresar el cursor {ex}")

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type:
                self.__conexion.rollback()
                logger.error(f"Ha ocurrido un error al guardar los datos en la Base de datos {exc_type}")
            else:
                self.__conexion.commit()
            self.__cursor.close()
            Conexion.leaveConexion(self.__conexion)
        except Exception as ex:
            logger.error(f"Ha ocurrido un error {ex}")





