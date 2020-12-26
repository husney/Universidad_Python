from UsuarioCrud import UsuarioCrud
from UsuarioEntity import Usuario

def seleccionarTodos():
    usuarios = UsuarioCrud.seleccionarTodos()
    for usuario in usuarios:
        print(usuario)

def seleccionarUno(regreso = False):
    id = int(input("Por favor ingrese el id del usuario a buscar: "))
    try:
        usuario = UsuarioCrud.seleccionarUno(id)
        print(usuario)
        if regreso:
            return usuario
    except:
        print("El usuario no existe")

def insertar():
    nombre = input("Por favor ingrese el nombre del nuevo usuario: ")
    password = input("Por favor ingrese la contraseña del usuario: ")
    usuario = Usuario(nombre, password)
    UsuarioCrud.insertar(usuario)

def actualizar():
    opt = 0
    while opt != 1:
        usuario = seleccionarUno(True)
        opt = int(input("¿Confirma que el usuario seleccionado es el que se va a actualizar?\n1) Si\n2) No\n: "))
    nuevoNombre = input("Por favor ingrese el nuevo nombre: ")
    nuevaPass = input("Por favor ingrese la nueva contraseña: ")
    usuario.setNombre(nuevoNombre)
    usuario.setPassword(nuevaPass)
    UsuarioCrud.actualizar(usuario)

def eliminar():
    opt = 0
    while opt != 1:
        usuario = seleccionarUno(True)
        opt = int(input("¿Confirma que el usuario a eliminar es el seleccionado?\n1) Si\n2) No\n: "))
    UsuarioCrud.eliminar(usuario.getId())


opcion = 0
while opcion != 6:
    opcion = int(input("1) Seleccionar todos los usuarios\n2) Seleccionar un usurio\n3) Registrar un usuario\n4) Acutalizar un usuario\n5) Eliminar un usuario\n6) Salir\n: "))
    if opcion == 1:
        seleccionarTodos()
    if opcion == 2:
        seleccionarUno()
    if opcion == 3:
        insertar()
    if opcion == 4:
        actualizar()
    if opcion == 5:
        eliminar()
    if opcion == 6:
        print("Muchas garacias...")


