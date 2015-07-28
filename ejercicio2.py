#!/usr/bin/python

cantidad = int(input("ingrese hasta cuantos numeros quiere saber que cumplen las condiciones: "))

for i in range(1 , cantidad):		
	if(i%3 == 2):
		if(i%5 == 3):
			if(i%7 == 2):
				print(i)
