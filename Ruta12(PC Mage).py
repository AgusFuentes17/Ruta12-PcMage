import os
import random
from datetime import date

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
			
class Informe:
	def __init__(self, tipo, destino, ubicacion, nombre):
		self.tipo = str(tipo)
		self.nombre = str(nombre)
		self.fecha = date.today()
		self.destino = str(destino)
		self.ubicacion = ubicacion
	
	def toString(self):
		aux = self.tipo +"\n"+ str(self.fecha)+"\n"
		if self.tipo == "Despacho":
			aux += "Se despacho un "+ self.nombre + " con destino a " + self.destino +"\n"
		else:
			aux += "Se deposito un " + str(self.nombre) + " en el pasillo " + str(self.ubicacion[0]+1) + ", estanteria " + str(self.ubicacion[1]+1) + ", posicion "+ str(self.ubicacion[2]+1)+"\n"
		print(aux)

Local = [
	[[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]],
	
	[[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]],

	[[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]],

	[[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]], 

	[[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]], 

	[[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]], 

	[[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]], 

	[[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 
	[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]]
]

Destinos = ["París", "Tokio", "Río de Janeiro", "Nueva York", "Sydney", "Kioto", "Roma", "Estambul", "Vancouver", "Ciudad de México", "Dubái", "Venecia", "Moscú", "Chiang Mai", "Reykjavik", "Ciudad de Ho Chi Minh"]

Productos = ["Cepillo TurboMax para Mascotas", "Auriculares Sonido Cristalino", "Silla Ergonómica UltraComfort", "Cámara Instantánea SnapShot", "Tablet NovaPad 10X", "Robot Asistente Doméstico RoboHelp", "Juego de Ollas MasterChef", "Bicicleta Eléctrica EcoRide", "Pulsera Fitness PulseTrack", "Limpiador Automático SmartClean", "Termo Aislante HeatWave", "Batidora de Alta Velocidad TurboBlend", "Monitor Curvo CrystalView", "Videojuego Galactic Quest"]

Camiones = []

Informes = []

cantPalets = 0
vecesLleno = 0
totalDespachados = 0

def mostrarEstado():
	print("[X] = Ocupado\n[0] = Vacio")
	for x in range(len(Local)):
		print("Pasillo ", x+1,":")
		for y in Local[x]:
			aux = "Estanteria:"
			for z in y:
				if z == None:
					aux += "[0]"
				else:
					aux += "[X]"
			print(aux)
		print("\n")

def buscarLugarVacio():
	global vecesLleno
	for x in range(0, 8):
		for y in range(0, 2):
			for z in range(0, 16):
				if(Local[x][y][z] == None):
					return True, x , y, z
	vecesLleno += 1
	return False, 0, 0, 0

def llenarMatrizAleatoriamente(lleno):
	for x in range(0, 8):
		for y in range(0, 2):
			for z in range(0, 16):
				if lleno:
					Local[x][y][z] = paletAleatorio(2)
					p = Local[x][y][z]
					Informes.append(Informe("Ingreso", None, [x,y,z], p.nombre))
				else:
					a = random.randint(1, 4)
					Local[x][y][z] = paletAleatorio(a)
					p = Local[x][y][z]
					if p != None:
						Informes.append(Informe("Ingreso", None, [x,y,z], p.nombre))

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
	resp, x, y, z = buscarLugarVacio()
	if resp == True:
		global cantPalets
		nom = str(input("Ingrese el nombre del producto que quiere guardar: "))
		cantPalets += 1
		cod = cantPalets
		producto = Palet(cod, nom)
		Local[x][y][z] = producto
		
		Informes.append(Informe("Ingreso", None, [x,y,z], nom))

		print("Se guardo el producto en el pasillo ", x+1, ", estantería ", y+1, ", pallet ", z+1 , "el codigo es:", cod)
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
		global totalDespachados
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
								totalDespachados += 1
								Informes.append(Informe("Despacho", puntero.destino, None, puntero.nombre))
			
			print("Los siguientes productos fueron despachados: ")
			camion.mostrarTrailer()
			print("Seran transportados en el camión ", camion.nombre, " y su destino es ", camion.destino , "\n")
			camion.trailer = []

	def despacharManual():
		global totalDespachados
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
							
							if puntero.destino == "":
								print("El producto elegido no cuenta con direccion de destino")
								puntero.destino = str(input("ingrese destino: "))

							Local[x][y][z] = None
							totalDespachados += 1
							camionSel.destino = puntero.destino

							Informes.append(Informe("Despacho", puntero.destino, None, puntero.nombre))

							print("Se despacho el producto del pasillo ", x+1, ", estantería ", y+1, ", pallet ", z+1)
							print("Se egresó con éxito el producto\nFue transportado en el camión ", camionSel.nombre, " y su destino es ", camionSel.destino)
							print("El camion contiene los siguientes productos:")
							camionSel.mostrarTrailer()
							return
			
		
		else:
			print("No existe el producto")
	
	opc = int(input("Que desea hacer: \n1-Despachar automaticamente (Agrupara los palets por destinaciones y despachara la mayor cantidad posible usando un camion, utilizara todos los camiones)\n2-Despachar manualmente\n- "))
	os.system("cls")
	match opc:
		case 1:
			despacharAuto()
		case 2:
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

def mostrarInforme():
	print("Cantidad de veces que se lleno el almacen:")
	print(vecesLleno)
	print("Cantidad de palets ingresados al almacen en total:")
	print(cantPalets)
	print("Cantidad de palets despachados del almacen en total:")
	print(totalDespachados)
	print("\n### Informes ###\n")
	for x in Informes:
		x.toString()


cam1 = Camion("Camion de Javi")
cam2 = Camion("Camion de Pepe")
cam3 = Camion("Camion de Jose")

Camiones.append(cam1)
Camiones.append(cam2)
Camiones.append(cam3)

resp = str(input("Quiere llenar el almacen aleatoriamente?('a' Creara cierta cantidad de palets y los pondra en lugares aleatorios, 'll' llenara el almacen entero de palets aleatorios, solo para testeo) [ll/a/n]"))
if resp == "ll":
	llenarMatrizAleatoriamente(True)
if resp == "a":
	llenarMatrizAleatoriamente(False)

while(True):
	os.system("cls")
	opc2 = int(input("Que funcion quiere hacer\n1-Agregar un producto\n2-Buscar un producto\n3-Despachar un producto\n4-Ver informe\n5-Mostrar estado del almacen\n6-Salir\n- "))
	os.system("cls")
	match opc2:
		case 1:
			agregarProducto()
		case 2:
			buscarProducto()
		case 3:
			despacharProducto()
		case 4:
			mostrarInforme()
		case 5:
			mostrarEstado()
		case 6:
			break
	input("Toque cualquier tecla para continuar")
os.system("pause")