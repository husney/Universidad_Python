from UsuarioCrud import UsuarioCrud
from UsuarioEntity import Usuario
opcion = 0

def listarTodos():
    usuarios = UsuarioCrud.seleccionarTodos()
    for usuario in usuarios:
        print(usuario)

def listarUno(retorno = False):
    id = int(input("Por favor ingrese el identificador del usuario a seleccionar: "))
    usuario = UsuarioCrud.seleccionarUno(id)
    print(usuario)
    if retorno == True:
        return usuario

def insertar():
    nombre = input("Por favor ingrse el nombre del nuevo usuario: ")
    password = input("Por favor ingrese la contraseña del nuevo usuario: ")
    usuario = Usuario(nombre, password)
    UsuarioCrud.insertar(usuario)

def actualizar():
    opt = 2
    while opt == 2:
        usuario = listarUno(True)
        opt = int(input("¿Confirma que el usuario a actualizar es el seleccionado?\n1) Si\n2) No\n: "))
    nuevoNombre = input("Por favor ingrese el nuevo nombre del usuario: ")
    nuevaPassword = input("Por favor ingrese la nueva contraseña del usuario: ")
    usuario.setNombre(nuevoNombre)
    usuario.setPassword(nuevaPassword)
    UsuarioCrud.actualizar(usuario)

def eliminar():
    opt = 2
    while opt == 2:
        usuario = listarUno(True)
        opt = int(input("¿Confirma que el usuario a eliminar es el seleccionado?\n1) Si\n2) No\n: "))
    UsuarioCrud.eliminar(usuario.getId())

while opcion != 6:
    opcion = int(input("Por favor escoja una opción:\n1) Listar Usuarios\n2) Listar un Usuario\n3) Ingresar Usuario\n4) Actualizar usuario\n5) Eliminar usuario\n6) Salir\n: "))

    if opcion == 1:
        listarTodos()
    if opcion == 2:
        listarUno()
    if opcion == 3:
        insertar()
    if opcion == 4:
        actualizar()
    if opcion == 5:
        eliminar()
    if opcion == 6:
        print("Muchas gracias")
