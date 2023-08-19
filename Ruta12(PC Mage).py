import os

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


def agregarProducto():
	espacioDisponible = False
	producto = str(input("Ingrese el producto que quiere guardar: "))
	for x in range(0, 8):
		for y in range(0, 2):
			for z in range(0, 16):
				if(Local[x][y][z] == None):
					Local[x][y][z] = producto
					print("Se guardo el producto en el pasillo ", x+1, ", estantería ", y+1, ", palet ", z+1)
					espacioDisponible = True

	if(espacioDisponible==False):
		print("No hay espacios disponibles")

def buscarProducto():
	encontrado = False
	producto = str(input("Ingrese el producto que quiere buscar: "))
	for x in range(0, 8):
		for y in range(0, 2):
			for z in range(0, 16):
				if(Local[x][y][z]==producto):
					print("El producto se encuentra en el pasillo ", x+1, ", estantería ", y+1, ", palet ", z+1)
					encontrado = True

	if(encontrado==False):
		print("El producto ingresado no se encuentra en el local")

def egresarProducto():
	encontrado = False
	camion = 1
	destino = "calamuchita"
	producto = str(input("Ingrese el producto que quiere egresar: "))
	for x in range(0, 8):
		for y in range(0, 2):
			for z in range(0, 16):
				if(Local[x][y][z] == producto):
					Local[x][y][z] = None
					print("Se egresó con éxito el producto\nFue transportado en el camión ", camion, " y su destino es ", destino)
					encontrado = True

	if(encontrado==False):
		print("No existe el producto")
				
def verInforme():
	

opc = 1
while(opc==1):
	opc2 = int(input("Que funcion quiere hacer\n1- Agregar un producto\n2- Buscar un producto\n3-Egresar un producto\n4-Ver informe\n: "))

	if(opc2==1):
		agregarProducto()

	elif(opc2==2):
		buscarProducto()

	elif(opc2==3):
		egresarProducto()

	elif(opc2==4):
		print("En construccion")

	opc = int(input("Que quiere hacer\n1-Seguir\n2-Cerrar\n: "))

os.system("pause")