from Cursor import Cursor
from LogBase import logger
from UsuarioEntity import Usuario

class UsuarioCrud:

    __SELECCIONARTODOS = "SELECT * FROM usuarios"
    __SELECCIONAR_UNO = "SELECT * FROM usuarios WHERE id = %s"
    __INSERTAR = "INSERT INTO usuarios(nombre, password) VALUES (%s, %s)"
    __ACTUALIZAR = "UPDATE usuarios SET nombre = %s, password = %s WHERE id = %s"
    __ELIMINAR = "DELETE FROM usuarios WHERE id = %s"


    @classmethod
    def seleccionarTodos(cls):
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
        with Cursor() as c:
            datos = (id,)
            c.execute(cls.__SELECCIONAR_UNO, datos)
            resultado = c.fetchone()
            user = Usuario(resultado[1], resultado[2])
            user.setId(resultado[0])
            return user

    @classmethod
    def insertar(cls, usuario):
        try:
            with Cursor() as c:
                datos = (usuario.getNombre(), usuario.getPassword())
                c.execute(cls.__INSERTAR, datos)
        except Exception as ex:
            logger.error(f"No se ha podido insertar un registro {usuario} error: {ex}")
        else:
            print("Registro ingresado correctamente\n")

    @classmethod
    def actualizar(cls, usuario):
        try:
            with Cursor() as c:
                datos = (usuario.getNombre(), usuario.getPassword(), usuario.getId())
                c.execute(cls.__ACTUALIZAR, datos)
        except Exception as ex:
            logger.error(f"No se pudo actualizar el usuario {usuario} error: {ex}")
        else:
            print(f"Se ha acutalizado correctamente el usuario {usuario.getNombre()}\n")

    @classmethod
    def eliminar(cls, id):
        try:
            with Cursor() as c:
                datos = (id,)
                c.execute(cls.__ELIMINAR, datos)
        except Exception as ex:
            logger.error(f"No se ha podido eliminar un registro {ex}")
        else:
            print("Registro eliminado correctamente\n")