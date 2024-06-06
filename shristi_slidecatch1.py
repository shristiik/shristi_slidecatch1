import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Rescue')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Load images
spaceship_img = pygame.image.load('spaceship.png').convert_alpha()
spaceship_img = pygame.transform.scale(spaceship_img, (50, 50))
astronaut_img = pygame.image.load('astronaut.png').convert_alpha()
astronaut_img = pygame.transform.scale(astronaut_img, (50, 50))
background_img = pygame.image.load('spaceship.png').convert_alpha()
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))

# Define classes
class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = spaceship_img
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)
        self.move_speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.move_speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.move_speed

class Astronaut(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = astronaut_img
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.y = 10
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.speed_y = random.randint(3, 8)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > screen_height:
            self.reset()

# Create sprite groups
all_sprites = pygame.sprite.Group()
astronauts = pygame.sprite.Group()

# Create instances of the classes
spaceship = Spaceship()
all_sprites.add(spaceship)

for _ in range(5):  # Create multiple astronauts
    astronaut = Astronaut()
    all_sprites.add(astronaut)
    astronauts.add(astronaut)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Check for collisions
    if pygame.sprite.spritecollide(spaceship, astronauts, True):
        new_astronaut = Astronaut()
        all_sprites.add(new_astronaut)
        astronauts.add(new_astronaut)

    # Draw everything
    screen.blit(background_img, (0, 0))
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
