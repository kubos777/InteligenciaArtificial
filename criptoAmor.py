#-*- coding:utf-8-*-	
import os
def asciiart():
	"""
	Función que me imprime un mensaje con ASCII art
	"""
	print("""
	 _____      _       _                         __        
	/  __ \    (_)     | |                       / _|/_/      
	| /  \/_ __ _ _ __ | |_ ___   __ _ _ __ __ _| |_ _  __ _ 
	| |   | '__| | '_ \| __/ _ \ / _` | '__/ _` |  _| |/ _` |
	| \__/\ |  | | |_) | || (_) | (_| | | | (_| | | | | (_| |
	 \____/_|  |_| .__/ \__\___/ \__, |_|  \__,_|_| |_|\__,_|
	             | |              __/ |                      
	             |_|             |___/                       
	______                            _   _                  
	| ___ \                          | | (_)                 
	| |_/ /___  _ __ ___   _/_/ _ __ | |_ _  ___ __ _        
	|    // _ \| '_ ` _ \ / _` | '_ \| __| |/ __/ _` |       
	| |\ \ (_) | | | | | | (_| | | | | |_| | (_| (_| |       
	\_| \_\___/|_| |_| |_|\__,_|_| |_|\__|_|\___\__,_|                                                          
		""")

def encriptar(palabraClave,texto):
	"""
	Función para encriptar un texto dada una palabra clave
	Recíbe los parámetros: palabraClave y texto
	"""
	#Tamaño de la clave
	tamClave=len(palabraClave)
	
	#Quítamos los espacios de la cadena
	texto=texto.replace(" ","")

	#Transformamos la cadena a lista
	texto=list(texto)
	
	#Para guardar el texo encriptado
	textoEncriptado=""
	#Rellenamos la lista con S
	while True:
		if len(texto)%tamClave!=0:
			texto.append('S')
		else:
			break	
	#print(len(texto))
	#print(texto)
	dicc={}
	#Lleno los valores de un diccionario con cadenas vacías
	for i in palabraClave:
		dicc[i]=""		
	#Íteramos por todo el texto, asígnando la letra correspondiente
	#de acuerdo al modulo de cada elemento de la lista palabraClave
	for j in range(len(texto)):
		print(palabraClave[j%len(palabraClave)])
		dicc[palabraClave[j%len(palabraClave)]]= dicc[palabraClave[j%len(palabraClave)]]+texto[j]
	
	#print(dicc)
	
	#print(dicc.keys())

	diccPalabraClave=list(dicc.keys())
	#print(diccPalabraClave)
	#Ordenamos la lista

	diccPalabraClave.sort()

	for i in diccPalabraClave:
		textoEncriptado=textoEncriptado+dicc[i]

	print("El texto encriptado es: ",textoEncriptado)

	palEncr=open("palabrasEncriptadas","a+")
	palEncr.write("\n"+textoEncriptado)

	funciona=palEncr.read()
	print(funciona)
def desencriptar(palabraClave,texto):
	pass
	



def main(opcion):
	"""
	Función principal, muestra el menu y llama a las funciones correspondientes
	Recíbe el parámetro opción
	"""

	if opcion=='1':
		os.system('clear')
		palabraClave=input("\nIngresa tu palabra clave:   ")
		texto="La criptografía es romántica"
		#texto=input("\nIngresa el texto:")
		encriptar(palabraClave,texto)
	
	elif opcion=='2':
		os.system('clear')
		palabraClave=input("\nIngresa tu palabra clave:   ")
		texto="La criptografía es romántica"
		#texto=input("\nIngresa el texto:")
		desencriptar(palabraClave,texto,textoEncriptado)
	elif opcion=='3':
		print("Vuelve pronto!")
		exit()
	else:
		os.system('clear')
		print('**********Opción inválida****************')

if __name__=='__main__':
	while True:
		asciiart()
		opcion=input("\nElige una opción para continuar:\n\t1.-Encriptar\n\t2.-Desencriptar\n\t3.-Salir\n")
		
		main(opcion)