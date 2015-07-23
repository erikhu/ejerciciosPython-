#!/usr/bin/python
import math

def calcularAnguloPoligono(radio ,  lados ):
	angulo = math.degrees(2*math.pi/lados)

pPoligono  = float(input("ingrese el valor del perimetro del poligono"))
radio  = float(input("ingrese el radio del circulo"))
pCirculo = perimetroCirculo(radio)
if(pPoligono > pCirculo):
	print("el perimetro del poligono no puede\n ser mayor al del circulo")
	stop()



		
