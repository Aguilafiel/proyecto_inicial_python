
import csv
import random
import interfaz 
from funciones import leer_palabra_secreta, pedir_letra , verificar_letra , validar_palabra

if __name__ == "__main__": 
    while True:
        print("\n¡Aquí comienza el juego del ahorcado!\n")
    # Inicializo las variables y listas a utilizar.
        max_cantidad_intentos = 7
        intentos = 0
        letras_usadas = []
        es_ganador = False
    
    
    # Leer la palabra secreta de un archivo csv.
        palabra_secreta = leer_palabra_secreta('palabras.csv')
    # Esto se realiza para que el jugador pueda ver al principio
    # la cantidad de letras de la palabra a adivinar.
        interfaz.dibujar(palabra_secreta, letras_usadas, intentos)
    
        while intentos < max_cantidad_intentos == 7 and not es_ganador:
        # Pedir una nueva letra
            letra = pedir_letra(letras_usadas)
        
        # Verificar si la letra es parte de la palabra secreta        
            if verificar_letra(letra, palabra_secreta) == False:
            # En caso de no estar la letra ingresada en la palabra
            # a adivinar incremento en 1 la variable intentos.
                intentos += 1
        
        # Dibujar la interfaz
            interfaz.dibujar(palabra_secreta, letras_usadas, intentos)

        # Validar si la palabra secreta se ha adivinado
            if validar_palabra(letras_usadas, palabra_secreta) == True:
                es_ganador = True
                break

        if es_ganador:
            print(f'\n¡Usted ha ganado la partida!, la palabra secreta es: {palabra_secreta}!\n')
            otra = input('¿quieres jugar otra vez? si/no\n')
            if otra == 'si':
                True
            else:
                break
        else:
            print('\n¡Ahorcado!')
            print(f'\n¡Usted ha perdido la partida!, la  palabra secreta es: {palabra_secreta}!\n')
            otra = input('¿quieres jugar otra vez? si/no\n')
            if otra == 'si':
                True
            else:
                break