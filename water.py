import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 800, 600
PARTICLE_RADIUS = 5
BG_COLOR = (0, 0, 0)
PARTICLE_COLOR = (0, 0, 255)
GRAVITY = 0.1
NUM_PARTICLES = 100
DAMPING = 0.8  # Damping factor to reduce bouncing
PARTICLE_INTERACTION_RADIUS = 20  # Interaction radius for particles

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

        # Interaction with screen boundaries - Apply damping to reduce bouncing
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -DAMPING
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -DAMPING

    def draw(self, screen):
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(self.x), int(self.y)), PARTICLE_RADIUS)

    def distance(self, other_particle):
        # Calculate the distance between two particles
        return math.sqrt((self.x - other_particle.x) ** 2 + (self.y - other_particle.y) ** 2)

    def interact_with(self, other_particle):
        # Apply interaction between two particles
        if self.distance(other_particle) < PARTICLE_INTERACTION_RADIUS:
            self.vx *= DAMPING
            self.vy *= DAMPING

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# List to store particles
particles = []

# Create a few particles within the screen boundaries
for _ in range(NUM_PARTICLES):
    x_position = random.randint(0, WIDTH)
    y_position = random.randint(0, HEIGHT)
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

    # Move and draw particles
    for particle in particles:
        particle.move()
        particle.draw(screen)

        # Check for particle-particle interactions
        for other_particle in particles:
            if particle != other_particle:
                particle.interact_with(other_particle)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
