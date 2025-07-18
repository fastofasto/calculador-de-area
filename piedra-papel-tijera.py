opciones = ['piedra', 'papel', 'tijera']
gana = {'tijera': 'piedra',
        'piedra': 'papel',
        'papel': 'tijera'}

turno = 1
print('Turno',turno)
nombre1 = input('Como se llamara el jugador 1?: ')
nombre2 = input('Como se llamara el jugador 2?: ')
while turno < 5:


    jugador1 = input(f'Hola {nombre1}! ¿Que eliges? ¿Piedra, papel o tijera?: ')
    jugador2 = input(f'Hola {nombre2}! ¿Que eliges? ¿Piedra, papel o tijera?: ')

    if jugador1 == jugador2:
        print('Es un empate!')
    elif jugador1 == gana[jugador2]:
        print(f'Ha ganado {nombre1}!')
    else:
        print(f'Ha ganado {nombre2}!')
turno += 1