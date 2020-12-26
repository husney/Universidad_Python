from LogBase import logger
from psycopg2 import pool
import sys

class ConexionPool:

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
                                                        host = cls.__HOST,
                                                        port = cls.__PORT,
                                                        user = cls.__USER,
                                                        password = cls.__PASSWORD,
                                                        database = cls.__DATABASE
                                                        )
                return cls.__POOL

            except Exception as ex:
                logger.critical(f"No se ha realizado el pool {ex}")
                sys.exit()
        else:
            return cls.__POOL


    @classmethod
    def getConexion(cls):
            try:
                return cls.getPool().getconn()
            except Exception as ex:
                logger.error(f"No se pudo obtener la conexion del pool {ex}")



    @classmethod
    def leaveConexion(cls, conexion):
        try:
            cls.getPool().putconn(conexion)
        except Exception as ex:
            print(f"No se ha regresado la conexión al pool {conexion}\nError: {ex}")


    @classmethod
    def closePool(cls):
        try:
            cls.getPool().closeall()
        except Exception as ex:
            logger.error("No se ha podido cerrar el pool {ex}")