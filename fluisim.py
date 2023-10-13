import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 800, 600
PARTICLE_RADIUS = 5
NUM_PARTICLES = 100
BG_COLOR = (0, 0, 0)
PARTICLE_COLOR = (0, 0, 255)
FPS = 60

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off the walls
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1

    def check_collision(self, other_particle):
        dx = self.x - other_particle.x
        dy = self.y - other_particle.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance < 2 * PARTICLE_RADIUS:
            # Simple collision response: particles change direction
            self.vx *= -1
            self.vy *= -1
            other_particle.vx *= -1
            other_particle.vy *= -1

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

    for i, particle in enumerate(particles):
        particle.move()
        particle.draw(screen)

        # Check for collisions with other particles
        for j in range(i + 1, len(particles)):
            particle.check_collision(particles[j])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
import pygame
import random
import math

# Constants
WIDTH, HEIGHT = 800, 600
PARTICLE_RADIUS = 5
NUM_PARTICLES = 100
BG_COLOR = (0, 0, 0)
PARTICLE_COLOR = (0, 0, 255)
FPS = 60

# Particle class
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off the walls
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1

    def check_collision(self, other_particle):
        dx = self.x - other_particle.x
        dy = self.y - other_particle.y
        distance = math.sqrt(dx ** 2 + dy ** 2)

        if distance < 2 * PARTICLE_RADIUS:
            # Simple collision response: particles change direction
            self.vx *= -1
            self.vy *= -1
            other_particle.vx *= -1
            other_particle.vy *= -1

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

    for i, particle in enumerate(particles):
        particle.move()
        particle.draw(screen)

        # Check for collisions with other particles
        for j in range(i + 1, len(particles)):
            particle.check_collision(particles[j])

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()

