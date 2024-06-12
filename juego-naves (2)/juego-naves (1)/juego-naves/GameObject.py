import pygame
from abc import ABC, abstractmethod

BLACK = (0, 0, 0)

# Clase base abstracta para objetos del juego
class GameObject(pygame.sprite.Sprite, ABC):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image # Asigna la imagen del objeto
        self.rect = self.image.get_rect() # Obtiene el rectángulo delimitador de la imagen
        self.rect.x = x # Posición en "x" del objeto.
        self.rect.y = y # Posición en "y" del objeto.

    #El método update es abstracto, lo que significa que cualquier clase hija tiene la obligacion de implementarlo
    #El polimorfismo se manifiesta cuando diferentes clases hijas implementan el método update de manera distinta
    @abstractmethod
    def update(self): 
        pass
