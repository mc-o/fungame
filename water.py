import pygame
import random

# Constants
WIDTH, HEIGHT = 800, 600
PARTICLE_RADIUS = 5
BG_COLOR = (0, 0, 0)
PARTICLE_COLOR = (0, 0, 255)
FLOW_RATE = 5  # Adjust the flow rate to control the number of particles added per frame
FPS = 60

# Particle class
class Particle:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def move(self):
        self.x += self.vx
        self.y += self.vy

        # Bounce off the screen boundaries
        if self.x < 0:
            self.x = 0
            self.vx *= -1
        if self.x > WIDTH:
            self.x = WIDTH
            self.vx *= -1
        if self.y < 0:
            self.y = 0
            self.vy *= -1
        if self.y > HEIGHT:
            self.y = HEIGHT
            self.vy *= -1

    def draw(self, screen):
        pygame.draw.circle(screen, PARTICLE_COLOR, (int(self.x), int(self.y)), PARTICLE_RADIUS)

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# List to store particles
particles = []

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Create new particles at the top-left corner with random velocities
    for _ in range(FLOW_RATE):
        x_position = 0
        y_position = 0
        vx = random.uniform(1, 3)  # Adjust the velocity range
        vy = random.uniform(1, 3)
        particle = Particle(x_position, y_position, vx, vy)
        particles.append(particle)

    screen.fill(BG_COLOR)

    # Move and draw particles
    for particle in particles:
        particle.move()
        particle.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
