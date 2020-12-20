class DispositivoEntrada:
    
    """Crea objetos de tipo dispositovo entrada"""
    
    def __init__(self, tipoEntrada, marca):
        self.__tipoEntrada = tipoEntrada
        self.__marca = marca
        
    def getTipoEntrada(self):
        return self.__tipoEntrada
    
    def setTipoEntrada(self, tipoEntrada):
        self.__tipoEntrada = tipoEntrada
        
    def getMarca(self):
        return self.__marca
    
    def setMarca(self, marca):
        self.__marca = marca
        
    def __str__(self):
        return f"Tipo Entrada: {self.__tipoEntrada}\nMarca: {self.__marca}\n"
        
        