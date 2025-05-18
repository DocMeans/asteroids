# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import WHITE, BLACK, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    # screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    frames = pygame.time.Clock()

    # Groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)

    # center the player in the screen
    player = Player((SCREEN_WIDTH / 2), SCREEN_HEIGHT / 2)

    dt = 0
    # game loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, BLACK)

        updatable.update(dt)
        

        # Check for collision with the player object
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            
            for shot in shots:
                if asteroid.collides_with(shot):
                    shot.kill()
                    asteroid.split()

        # Draw the objects to the screen
        for obj in drawable:
            obj.draw(screen)       
        
        
        pygame.display.flip()
        
        dt = frames.tick(60) / 1000


if __name__ == "__main__":
    main()