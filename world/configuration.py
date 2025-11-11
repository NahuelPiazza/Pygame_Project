import constants as const



# Configuration settings for the game world

WORLD_WIDTH = 1200
WORLD_HEIGHT = 800

def create_world(screen):
    # Fill the screen with a light gray color
    screen.fill((const.BLACK))