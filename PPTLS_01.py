#Combinaciones
#Izquierda le gana a derecha
#Piedra: Tijeras, Lagarto
#Papel: Piedra, Spock
#Tijeras: Papel, Lagarto
#Lagarto: Papel, Spock
#Spock: Tijeras, Piedra


#Izquierda pierde contra derecha
#0) Piedra: Papel, Spock
#1) Papel: Tijera, Lagarto
#2) Tijeras: Piedra, Spock
#3) Lagarto: Piedra, Tijeras
#4) Spock: Papel, Lagarto

#Recordatorio: Agregar Shuffle()
Manos_Jugar = [0, 1, 2, 3, 4]

counter = [[1, 4],[2, 3],[0, 4],[0, 2],[1, 3]]

import pygame
import random
import sys


blanco = (255, 255, 255) 
negro = (0, 0, 0) 
rojo = (0, 255, 255) 
fps = 30

class pantalla():
    pass

