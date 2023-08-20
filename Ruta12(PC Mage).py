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

def recorrerMatriz(par):
	for x in range(0, 8):
		for y in range(0, 2):
			for z in range(0, 16):
				if(Local[x][y][z] == par):
					return True, x , y, z
				 

def agregarProducto():
	resp, x, y, z = recorrerMatriz(None)
	if resp == True:
		producto = str(input("Ingrese el producto que quiere guardar: "))
		Local[x][y][z] = producto
		print("Se guardo el producto en el pasillo ", x+1, ", estantería ", y+1, ", pallet ", z+1)
	else:
		print("No hay espacios disponibles")

def buscarProducto():
	producto = str(input("Ingrese el producto que quiere buscar: "))
	resp, x, y, z = recorrerMatriz(producto)
	if resp == True:
		print("El producto se encuentra en el pasillo ", x+1, ", estantería ", y+1, ", pallet ", z+1)
	else:
		print("El producto ingresado no se encuentra en el local")

def egresarProducto(camion, destino):
	producto = str(input("Ingrese el producto que quiere egresar: "))
	resp, x, y, z = recorrerMatriz(producto)
	if resp == True:
		Local[x][y][z] = None
		print("Se egresó con éxito el producto\nFue transportado en el camión ", camion, " y su destino es ", destino)
		encontrado = True
	else:
		print("No existe el producto")
				

opc = int(1)
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