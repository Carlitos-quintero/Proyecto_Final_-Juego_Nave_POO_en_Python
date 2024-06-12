import pygame
from GameObject import GameObject

BLACK = (0, 0, 0)

# Clase para las explosiones
class Explosion(GameObject):
    def __init__(self, explosion_anim, center):
        super().__init__(explosion_anim[0], center[0], center[1])
        self.rect.center = center # Centra la explosión en el punto dado.
        self.frame = 0 # Contador de frames para la animación.
        self.last_update = pygame.time.get_ticks() # Tiempo transcurrido desde el último frame.
        self.frame_rate = 50 # Velocidad de la animación.
        self.explosion_anim = explosion_anim

    def update(self):
        now = pygame.time.get_ticks()  # Tiempo actual.
        if now - self.last_update > self.frame_rate: # Si ha pasado suficiente tiempo desde el último frame.
            self.last_update = now # Actualiza el tiempo del último frame.
            self.frame += 1 # Avanza al siguiente frame de la animación.
            if self.frame == len(self.explosion_anim): # Si llega al final de la animación.
                self.kill() # Elimina la explosión.
            else:
                center = self.rect.center # Guarda el centro actual de la explosión.
                self.image = self.explosion_anim[self.frame] # Actualiza la imagen de la explosión.
                self.rect = self.image.get_rect() # Obtiene el nuevo rectángulo de la imagen.
                self.rect.center = center # Restaura el centro de la explosión.
