import sys
from psycopg2 import pool
from logBase import logger

class Conexion:
    
    __HOST = "localhost"
    __PORT = "5432"
    __USER = "postgres"
    __PASSWORD = "12345"
    __DATABASE = "testDb"
    __MIN_CONEXIONES = 1
    __MAX_CONEXIONES = 5
    __POOL = None
    
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
                logger.error("Error al crear el pool")
        else:
            return cls.__POOL
        
    @classmethod
    def getConexion(cls):
        conexion =  cls.getPool().getconn()
        logger.info(f"Conexión establecida {conexion}")
        return conexion
    
    @classmethod
    def leaveConexion(cls, conexion):
        cls.getPool().putconn(conexion)
        print(f"Cerrando conexion {conexion}")
        
    @classmethod
    def closeConexiones(cls):
        cls.getPool().closeall()
        logger.info("Todas las conexiones han regresado al pool")
       
        
