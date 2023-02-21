# A WW2 PyGame game made out of boredom by MalekK882, intended for public use on GitHub.
# Importing the necessary libraries
import pygame
import random

# Screen size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initializing pygame
pygame.init()

# Setting up the window
window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("World War II Game")

# Setting up a score counter
score = 0

# Game loop
running = True
while running:
    # Setting the background
    window.fill((255,255,255))

    # Drawing the elements of the game on the screen
    for i in range(5):
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        pygame.draw.circle(window, (0, 0, 0), (x, y), 5)

    # Getting user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Updating the screen and incrementing the score
    pygame.display.update()
    score += 1

# Closing pygame
pygame.quit()    
