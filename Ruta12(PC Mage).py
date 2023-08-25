import os
import random
class Palet:
	def __init__(self, cod, nom):
		self.codigo = cod
		self.nombre = nom
		self.destino = ""
		self.camion = ""
	
	def toString(self):
		print(str(self.codigo) + str(self.nombre) + self.destino + self.camion)

class Camion:
	def __init__(self, nom):
		self.nombre = nom
		self.trailer = []
		self.destino = ""

	def toString(self):
		print(self.trailer)
	
	def agregarPalet(self, palet):
		self.trailer.append(palet)
	
	def mostrarTrailer(self):
		aux = ""
		for x in self.trailer:
			aux += x + ", "
		print(aux)
			

Local = [
	[["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o"], 
	["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4"]],
	
	[["5", "6", "7", "8", "9", "10", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"], 
	["K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]],

	[["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o"], 
	["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4"]],

	[["5", "6", "7", "8", "9", "10", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"], 
	["K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]], 

	[["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o"], 
	["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4"]], 

	[["5", "6", "7", "8", "9", "10", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"], 
	["K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]], 

	[["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o"], 
	["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4"]], 

	[["5", "6", "7", "8", "9", "10", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"], 
	["K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]]
]

Destinos = ["París", "Tokio", "Río de Janeiro", "Nueva York", "Sydney", "Kioto", "Roma", "Estambul", "Vancouver", "Ciudad de México", "Dubái", "Venecia", "Moscú", "Chiang Mai", "Reykjavik", "Ciudad de Ho Chi Minh"]

Productos = ["Cepillo TurboMax para Mascotas", "Auriculares Sonido Cristalino", "Silla Ergonómica UltraComfort", "Cámara Instantánea SnapShot", "Tablet NovaPad 10X", "Robot Asistente Doméstico RoboHelp", "Juego de Ollas MasterChef", "Bicicleta Eléctrica EcoRide", "Pulsera Fitness PulseTrack", "Limpiador Automático SmartClean", "Termo Aislante HeatWave", "Batidora de Alta Velocidad TurboBlend", "Monitor Curvo CrystalView", "Videojuego Galactic Quest"]

Camiones = []

cantPalets = 0

def recorrerMatriz(par):
	for x in range(0, 8):
		for y in range(0, 2):
			for z in range(0, 16):
				if(Local[x][y][z] == par):
					return True, x , y, z

def llenarMatrizAleatoriamente():
	for x in range(0, 8):
		for y in range(0, 2):
			for z in range(0, 16):
				a = random.randint(1, 4)
				Local[x][y][z] = paletAleatorio(a)			

def paletAleatorio(num):
	global cantPalets
	if num == 1:
		cantPalets += 1
		p = Palet(str(cantPalets), Productos[random.randint(0, 13)])
		return p
	if num == 2:
		cantPalets += 1
		p = Palet(str(cantPalets), Productos[random.randint(0, 13)])
		p.destino = Destinos[random.randint(0, 15)]
		return p

	return(None)
		

def agregarProducto():
	resp, x, y, z = recorrerMatriz(None)
	if resp == True:
		nom = str(input("Ingrese el nombre del producto que quiere guardar: "))
		cod = str(input("Ingrese el codigo del producto que quiere guardar: "))
		producto = Palet(cod, nom)
		Local[x][y][z] = producto
		print("Se guardo el producto en el pasillo ", x+1, ", estantería ", y+1, ", pallet ", z+1)
	else:
		print("No hay espacios disponibles")

def buscarProducto():
	nomCodProducto = str(input("Ingrese el nombre o codigo del producto que quiere buscar: "))
	for x in range(0, 8):
		for y in range(0, 2):
			for z in range(0, 16):
				puntero = Local[x][y][z]
				if puntero != None: 
					if(puntero.nombre == nomCodProducto or puntero.codigo == nomCodProducto):
						print("El producto se encuentra en el pasillo ", x+1, ", estantería ", y+1, ", pallet ", z+1)
						puntero.toString()
						return
					
	print("El producto ingresado no se encuentra en el local")

def despacharProducto():

	def despacharAuto():
		for i in range(len(Camiones)):
			direccion = devolverMayorCantDire(0)
			camion = Camiones[i]
			camion.destino = direccion
			for x in range(0, 8):
				for y in range(0, 2):
					for z in range(0, 16):
						puntero = Local[x][y][z]
						if puntero != None: 
							if puntero.destino == direccion:
								camion.agregarPalet(puntero.nombre)
								Local[x][y][z] = None
			
			print("Los siguientes productos fueron despachados: ")
			camion.mostrarTrailer()
			print("Seran transportados en el camión ", camion.nombre, " y su destino es ", camion.destino)

	def despacharManual():

		nomCodProducto = str(input("Ingrese el nombre o codigo del producto que quiere egresar: "))
		opcCamion = int(input("Seleccione un camion disponible para llevar el envio:"))
		camionSel = Camiones[opcCamion-1]
		mostrarCamiones()

		for x in range(0, 8):
			for y in range(0, 2):
				for z in range(0, 16):
					puntero = Local[x][y][z]
					if puntero != None: 
						if(puntero.nombre == nomCodProducto or puntero.codigo == nomCodProducto):
							Local[x][y][z] = None
							if puntero.destino == "":
								print("El producto elegido no cuenta con direccion de destino")
								puntero.destino = str(input("ingrese destino: "))

							camionSel.destino = puntero.destino
							print("Se despacho el producto del pasillo ", x+1, ", estantería ", y+1, ", pallet ", z+1)
							print("Se egresó con éxito el producto\nFue transportado en el camión ", camionSel.nombre, " y su destino es ", camionSel.destino)
							print("El camion contiene los siguientes productos:")
							camionSel.mostrarTrailer()
							return
			
		
		else:
			print("No existe el producto")
	
	despacharAuto()
	despacharManual()

def mostrarCamiones():
	for x in Camiones:
		print(x.nombre)

def devolverMayorCantDire(puesto):
	arrDirecciones = []
	arrCant = []

	def compConArray(puntero):
		for x in range(len(arrDirecciones)):
			if arrDirecciones[x] == puntero.destino:
				return True , x
		return False , 0
	
	def sorter():
		for i in range(len(arrDirecciones)):
			for x in range(len(arrDirecciones)-1):
				if arrCant[x] < arrCant[x+1]:
					aux = arrCant[x+1]
					aux2 = arrDirecciones[x+1]
					arrCant[x+1]= arrCant[x]
					arrDirecciones[x+1]= arrDirecciones[x]
					arrCant[x] = aux
					arrDirecciones[x] = aux2
	
	for x in range(0, 8):
		for y in range(0, 2):
			for z in range(0, 16):
				puntero = Local[x][y][z]
				if puntero != None and puntero.destino != "": 
					resp, pos = compConArray(puntero)
					if resp != True:
						arrDirecciones.append(puntero.destino)
						arrCant.append(1)
					else:
						arrCant[pos] += 1
	
	sorter()
	return arrDirecciones[puesto] 			


opc = 1

cam1 = Camion("Camion de Javi")
cam2 = Camion("Camion de Pepe")
cam3 = Camion("Camion de Jose")

Camiones.append(cam1)
Camiones.append(cam2)
Camiones.append(cam3)

resp = str(input("Quiere llenar el almacen aleatoriamente? (y/n)"))
if resp == "y":
	llenarMatrizAleatoriamente()

while(True):
	opc2 = int(input("Que funcion quiere hacer\n1- Agregar un producto\n2- Buscar un producto\n3-Despachar un producto\n4-Ver informe\n5-Salir\n- "))

	if(opc2==1):
		agregarProducto()

	elif(opc2==2):
		buscarProducto()

	elif(opc2==3):
		despacharProducto()

	elif(opc2==4):
		print("En construccion")

	elif(opc == 5):
		break

os.system("pause")