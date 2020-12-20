from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas

usando = True

def agregarPeliculaCatalogo():
    nombre = input("Nombre de la película: ")
    categoria = input("Categoria de la película: ")
    CatalogoPeliculas.agregar_pelicula(Pelicula(nombre, categoria))

def listarPeliculas():
    CatalogoPeliculas.listar_peliculas()
    
def eliminarCatalogo():
    CatalogoPeliculas.eliminar()

while usando:
    
    opt = int(input("1) Agregar película\n2) Listar películas\n3) Eliminar catalogo \n4) Salir del menú \n"))
    
    if opt == 1:
       agregarPeliculaCatalogo()
    elif opt == 2:
        listarPeliculas()
    elif opt == 3:
        eliminarCatalogo()
    elif opt == 4:
        usando = False
        print("Muchas gracias")


        
    
    

