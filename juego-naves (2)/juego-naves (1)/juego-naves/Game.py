import pygame
import random
from Player import Player
from Enemy import Enemy
from Explosion import Explosion
from Bullet import Bullet

WHITE = (255, 255, 255)
WIDTH = 800
HEIGHT = 600

# Clase principal del juego
class Game:
    def __init__(self, screen, player_image, enemy_image, bullet_image, explosion_anim, shoot_sound, background_image):
        self.screen = screen # Pantalla del juego.
        self.background_image = background_image # Imagen de fondo.
        self.clock = pygame.time.Clock() # Reloj para controlar la velocidad del juego.
        self.running = True # Bandera para indicar si el juego está en ejecución.
        self.all_sprites = pygame.sprite.Group() # Grupo de todos los sprites en el juego.
        self.enemies = pygame.sprite.Group() # Grupo de enemigos.
        self.bullets = pygame.sprite.Group()  # Grupo de proyectiles.
        self.player_image = player_image
        self.enemy_image = enemy_image
        self.bullet_image = bullet_image
        self.explosion_anim = explosion_anim
        self.shoot_sound = shoot_sound

    def create_instances(self):
        # Crea instancias de los grupos y el jugador.
        # Grupos de sprites
        self.all_sprites = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()

        # Creación de la nave del jugador
        self.player = Player(self.player_image)
        self.all_sprites.add(self.player) # Añade al jugador al grupo de todos los sprites.

        # Creación de los enemigos
        for i in range(8):
            enemy = Enemy(self.enemy_image)
            self.all_sprites.add(enemy) # Añade el enemigo al grupo de todos los sprites.
            self.enemies.add(enemy) # Añade el enemigo al grupo de enemigos.

    # Muestra la pantalla de inicio del juego.
    def show_start_screen(self):
        self.screen.blit(self.background_image, (0, 0))
        self.draw_text("Juego de Naves", 64, WIDTH // 2, HEIGHT // 4)
        self.draw_text("Presiona cualquier tecla para comenzar", 22, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip() # Actualiza la pantalla.
        self.wait_for_key() # Espera a que el usuario presione una tecla.

    # Muestra la pantalla de fin del juego.
    def show_game_over_screen(self):
        self.screen.blit(self.background_image, (0, 0))
        self.draw_text("GAME OVER", 64, WIDTH // 2, HEIGHT // 4)
        self.draw_text("Presiona cualquier tecla para volver a jugar", 22, WIDTH // 2, HEIGHT // 2)
        pygame.display.flip() # Actualiza la pantalla.
        self.wait_for_key() # Espera a que el usuario presione una tecla.

    # Método para dibujar texto en la pantalla.
    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(None, size) # Fuente y tamaño del texto.
        text_surface = font.render(text, True, WHITE) # Renderiza el texto.
        text_rect = text_surface.get_rect() # Obtiene el rectángulo del texto.
        text_rect.midtop = (x, y) # Establece la posición del texto.
        self.screen.blit(text_surface, text_rect) # Dibuja el texto en la pantalla.

    # Espera a que el usuario presione una tecla para continuar.
    def wait_for_key(self):
        waiting = True # Bandera para controlar la espera.
        while waiting:
            for event in pygame.event.get(): # Recorre los eventos en la cola de eventos.
                if event.type == pygame.QUIT: # Si se cierra la ventana.
                    pygame.quit() # Cierra pygame.
                    exit() # Sale del programa.
                if event.type == pygame.KEYDOWN: # Si se presiona una tecla.
                    waiting = False # Sale del bucle de espera.

    # Método principal para ejecutar el juego.
    def run(self):
        while self.running: # Mientras el juego esté en ejecución.
            self.show_start_screen() # Muestra la pantalla de inicio del juego.
            self.create_instances() # Crea las instancias del juego.

            game_over = False # Bandera para indicar si el juego ha terminado.
            while not game_over: # Mientras el juego no haya terminado.
                self.clock.tick(60) # Limita el bucle principal a 60 fotogramas por segundo.
                
                # Procesamiento de eventos
                for event in pygame.event.get(): # Recorre los eventos en la cola de eventos.
                    if event.type == pygame.QUIT: # Si se cierra la ventana.
                        game_over = True # Termina el juego.
                        self.running = False # Termina la ejecución del juego.
                    elif event.type == pygame.KEYDOWN: # Si se presiona una tecla.
                        if event.key == pygame.K_SPACE: # Si la tecla es la barra espaciadora.
                            bullet = self.player.shoot(self.bullet_image) # El jugador dispara un proyectil.
                            self.all_sprites.add(bullet) # Añade el proyectil al grupo de todos los sprites.
                            self.bullets.add(bullet) # Añade el proyectil al grupo de proyectiles.
                            self.shoot_sound.play() # Reproduce el sonido de disparo.

                # Actualización de sprites
                self.all_sprites.update()
                
                # Colisiones
                hits = pygame.sprite.groupcollide(self.enemies, self.bullets, True, True) # Colisiones entre enemigos y proyectiles.
                for hit in hits: # Para cada colisión.
                    explosion = Explosion(self.explosion_anim, hit.rect.center) # Crea una explosión en el centro del enemigo.
                    self.all_sprites.add(explosion) # Añade la explosión al grupo de todos los sprites.
                    enemy = Enemy(self.enemy_image) # Crea un nuevo enemigo.
                    self.all_sprites.add(enemy) # Añade el enemigo al grupo de todos los sprites.
                    self.enemies.add(enemy) # Añade el enemigo al grupo de enemigos.

                hits = pygame.sprite.spritecollide(self.player, self.enemies, False) # Colisiones entre el jugador y los enemigos.
                if hits: # Si hay colisiones.
                    game_over = True # El juego ha terminado

                # Renderizado
                self.screen.blit(self.background_image, (0, 0))
                self.all_sprites.draw(self.screen) # Dibuja todos los sprites en la pantalla.
                pygame.display.flip() # Actualiza la pantalla.

            self.show_game_over_screen() # Muestra la pantalla de fin del juego.
