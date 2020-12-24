from conexion import Conexion
from PersonaEntity import Persona
from logBase import logger

class PersonaCrud:
    
    
    __SELECCIONARMULTIPLE = f"SELECT * FROM personas"
    __SELECCIONARUNO = "SELECT * FROM personas WHERE id = %s"
    __INSERT = "INSERT INTO personas (nombre, apellido, email) VALUES (%s, %s, %s)"
    __UPDATE = "UPDATE personas SET nombre = %s, apellido = %s, email = %s WHERE id = %s"
    __ELIMINAR = "DELETE FROM personas WHERE id = %s"
    
    @classmethod
    def seleccionarTodos(cls):
        try:
            c = Conexion.getConexion()
            cursor = c.cursor()            
            cursor.execute(PersonaCrud.__SELECCIONARMULTIPLE)            
            resultados = cursor.fetchall()            
            personas = []
            for persona in resultados:
                resultado = Persona(persona[1], persona[2], persona[3])
                resultado.setId(persona[0])
                personas.append(resultado)
            return personas
            
        except Exception as ex:
            print(f"Ha ocurrido un error {ex}")
            logger.error(f"Ha ocurrido un error al seleccionar las personas {ex}")
        finally:
           cursor.close()
           c.close()
            
    @classmethod
    def seleccionarUno(cls, datos):
        try:
            c = Conexion.getConexion()
            cursor = c.cursor()
            cursor.execute(PersonaCrud.__SELECCIONARUNO, datos)
            resultados = cursor.fetchone()            
            persona = Persona(resultados[1],resultados[2], resultados[3]) 
            persona.setId(resultados[0]) 
            return persona
        except Exception as ex:
            print(f"Ha ocurrido un error {ex}")
            logger.error(f"Ha ocurrido un error al seleccionar una persona {ex}")
        finally:
           cursor.close()
           c.close()
        
    
    @classmethod
    def insertar(cls, persona):
        try:
            c = Conexion.getConexion()
            cursor = c.cursor()            
            datos = (persona.getNombre(), persona.getApellido(), persona.getEmail())
            cursor.execute(PersonaCrud.__INSERT, datos)
            c.commit()
        except Exception as ex:
            c.rollback()
            print(f"Ha ocurrido un error{ex}")
            logger.error(f"Ha ocurrido un error al insertar una persona {ex}")            
        else:
            print(f"Registrado correctamente")
        finally:
            cursor.close()
            c.close()
            
    @classmethod
    def actualizar(cls, persona):
        try:
            c = Conexion.getConexion()
            cursor = c.cursor()
            datos = (persona.getNombre(), persona.getApellido(), persona.getEmail(), persona.getId())
            cursor.execute(cls.__UPDATE, datos)
            c.commit()
        except Exception as ex:
            c.rollback()
            print("Error al actualizar registro")
            logger.error(f"Error al actualizar el registro {persona} | {ex}")
        else:
            print("Cambios Realizados correctamente registros afectados :", cursor.rowcount)
            
      
        
    @classmethod
    def eliminar(cls, datos):
        try:
            c = Conexion.getConexion()
            cursor = c.cursor()
            cursor.execute(PersonaCrud.__ELIMINAR, datos)
            c.commit()
            
        except Exception as ex:
            print(f"Ha ocurrido un errror {ex}")
            c.rollback()
        else:
            print("Se ha eliminado el registro correctamente")
        finally:
            cursor.close()
            c.close()
        
        
    