import pygame
from GameObject import GameObject
from Bullet import Bullet

BLACK = (0, 0, 0)
WIDTH = 800
HEIGHT = 600

# Clase para la nave del jugador
class Player(GameObject): #lo que esta dentro del parentesis indica que hay herencia, en este caso la clase Player hereda de GameObject
    def __init__(self, player_image):
        super().__init__(pygame.transform.scale(player_image, (80, 80)), WIDTH // 2, HEIGHT - 60)
        self.image.set_colorkey(BLACK)
        self.speed_x = 0 # Velocidad horizontal inicial del jugador.

    def update(self):
        self.speed_x = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]: # Si se presiona la tecla 'a'.
            self.speed_x = -5 # Se mueve hacia la izquierda.
        if keystate[pygame.K_d]: # Si se presiona la tecla 'd'.
            self.speed_x = 5 # Se mueve hacia la derecha.
        self.rect.x += self.speed_x # Actualiza la posición "x" del jugador.
        if self.rect.right > WIDTH: # Si el jugador llega al borde derecho de la pantalla.
            self.rect.right = WIDTH # Limita su posición a la pantalla.
        if self.rect.left < 0: # Si el jugador llega al borde izquierdo de la pantalla.
            self.rect.left = 0 # Limita su posición a la pantalla.

    # Método para que el jugador dispare un proyectil.
    def shoot(self, bullet_image):
        bullet = Bullet(bullet_image, self.rect.centerx, self.rect.top)  # Crea un proyectil en la posición del jugador.
        return bullet
