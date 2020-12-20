from Monitor import Monitor
from Orden import Orden
from Mouse import Mouse
from Teclado import Teclado
from TiposEntrada import TiposEntrada
from Computadora import Computadora

pMonitor = Monitor(TiposEntrada.vga.name, "Dell", 24)
pMouse = Mouse("Prueba", "Prueba")
pTeclado = Teclado("Prueba", "Prueba", "Mecanico")
pComputador = Computadora("Computadora", pMonitor, pTeclado, pMouse)
pComputador2 = Computadora("Computadora", pMonitor, pTeclado, pMouse)
#print(pMonitor)
#print(pMouse)
#print(pTeclado)
#print()
#print(pComputador)

pOrden = Orden()
pOrden.agregarComputadora(pComputador)
pOrden.agregarComputadora(pComputador2)
print(pOrden)