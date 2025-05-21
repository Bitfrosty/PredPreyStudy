import pygame
import random

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
NUM_PREY = 30
NUM_PREDATORS = 5

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
FPS = 10

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_random(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        self.x = max(0, min(WIDTH // GRID_SIZE - 1, self.x))
        self.y = max(0, min(HEIGHT // GRID_SIZE - 1, self.y))

class Prey(Agent):
    pass

class Predator(Agent):
    def hunt(self, prey_list):
        for prey in prey_list:
            if self.x == prey.x and self.y == prey.y:
                prey_list.remove(prey)
                break

# Initialize
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Create agents
preys = [Prey(random.randint(0, WIDTH // GRID_SIZE - 1),
              random.randint(0, HEIGHT // GRID_SIZE - 1)) for _ in range(NUM_PREY)]
predators = [Predator(random.randint(0, WIDTH // GRID_SIZE - 1),
                      random.randint(0, HEIGHT // GRID_SIZE - 1)) for _ in range(NUM_PREDATORS)]

# Main loop
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move and draw prey
    for prey in preys:
        prey.move_random()
        pygame.draw.rect(screen, GREEN, (prey.x * GRID_SIZE, prey.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    # Move and draw predators
    for predator in predators:
        predator.move_random()
        predator.hunt(preys)
        pygame.draw.rect(screen, RED, (predator.x * GRID_SIZE, predator.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
