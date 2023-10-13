import pygame
import random

# Constants
WIDTH, HEIGHT = 800, 600
PARTICLE_RADIUS = 3
NUM_PARTICLES = 100
BG_COLOR = (0, 0, 0)
PARTICLE_COLOR = (0, 0, 255)
FPS = 60

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def move(self):
        # Simple random motion
        self.vx += random.uniform(-0.1, 0.1)
        self.vy += random.uniform(-0.1, 0.1)
        self.x += self.vx
        self.y += self.vy

        # Bounce off the walls
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(self.x), int(self.y)), PARTICLE_RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create particles
particles = [Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(NUM_PARTICLES)]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    for particle in particles:
        particle.move()
        particle.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

