import pygame
from Game import Game

# Definición de colores en formato RGB
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Juego de Naves")

# Cargar imágenes
player_image = pygame.image.load("jugador.png").convert()
enemy_image = pygame.image.load("asteroide.png").convert()
bullet_image = pygame.image.load("kylorenlightsaberused3dmodelsset05.jpg").convert()

explosion_anim = []
for i in range(12):
    img = pygame.image.load(f"{i+1}.png").convert()
    explosion_anim.append(img)

# Carga de sonido
shoot_sound = pygame.mixer.Sound("laser-zap-90575.mp3")
background_image = pygame.image.load("deep_space_environment_cd0002.jpg").convert()

# Escalar imagen de fondo para que coincida con el tamaño de la pantalla
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

if __name__ == "__main__":
    # Crea una instancia del juego.
    game = Game(screen, player_image, enemy_image, bullet_image, explosion_anim, shoot_sound, background_image)
    game.run() # Ejecuta el juego.
    pygame.quit() # Cierra pygame.



