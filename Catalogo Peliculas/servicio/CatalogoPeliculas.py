from dominio.Pelicula import Pelicula
import os

class CatalogoPeliculas:
    
    """Realiza operaciones sobre el archivo Peliculas.txt"""
    
    ruta_archivo = "Peliculas.txt"
    
    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            catalogo = open(CatalogoPeliculas.ruta_archivo, "a")
            catalogo.write("\n"+pelicula.__str__())            
        except Exception as ex:
            print("_________________")
            print("Ha ocurrido un error", ex)
            print(type(ex))
            print("_________________")
        else:
            print("_________________")
            print("Se ha guardado la pelicula correctamente")
            print("_________________")
        finally:
            catalogo.close()
            
    @staticmethod
    def listar_peliculas():
        try:
            catalogo = open(CatalogoPeliculas.ruta_archivo, "r")
            print(catalogo.read())
        except Exception as ex:
            print("_________________")
            print("Ha ocurrido un error", ex)
            print(type(ex))
            print("_________________")
        else:
            print("_________________")
            print("Fin del catalogo")
            print("_________________")
        finally:
            catalogo.close()
            
  
    @staticmethod
    def eliminar_pelicula():
        try:
            CatalogoPeliculas.listar_peliculas()
            peliculas = []  
            catalogo = open(CatalogoPeliculas.ruta_archivo, "r+")
            peliculas = catalogo.readlines()
            print(peliculas)
            numero = input("Ingrese el nombre de la película a borrar: ")
            categoria = input("Ingrese la categoria de la película: ")
            busqueda = str(peliculas.index(f"---PELICULA---\n Nombre: {numero}\n Categoria: {categoria}\n--------------\n"))
            print(peliculas.index(busqueda))
            
            #peliculas.remove(x)
            #catalogo.writelines(peliculas)            
        except Exception as ex:
            print("_________________")
            print("Ha ocurrido un error", ex)
            print(type(ex))
            print("_________________")
        else:
            print("_________________")
            print("Se ha eliminado correctamente la pelicula")
            print("_________________")
        finally:
            catalogo.close()
    
    @staticmethod
    def eliminar():
        os.remove(CatalogoPeliculas.ruta_archivo)