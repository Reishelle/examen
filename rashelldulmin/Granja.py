import gato
def construirgato(CantidadReproduccion,CantidadAnimales):
	g = gato.gato(CantidadReproduccion,CantidadAnimales)
	return g 
	
def imprimirmenu("1 Agregar  Nuevo Animal\n2 Alimentar Animales\n3 Dar de beber")
	print("4 salir")
	accion= int(input("Ingrese el numero de la accion que desea hacer"))
	return accion 
	
def imprimirAnimale():
	print("1 gato\n2")
	accion = int(input("Ingrese el numero de la accion que desea hacer"))
	return accion 

gatoconstruido=False
salir=False 

