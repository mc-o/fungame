import pygame
import random

# Constants
WIDTH, HEIGHT = 800, 600
PARTICLE_RADIUS = 5
BG_COLOR = (0, 0, 0)
PARTICLE_COLOR = (0, 0, 255)
TANK_COLOR = (128, 128, 128)
GRAVITY = 0.1
NUM_PARTICLES = 5

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0

    def move(self):
        self.vy += GRAVITY  # Simulate gravity
        self.x += self.vx
        self.y += self.vy

        # Interaction with edges - Bounce off the edges
        if self.x < tank.left or self.x > tank.right:
            self.vx *= -1
        if self.y < tank.top or self.y > tank.bottom:
            self.vy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(self.x), int(self.y)), PARTICLE_RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# List to store particles
particles = []

# Create the tank as a simple rectangle
tank = pygame.Rect(100, 100, 600, 400)

# Create a few particles within the tank
for _ in range(NUM_PARTICLES):
    x_position = random.randint(tank.left, tank.right)
    y_position = random.randint(tank.top, tank.bottom)
    particle = Particle(x_position, y_position)
    particle.vx = random.uniform(-1, 1)
    particle.vy = random.uniform(-1, 1)
    particles.append(particle)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG_COLOR)

    # Draw the tank
    pygame.draw.rect(screen, TANK_COLOR, tank)

    # Move and draw particles
    for particle in particles:
        particle.move()
        particle.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
