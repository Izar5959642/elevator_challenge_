
import pygame
from my_setting import *
from models.building import Building, ElevatorFactory

# Initialize Pygame
pygame.init()
pygame.display.set_caption('Elevator Challenge')

# === CREATE MULTIPLE BUILDINGS ===
class BuildingFactory:
    def __init__(self, factory):
        self.factory = factory

    def create_building(self, num_elevators, num_floors, current_x_pos, max_building_height):
        return Building(num_elevators, num_floors, current_x_pos, max_building_height, self.factory)


factory = ElevatorFactory()
building_factory = BuildingFactory(factory)

buildings = []
building_surfaces = []  # List to store precomputed surfaces
x_building_list = []  # List to store x positions of buildings
current_x_pos = 0



# Create buildings with different configurations
for config in BUILDING_CONFIGS:
    num_elevators, num_floors = config
    building = building_factory.create_building(num_elevators, num_floors, current_x_pos, MAX_BUILDING_HEIGHT)
    buildings.append(building)
    building_surfaces.append(building.createSurface())  # Precompute the surface
    x_building_list.append(current_x_pos)  # Store the x position of the building
    current_x_pos += building.width

# Set up the screen and background
screen = pygame.display.set_mode((current_x_pos , SCREEN_HEIGHT))
scrollable_surface = pygame.Surface((current_x_pos, MAX_BUILDING_HEIGHT), pygame.SRCALPHA)

scrollable_surface_y_position = max(0,(MAX_BUILDING_HEIGHT - SCREEN_HEIGHT))
scroll_y  = scrollable_surface_y_position

# Main loop
run = True
while run:
    # Clear the screen
    scrollable_surface.fill((255, 255, 255))
    screen.fill((255, 255, 255))

    for building  in (buildings):
        building.updateAll(scroll_y)  
        building.drawAll()
        scrollable_surface.blit(building.surface, (building.current_x_pos, 0))  

    screen.blit(scrollable_surface, (0, -scroll_y) )    
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_click_mouse = pygame.mouse.get_pos()
            for building in buildings:
                local_x = pos_click_mouse[0] - building.current_x_pos
                local_y = pos_click_mouse[1] - scroll_y
                if 0 <= local_x < building.width:
                    building.getMouseClickPos()
                    break
        if event.type == pygame.MOUSEWHEEL:
            scroll_y -= event.y * 20
            scroll_y = max(0, min(scroll_y, MAX_BUILDING_HEIGHT - SCREEN_HEIGHT))
            
    pygame.display.update()

pygame.quit()
