import random

numero_secreto = random.randint(1,101)
adivinado = False
cant_intentos = 0
cant_max_intentos = 5

print('Hora del acertijo, elije un numero del 1 al 100')

while not adivinado:
    if cant_intentos >= cant_max_intentos:
        print('Te has quedado sin intentos')
        break
    numero = int(input ('Introduce el numero secreto: '))

    if numero == numero_secreto:
        print('Enhorabuena, has adivinado! El numero secreto era',numero_secreto)
        adivinado = True
    elif numero > 100 or numero < 1:
        print('El numero ingresado no es valido')
    elif numero < numero_secreto:
        print('El numero es mayor al ingresado')
    else:
        print('El numero es menor al ingresado')
    cant_intentos += 1