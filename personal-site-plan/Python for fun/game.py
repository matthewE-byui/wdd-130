import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Objects")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player properties
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 20

# Obstacle properties
obstacle_size = 50
obstacle_x = random.randint(0, WIDTH - obstacle_size)
obstacle_y = -obstacle_size
obstacle_speed = 60

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Get keys pressed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    
    # Move obstacle
    obstacle_y += obstacle_speed
    if obstacle_y > HEIGHT:
        obstacle_y = -obstacle_size
        obstacle_x = random.randint(0, WIDTH - obstacle_size)
    
    # Collision detection
    if (player_x < obstacle_x + obstacle_size and
        player_x + player_size > obstacle_x and
        player_y < obstacle_y + obstacle_size and
        player_y + player_size > obstacle_y):
        print("Game Over!")
        running = False
    
    # Draw player and obstacle
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_size, obstacle_size))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
