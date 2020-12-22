class DispositivoEntrada:
    
    """Crea objetos de tipo dispositovo entrada"""
    
    def __init__(self, tipoEntrada, marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca
        
    def getTipoEntrada(self):
        return self._tipoEntrada
    
    def setTipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada
        
    def getMarca(self):
        return self._marca
    
    def setMarca(self, marca):
        self._marca = marca
        
    def __str__(self):
        return f"Tipo Entrada: {self._tipoEntrada}\nMarca: {self._marca}\n"
        
        