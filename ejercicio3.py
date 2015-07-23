#!/usr/bin/python
'''
Autor: Erik Alexander Gonzalez Cardona

Descripcion: script que recibe tres numeros y muestra la suma de esos numeros, luego encuentra la lista de todas las tripletas de números naturales que sumen lo mismo que los numeros entrados por el usuario
'''
n = []
r = 0
for i in range(0,3):
	muestra  = "ingrese un numero entero en el casillero  %d :  "%(i+1) 
	numero = int(input( muestra ))
	r +=  numero
	n.append(numero)

print("la suma de los tres numeros es de  : %d  "%(r))
print("se buscaran mas numeros que sumados den el mismo resultado : ")

cache = []
cache.append(n)
for i1 in range(0,r+1):
	for i2 in range(0,r+1):
		for i3 in range(0,r+1):
			verdadero = True
			ordenados = sorted([i1,i2,i3])
			if not cache:
				cache.append(ordenados)
			else:
				if(i1+i2+i3 == r):
					for lista in cache:
						if(ordenados == lista):
							verdadero = False
					if(verdadero):
						cache.append(ordenados)
						print(" los numeros : %d %d %d "%(ordenados[0], ordenados[1], ordenados[2]))
						
				
	
