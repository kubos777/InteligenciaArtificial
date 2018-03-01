#-*- coding:utf-8-*-	
import argparse
import random
"""
TEST
"""
class Automata(object):
	"""
	Clase que representa el automata celular unidimensional
	"""
	regla = {
		"00"	: "0",
		"01"	: "1",
		"10"	: "1",
		"11"	: "1",
		"000"	: "0",
		"001"	: "1",
		"010"	: "1",
		"011"	: "1",
		"100"	: "1",
		"101"	: "1",
		"110"	: "1",
		"111"	: "0"
	}
	cadena = ""
	cadena_siguiente = ""

	def mostrar(self):
		"""
		Muestra el valor actual de la cadena
		"""
		salida = self.cadena.replace("0"," ")
		salida = salida.replace("1","*")
		print(salida)

	def evaluar(self,n=1):
		"""
		Permite evaluar la cadena del automata n veces
		"""
		self.mostrar()
		for j in range(n):
			self.cadena_siguiente = ""
			for i in range(len(self.cadena)):
				if i == 0:
					self.cadena_siguiente += self.regla[self.cadena[:2]]
				elif i == len(self.cadena):
					self.cadena_siguiente += self.regla[self.cadena[-2]]
				else:
					self.cadena_siguiente += self.regla[self.cadena[i-1:i+2]]
			self.cadena = self.cadena_siguiente
			self.mostrar()

	


if __name__=='__main__':
	
	parser = argparse.ArgumentParser()
	
	parser.add_argument('-a', action='store', dest='accion', choices=['aleatorio','sierpinski'])
	parser.add_argument('-t', action='store', dest='tamano', type=int)
	parser.add_argument('-v', action='store', dest='veces', type=int)
	argumentos = parser.parse_args()

	atm = Automata()

	if not argumentos.accion or not argumentos.tamano or not argumentos.veces:
		parser.print_help()	

	if argumentos.accion == 'aleatorio':
		cadena = ''.join(random.choice('01') for _ in range(argumentos.tamano))
		
	elif argumentos.accion == 'sierpinski':
		subcadena1 = ['0' for i in range(int(argumentos.tamano/2))]
		subcadena2 = ['1' for i in range((argumentos.tamano%2) + 1)]
		resultado = subcadena1 + subcadena2 + subcadena1
		cadena = ''.join(resultado)

	atm.cadena = cadena
	atm.evaluar(argumentos.veces)
