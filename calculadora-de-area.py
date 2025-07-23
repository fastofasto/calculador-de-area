from math import pi
#######################
'''
Problematica:
"El ususario quiere saber cual es el area de un circulo teniendo el radio
'''
#######################
'''
Algoritmo:
1. Solicitar al usuario que ingrese el radio del circulo.
2. Calcular el area del circulo utilizando la formula del area
3. Mostrar al usuario el area calculada.'''
#######################



radio = input('Ingrese el radio en cm del circulo del cual desea calulcar su area : ')

calculo_area = (float(radio) ** 2) * pi

print('El area de tu circulo es de',calculo_area,'centimetros')