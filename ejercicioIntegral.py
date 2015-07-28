#!/usr/bin/python
import math
def areaTrapezio(espacio,y1,y2):
	return  (y1+y2)*espacio/2
	
def f(x):
	return math.sqrt(x)

def calcularIntegral(xInicial,xFinal, div):
	total  = 0 
	espacio = (xFinal-xInicial)/div
	contador = 0 
	
	while(contador < div):
		tmp = xInicial
		xInicial+=espacio
		total += areaTrapezio(espacio , f(tmp),f(xInicial))		
		contador = contador+1
	print(total)

x1 = float(input("ingrese el xinicial: "))
x2 = float(input("ingrese el xfinal: "))
d = float(input("ingrese cuantas veces quiere dividir el espacio: "))	
	
calcularIntegral(x1,x2,d)

