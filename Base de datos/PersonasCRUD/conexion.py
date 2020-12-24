import psycopg2
from logBase import logger 
import sys

class Conexion:    
    
    __USER = "postgres"
    __PASSWORD = "12345"
    __HOST = "localhost"
    __DB_PORT = "5432"
    __DATABASE = "testDb"
    __CONEXION = None
    
    
    @classmethod
    def __conectar(cls):
        try:
            cls.__CONEXION =  psycopg2.connect(user = cls.__USER,
                                    password = cls.__PASSWORD,
                                    host = cls.__HOST,
                                    database=cls.__DATABASE,
                                    port = cls.__DB_PORT)                
            return cls.__CONEXION
        except Exception as ex:
            print("Error al conectar a la Base de datos")
            logger.error(f"Error al conectar a la Base de datos {ex}")
            sys.exit()
    
    
    
    @classmethod
    def getConexion(cls):        
        return cls.__conectar()
            



    
    
    
    
    
    

