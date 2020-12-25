from psycopg2 import pool
from logBase import logger
import sys

class Conexion:
    
    __USER = "postgres"
    __PASSWORD = "12345"
    __HOST = "localhost"
    __PORT = "5432"
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
                                            host=cls.__HOST,
                                            user=cls.__USER,
                                            password=cls.__PASSWORD,
                                            port=cls.__PORT,
                                            database=cls.__DATABASE)
                
                return cls.__POOL
            except Exception as e:
                
                sys.exit()
        else:
            return cls.__POOL
        
    @classmethod
    def getConexion(cls):
        conexion =  cls.getPool().getconn()
        logger.debug(f"Se ha creado la conexión {conexion}")
            
    @classmethod
    def liberarConexion(cls, conexion):
        #Regresar el objeto conexion al pool
        cls.getPool().putconn(conexion)
        logger.debug(f'Regresamos la conexion al pool: {conexion}')
        logger.debug(f'Estado del pool: {cls.__pool}')
       
    @classmethod
    def closeConexiones(cls):
        cls.getPool().closeall()
        logger.debug(f"Se cierran todas las conexiones del pool {cls.__POOL}")


conexion1 = Conexion.getConexion()
conexion2 = Conexion.getConexion()
#conexion3 = Conexion.getConexion()
#conexion4 = Conexion.getConexion()
#conexion5 = Conexion.getConexion()

Conexion.liberarConexion(conexion2)

