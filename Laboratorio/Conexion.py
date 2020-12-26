from psycopg2 import pool
from LogBase import logger

class Conexion:

    __HOST = "localhost"
    __PORT = "5432"
    __USER = "postgres"
    __PASSWORD = "12345"
    __DATABASE = "testDb"
    __POOL = None
    __MIN_CONEXIONES = 1
    __MAX_CONEXIONES = 5

    @classmethod
    def getPool(cls):
        if cls.__POOL is None:
            try:
                cls.__POOL = pool.SimpleConnectionPool(
                                                        cls.__MIN_CONEXIONES,
                                                        cls.__MAX_CONEXIONES,
                                                        host=cls.__HOST,
                                                        port=cls.__PORT,
                                                        user=cls.__USER,
                                                        password=cls.__PASSWORD,
                                                        database=cls.__DATABASE
                                                        )
                return cls.__POOL
            except Exception as ex:
                logger.error(f"No se ha realizado el pool de conexiones error: {ex}")
        else:
            return cls.__POOL


    @classmethod
    def getConexion(cls):
        try:
            return cls.getPool().getconn()
        except Exception as ex:
            logger.error(f"No se ha podido asignar un aconexión error: {ex}")

    @classmethod
    def leaveConexion(cls, conexion):
        try:
            cls.getPool().putconn(conexion)
        except Exception as ex:
            logger.error(f"Error al regresar conexión {ex}")


    @classmethod
    def closePool(cls):
        try:
            cls.getPool().closeall()
            print("Pool cerrado")
        except Exception as ex:
            logger.error(f"Error al cerrar el pool {ex}")

