import pygame
from GameObject import GameObject

BLACK = (0, 0, 0)

# Clase para los disparos del jugador
class Bullet(GameObject):
    def __init__(self, bullet_image, x, y):
        super().__init__(pygame.transform.scale(bullet_image, (10, 20)), x, y)
        self.image.set_colorkey(BLACK)
        self.rect.centerx = x # Posición en "x" del proyectil.
        self.rect.bottom = y # Posición en "y" del proyectil.
        self.speed_y = -10

    def update(self):
        self.rect.y += self.speed_y # Actualiza la posición "y" del proyectil.
        if self.rect.bottom < 0: # Si el proyectil sale de la pantalla por arriba.
            self.kill() # Elimina el proyectil.
