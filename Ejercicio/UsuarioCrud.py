from Cursor import Cursor
from LogBase import logger
from UsuarioEntity import Usuario

class UsuarioCrud:

    __SELECCIONARTODOS = "SELECT * FROM usuarios"
    __SELECCIONARUNO = "SELECT * FROM usuarios WHERE id = %s"
    __INSERTAR = "INSERT INTO usuarios(nombre, password) VALUES (%s, %s)"
    __ACTUALIZAR = "UPDATE usuarios SET nombre = %s, password = %s WHERE id = %s"
    __ELIMINAR = "DELETE FROM usuarios WHERE id = %s"

    @classmethod
    def seleccionarTodos(cls):
        """Selecciona todos los usuarios registrados"""

        with Cursor() as c:
            c.execute(cls.__SELECCIONARTODOS)
            resultados = c.fetchall()
            usuarios = []
            for usuario in resultados:
                user = Usuario(usuario[1], usuario[2])
                user.setId(usuario[0])
                usuarios.append(user)
            return usuarios


    @classmethod
    def seleccionarUno(cls, id):
        """Selecciona un Usuario por ID"""

        with Cursor() as c:
            datos = (id,)
            c.execute(cls.__SELECCIONARUNO, datos)
            resultado = c.fetchone()
            usuario = Usuario(resultado[1], resultado[2])
            usuario.setId(resultado[0])
            return usuario

    @classmethod
    def insertar(cls, usuario):
        """Registra un usuario en la Base de Datos"""

        try:
            with Cursor() as c:
                datos = (usuario.getNombre(), usuario.getPassword())
                c.execute(cls.__INSERTAR, datos)
        except Exception as ex:
            logger.error(f"No se ha podido registrar el usuario: {usuario.getNombre()}\nError: {ex}")
        else:
            print(f"Usuario {usuario.getNombre()} registrado correctamente")

    @classmethod
    def actualizar(cls, usuario):
        try:
            with Cursor() as c:
                datos = (usuario.getNombre(), usuario.getPassword(), usuario.getId())
                c.execute(cls.__ACTUALIZAR, datos)
        except Exception as ex:
            logger.error(f"No se pudo actualizar el usuario {usuario.getNombre()}")
        else:
            print(f"{usuario.getNombre()} acutalizado correctamente")

    @classmethod
    def eliminar(cls, id):
        try:
            with Cursor() as c:
                datos = (id,)
                c.execute(cls.__ELIMINAR, datos)
        except Exception as ex:
            logger.error(f"No se ha podido eliminar el usuario con el id: {id}")
        else:
            print(f"Se ha eliminado correctamente el usuario con el id: {id}")