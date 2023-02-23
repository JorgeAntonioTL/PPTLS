#Declaración de las clases

import pygame
import random
import sys

blanco = (255, 255, 255) 
negro = (0, 0, 0) 
rojo = (255, 0, 0) 
fps = 30

def texto(texto, tam = 20, color = (0, 0, 0)):
    fuente = pygame.font.Font(None, tam)
    return fuente.render(texto, True, color)

def main():
    pygame.init()
    
    #Dimensiones de la pantalla
    ancho = 1000
    alto = 800
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("PPTLS")

    #Actualizar el display
    actualiza_Display = pygame.time.Clock()

    empezar = True

    while empezar:
        actualiza_Display.tick(fps)

        for event in pygame.event.get():
            if event.type is pygame.quit:
                empezar = False
        
    
    pantalla.fill(negro)
    pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit | sys.exit


class Mano(pygame.sprite.Sprite):
    def __init__(self, texto, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(texto + ".png")
        self.rect = self.image.get_rect()
        self.rect.topleft = x, y
        self.copia_imagen = self.image
        self.tipo = texto
        self.x = x
        self.y = y
        self.factor_reduccion = 15

    def obtener_imagen(self): 
        return self.copia_imagen

    def obtener_rect(self):
        return self.rect

    def tipo_mano(self):
        return self.tipo

    def presionar (self, estado):
        if estado:
            dim_imagen = self.rect.size[0] - self.factor_reduccion
            self.image = pygame.transform.scale(self.image, (dim_imagen, dim_imagen))
            self.rect.topleft = self.x + self.factor_reduccion / 2, self.y + self.factor_reduccion / 2
        else:
            self.image = self.copia_imagen 
            self.rect.topleft = self.x, self.y

class Juego():

    def __init__(self):
    
        self.manos = []

        posicion_vertical = 320 
        self.manos.append(Mano ("Piedra", 10, posicion_vertical))
        self.manos.append(Mano ("Spock", 167, posicion_vertical))
        self.manos.append(Mano ("Papel", 324, posicion_vertical))
        self.manos.append(Mano ("Lagarto", 481, posicion_vertical)) 
        self.manos.append(Mano ("Tijeras", 638, posicion_vertical))

        self.todos_los_sprites = pygame.sprite.Group(self.manos)
        
        self.jugador_escoge = ""
        self.comp_escoge = ""
        self.resultado = ""
        self.texto_jugador = texto("Jugador", 20, blanco) 
        self.texto_computadora = texto ("Máquina", 20, blanco)
        self.texto_resultado = texto("Resultado", 20, blanco)
        
        self.vs_imagen = pygame.image.load("vs.png")
        self.mano_seleccionada = None 
        self.jugador_imagen = None
        self.comp_imagen = None
        
        self.jugador_pos = 120
        self.comp_pos = 480
        
        self.puntuacion = [0, 0] 
