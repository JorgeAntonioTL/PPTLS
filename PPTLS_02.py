#Declaración de las clases

import pygame
import random
import sys

Manos_Jugar = [0, 1, 2, 3, 4]
counter = [[1, 4],[2, 3],[0, 4],[0, 2],[1, 3]]

blanco = (255, 255, 255) 
negro = (0, 0, 0) 
rojo = (0, 255, 255) 
fps = 30

def Shuffle_Manos_Jugar():
    return random.shuffle(Manos_Jugar)


def texto(texto, tam = 20, color = (0, 255, 255)):
    fuente = pygame.font.Font(None, tam)
    return fuente.render(texto, True, color)


class manos(pygame.sprite.Sprite):

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

        posicion_vertical = 400 
        self.manos.append(manos ("Piedra", 60, posicion_vertical))
        self.manos.append(manos ("Spock", 217, posicion_vertical))
        self.manos.append(manos ("Papel", 374, posicion_vertical))
        self.manos.append(manos ("Lagarto", 531, posicion_vertical)) 
        self.manos.append(manos ("Tijeras", 688, posicion_vertical))

        self.todos_los_sprites = pygame.sprite.Group(self.manos)
        
        self.jugador_escoge = ""
        self.comp_escoge = ""
        self.resultado = ""

        self.texto_jugador = texto("Persona", 20, blanco) 
        self.texto_computadora = texto ("Computadora", 20, blanco)
        self.texto_resultado = texto("Resultado", 20, blanco)
        
        self.vs_imagen = pygame.image.load("vs.png")
        self.mano_seleccionada = None 
        self.jugador_imagen = None
        self.comp_imagen = None
        
        self.jugador_pos = 120
        self.comp_pos = 600
        
        self.puntuacion = [0, 0] 
        
    def copiar_imagen(self, mano_seleccionada):
        for mano in self.manos:
            if mano.tipo_mano() == mano_seleccionada: 
                return pygame.transform.scale(mano.obtener_imagen(), (200, 200))
            
    def obtener_manos(self):
        return self.manos

    def seleccionar (self, mano):
        self.mano_seleccionada = mano

    def obtener_mano_seleccionada(self): 
        return self.mano_seleccionada
    
    def dibujar(self, pantalla):
        pantalla.blit(self.texto_jugador, (10, 10))
        pantalla.blit(self.texto_computadora, (700, 10))
        pantalla.blit(self.texto_resultado, (370, 10))

        if self.jugador_imagen:
            pantalla.blit(texto(str(self.puntuacion[0]), 80, blanco), (190, 40)) 
            pantalla.blit(texto(str(self.puntuacion[1]), 80, blanco), (590, 40))
            pantalla.blit(texto(self.resultado, 50, blanco), (320, 50))
            pantalla.blit (texto(self.jugador_escoge, 30, rojo), (10, 30)) 
            pantalla.blit(texto (self.comp_escoge, 30, rojo), (720, 30))
            pantalla.blit(self.vs_imagen, (350,150))
            pantalla.blit(self.jugador_imagen, (self.jugador_pos,100))
            pantalla.blit(self.comp_imagen, (self.comp_pos,100))
        self.todos_los_sprites.draw(pantalla)

    def nombre_a_numero(self, nombre): 
        if nombre == "Piedra": return 0
        elif nombre == "Spock": return 1 
        elif nombre == "Papel": return 2
        elif nombre == "Lagarto": return 3
        elif nombre == "Tijeras": return 4
        else: print ("Introduce un nombre valido")

    def numero_a_nombre(self, numero):
        if  numero == 0: return "Piedra"
        elif numero == 1: return "Spock"
        elif numero == 2: return "Papel"
        elif numero == 3: return "Lagarto" 
        elif numero == 4: return "Tijeras"
        else: print("Numero fuera de rango")

    def jugar(self, jugador):        
        self.jugador_escoge = jugador  
        self.jugador_imagen = self.copiar_imagen (jugador)
        numero_jugador = self.nombre_a_numero(jugador)
        
        numero_comp = Manos_Jugar[random.randint(0, len(Manos_Jugar) - 1)]
        Manos_Jugar.extend(counter[numero_jugador])

        self.comp_escoge = self.numero_a_nombre (numero_comp) 
        self.comp_imagen = self.copiar_imagen(self.comp_escoge)
        res = (numero_jugador - numero_comp) % 5
        
        if res == 0: self.resultado = "Empataron"
        
        elif res < 3:
            self.resultado = "Ganaste"
            self.puntuacion[0] += 1
        
        elif res > 2: 
            self.resultado = "Perdiste"
            self.puntuacion[1] += 1

        #Piedra - Papel, Spock
        #Spock  - Papel, Lagarto
        #Papel  - Tijeras, Lagarto
        #Lagarto - Piedra, Tiejera 
        #Tijeras - Piedra, Spock

        #0 - 2, 1
        #1 - 2, 3
        #2 - 4, 3
        #3 - 0, 4
        #4 - 0, 1

    def actualiza(self):
        if pygame.mouse.get_pressed()[0]:
            mouse = pygame.mouse.get_pos() 
            self.seleccionar (None) 
            for mano in self.obtener_manos():

                if mano.obtener_rect().collidepoint(mouse): 
                    mano.presionar(True) 
                    self.seleccionar(mano) 

                else: mano.presionar (False)

def main():
    pygame.init()

    #Dimensiones de la pantalla
    ancho = 900
    alto = 600
    pantalla = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("PPTLS")

    juego = Juego()

    #Actualizar el display
    actualiza_Display = pygame.time.Clock()

    empezar = True

    while empezar:
        actualiza_Display.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                empezar = False
            
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                empezar = False
            
            elif event.type == pygame.MOUSEBUTTONUP:
                if  juego.obtener_mano_seleccionada():
                     juego.jugar(juego.obtener_mano_seleccionada().tipo_mano())

                for mano in juego.obtener_manos():
                    mano.presionar(False)
        
        juego.actualiza()

        pantalla.fill(negro)
        juego.dibujar(pantalla)

        pygame.display.flip()

if __name__ == "__main__":
    main()
    pygame.quit | sys.exit
   

