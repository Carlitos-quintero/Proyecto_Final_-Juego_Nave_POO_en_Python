import pygame
import random
from GameObject import GameObject

BLACK = (0, 0, 0)
WIDTH = 800
HEIGHT = 600

# Clase para los enemigos
class Enemy(GameObject):
    def __init__(self, enemy_image):
        super().__init__(pygame.transform.scale(enemy_image, (50, 50)), random.randrange(WIDTH - 30), random.randrange(-100, -40))
        self.image.set_colorkey(BLACK)
        self.speed_y = random.randrange(1, 8) # Velocidad vertical aleatoria del enemigo.

    def update(self):
        self.rect.y += self.speed_y # Actualiza la posición "y" del enemigo.
        if self.rect.top > HEIGHT + 10: # Si el enemigo sale de la pantalla por abajo.
            self.rect.x = random.randrange(WIDTH - self.rect.width) # Lo vuelve a posicionar arriba.
            self.rect.y = random.randrange(-100, -40) # Aleatoriamente en la parte superior de la pantalla.
            self.speed_y = random.randrange(1, 8) # Asigna una nueva velocidad vertical aleatoria.
