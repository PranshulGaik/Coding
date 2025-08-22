import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Game")

# Colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Clock for FPS
clock = pygame.time.Clock()
FPS = 60

# Pacman properties
pacman_size = 30
pacman_x = WIDTH // 2
pacman_y = HEIGHT // 2
pacman_speed = 5

# Ghost properties
ghost_size = 30
ghosts = []
for _ in range(4):
    ghosts.append([random.randint(0, WIDTH - ghost_size), random.randint(0, HEIGHT - ghost_size),
                   random.choice([-3, 3]), random.choice([-3, 3])])

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed

    # Keep Pacman inside the screen
    pacman_x = max(0, min(WIDTH - pacman_size, pacman_x))
    pacman_y = max(0, min(HEIGHT - pacman_size, pacman_y))

    # Move ghosts
    for ghost in ghosts:
        ghost[0] += ghost[2]
        ghost[1] += ghost[3]
        if ghost[0] <= 0 or ghost[0] >= WIDTH - ghost_size:
            ghost[2] = -ghost[2]
        if ghost[1] <= 0 or ghost[1] >= HEIGHT - ghost_size:
            ghost[3] = -ghost[3]

    # Check collisions
    pacman_rect = pygame.Rect(pacman_x, pacman_y, pacman_size, pacman_size)
    for ghost in ghosts:
        ghost_rect = pygame.Rect(ghost[0], ghost[1], ghost_size, ghost_size)
        if pacman_rect.colliderect(ghost_rect):
            print("Game Over!")
            pygame.quit()
            sys.exit()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.circle(screen, YELLOW, (pacman_x + pacman_size // 2, pacman_y + pacman_size // 2), pacman_size // 2)
    for ghost in ghosts:
        pygame.draw.rect(screen, RED, (ghost[0], ghost[1], ghost_size, ghost_size))

    pygame.display.flip()
    clock.tick(FPS)
