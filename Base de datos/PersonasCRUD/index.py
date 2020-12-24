from PersonaCRUD import PersonaCrud
from PersonaEntity import Persona


#registros = PersonaCrud.seleccionarTodos()
#for persona in registros:
#    print(persona)
    
    
#datos = ("Insert", "Insert", "Insert")
#PersonaCrud.insertar(datos)

#datos = (31,)
#print(PersonaCrud.seleccionarUno(datos))

#datos = ("UPDATE", "UPDATE", "UPDATE", 32)
#PersonaCrud.actualizar(datos)

#datos = (32,)
#PersonaCrud.eliminar(datos)

#datos = (3,)
#print(PersonaCrud.seleccionarUno(datos))

#datos = PersonaCrud.seleccionarTodos()

#for persona in datos:
#   print(persona)

Laura = PersonaCrud.seleccionarUno((33, ))
Laura.setNombre("Lauriasdasta")
Laura.setApellido("Laurita")
Laura.setEmail("Laurita@Gmail.com")

PersonaCrud.actualizar(Laura)