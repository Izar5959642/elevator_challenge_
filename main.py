import pygame
from settings import BUILDING_CONFIGS, MAX_BUILDING_HEIGHT 
from models.neighborhood import Neighborhood

if __name__ == "__main__":
    """Main entry point for the elevator simulation."""
    pygame.init()
    neighborhood = Neighborhood(BUILDING_CONFIGS, MAX_BUILDING_HEIGHT)
    neighborhood.go_live()
    pygame.quit()