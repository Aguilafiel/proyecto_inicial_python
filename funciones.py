import csv
import random
import interfaz 


def leer_palabra_secreta(archivo):
    archivo = 'palabras.csv'
    with open(archivo) as f:
        lista_archivo = list(f)
    
    lista_palabras_secreteas = []

    for x in lista_archivo:
        lista_palabras_secreteas.append(x)
    
    palabra_secreta = random.choice(lista_palabras_secreteas)
    palabra_secreta = palabra_secreta.strip() 
    return(palabra_secreta)

def pedir_letra(letras_usadas):
    while True:
        nueva_letra = str(input('Ingrese UNA nueva letra que no haya utilizado antes: '))
        
        letra = nueva_letra.lower()
        
        if letra not in letras_usadas and len(letra) == 1:
            break
        else:
            continue
    letras_usadas += letra
    
    return(letra)

def verificar_letra(letra, palabra_secreta):
    if letra in palabra_secreta:
        return(True)
        
    else:
        return(False)

def validar_palabra(letras_usadas, palabra_secreta):
    contador = 0
    for letra in palabra_secreta:
        if letra  in letras_usadas:
            contador  += 1
        else:
            contador = 0
    
    
    if contador == len(palabra_secreta):
        return(True)
    else:
        return(False)
