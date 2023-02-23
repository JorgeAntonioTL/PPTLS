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


counter = [["Papel", "Spock"],
            ["Tijeras", "Lagarto"],
            ["Piedra", "Spock"],
            ["Piedra", "Tijeras"],
            ["Papel", "Lagarto"]]

import pygame
import random
import sys


blanco = (255, 255, 255) 
negro = (0, 0, 0) 
rojo = (255, 0, 0) 
fps = 30

class pantalla():
    pass

