import pygame
import random

#constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
NUM_PREY = 30
NUM_PREDATORS = 5

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
FPS = 10

#base agent class for initialization and movement
class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #randomly moves the agent by selecting a random from -1 to 1 for both the x and y coords
    def move_random(self):
        self.x += random.choice([-1, 0, 1])
        self.y += random.choice([-1, 0, 1])
        self.x = max(0, min(WIDTH // GRID_SIZE - 1, self.x))
        self.y = max(0, min(HEIGHT // GRID_SIZE - 1, self.y))

#empty template for Prey
class Prey(Agent):
    pass

#predator agent with simple function for removing prey
class Predator(Agent):
    def hunt(self, prey_list):
        for prey in prey_list:
            if self.x == prey.x and self.y == prey.y:
                prey_list.remove(prey)
                break

#initializes the sim
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#creates predator and prey agents, stored as arrays
preys = [Prey(random.randint(0, WIDTH // GRID_SIZE - 1),
              random.randint(0, HEIGHT // GRID_SIZE - 1)) for _ in range(NUM_PREY)]
predators = [Predator(random.randint(0, WIDTH // GRID_SIZE - 1),
                      random.randint(0, HEIGHT // GRID_SIZE - 1)) for _ in range(NUM_PREDATORS)]

#main loop
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #move and draw prey
    for prey in preys:
        prey.move_random()
        pygame.draw.rect(screen, GREEN, (prey.x * GRID_SIZE, prey.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    #move and draw predators
    for predator in predators:
        predator.move_random()
        predator.hunt(preys)
        pygame.draw.rect(screen, RED, (predator.x * GRID_SIZE, predator.y * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
