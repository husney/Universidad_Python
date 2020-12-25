from PersonaEntity import Persona
from cursorPool import CursorPool
from logBase import logger

class PersonaCrud:
    
    
    __SELECCIONARMULTIPLE = f"SELECT * FROM personas"
    __SELECCIONARUNO = "SELECT * FROM personas WHERE id = %s"
    __INSERT = "INSERT INTO personas (nombre, apellido, email) VALUES (%s, %s, %s)"
    __UPDATE = "UPDATE personas SET nombre = %s, apellido = %s, email = %s WHERE id = %s"
    __ELIMINAR = "DELETE FROM personas WHERE id = %s"
    
    @classmethod
    def seleccionarTodos(cls):
        with CursorPool() as c:
            try:            
                c.execute(PersonaCrud.__SELECCIONARMULTIPLE)            
                resultados = c.fetchall()            
                personas = []
                for persona in resultados:
                    resultado = Persona(persona[1], persona[2], persona[3])
                    resultado.setId(persona[0])
                    personas.append(resultado)
                return personas
            except Exception as ex:
                print(f"Ha ocurrido un error {ex}")
                logger.error(f"Ha ocurrido un error al seleccionar las personas {ex}")
        
            
    @classmethod
    def seleccionarUno(cls, id):
        with CursorPool() as c:        
            try:
                datos = (id,)
                c.execute(PersonaCrud.__SELECCIONARUNO, datos)
                resultados = c.fetchone()            
                persona = Persona(resultados[1],resultados[2], resultados[3]) 
                persona.setId(resultados[0]) 
                return persona
            except Exception as ex:
                print(f"Ha ocurrido un error {ex}")
                logger.error(f"Ha ocurrido un error al seleccionar una persona {ex}")
            
            
    
    @classmethod
    def insertar(cls, persona):
        with CursorPool() as c:
            try:                
                datos = (persona.getNombre(), persona.getApellido(), persona.getEmail())
                c.execute(PersonaCrud.__INSERT, datos)                
            except Exception as ex:                
                print(f"Ha ocurrido un error{ex}")
                logger.error(f"Ha ocurrido un error al insertar una persona {ex}")            
            else:
                print(f"Registrado correctamente")
            
    @classmethod
    def actualizar(cls, persona):
        with CursorPool() as c:
            try:
                datos = (persona.getNombre(), persona.getApellido(), persona.getEmail(), persona.getId())
                c.execute(cls.__UPDATE, datos)                
            except Exception as ex:                
                print("Error al actualizar registro")
                logger.error(f"Error al actualizar el registro {persona} | {ex}")
            else:
                print("Cambios Realizados correctamente registros afectados :", c.rowcount)
            
      
        
    @classmethod
    def eliminar(cls, id):
        with CursorPool() as c:
            try:
                datos = (id,)
                c.execute(PersonaCrud.__ELIMINAR, datos)
            except Exception as ex:
                print(f"Ha ocurrido un errror {ex}")                
            else:
                print("Se ha eliminado el registro correctamente")
        
        
if __name__ == '__main__':
    # datos = PersonaCrud.seleccionarTodos()
    # for persona in datos:
    #     print(persona)
    
    # p = Persona("INSERTN", "INSERTN", "INSERTN")
    # PersonaCrud.insertar(p)
    
    # p = Persona("UPDATEN", "UPDATEN", "UPDATEN")
    # p.setId(34)
    # PersonaCrud.actualizar(p)
    
    # datos = PersonaCrud.seleccionarUno(34)
    # print(datos)
    
    PersonaCrud.eliminar(34)