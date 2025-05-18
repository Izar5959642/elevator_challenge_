
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

    def create_building(self, num_elevators, num_floors, current_x_pos):
        return Building(num_elevators, num_floors, current_x_pos, self.factory)

# Define building configurations (NUM_ELV, NUM_FLOORS)
building_configs = [(3, 15), (4, 6), (2, 4)]  # Example configurations

factory = ElevatorFactory()
building_factory = BuildingFactory(factory)

buildings = []
building_surfaces = []  # List to store precomputed surfaces
x_building_list = []  # List to store x positions of buildings
#screen_width_world = START_X_POS_FLOOR
current_x_pos = 0
max_building_height = SCREEN_HEIGHT


# Create buildings with different configurations
for config in building_configs:
    num_elevators, num_floors = config
    building = building_factory.create_building(num_elevators, num_floors, current_x_pos)
    buildings.append(building)
    building_surfaces.append(building.createSurface())  # Precompute the surface
    x_building_list.append(current_x_pos)  # Store the x position of the building

    #screen_width_world += building.width + START_X_POS_FLOOR

    current_x_pos += building.width
    max_building_height = max(max_building_height, building.height)

# Set up the screen and background
screen = pygame.display.set_mode((current_x_pos , SCREEN_HEIGHT))

scrollable_surface = pygame.Surface((current_x_pos, max_building_height), pygame.SRCALPHA)
scrollable_surface_y_position = max(0,(max_building_height - SCREEN_HEIGHT))
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
        scrollable_surface.blit(building.surface, (building.current_x_pos, scrollable_surface_y_position))  

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
            scroll_y = max(0, min(scroll_y, max_building_height - SCREEN_HEIGHT))
            # scrollable_surface_y_position = scroll_y
            # print("--",scroll_y,pos_click_mouse[1],local_y, event.y, max_building_height, SCREEN_HEIGHT )
            print(f"-- --scroll_y = {scroll_y},pos_click_mouse[1] = {pos_click_mouse[1]},local_y = {local_y},scrollable_surface_y_position = {scrollable_surface_y_position}, max_building_height = {max_building_height}"  )

    pygame.display.update()

pygame.quit()







    # # Handle events
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         run = False

    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         pos_click_mouse = pygame.mouse.get_pos()
    #         global_x = pos_click_mouse[0] 
    #         global_y = pos_click_mouse[1]

    #         # Determine which building was clicked
    #         for i, building in enumerate(buildings):
    #             if x_building_list[i] <= global_x < x_building_list[i] + building.width:
    #                 local_x = global_x - building.current_x_pos
    #                 local_y = global_y 
    #                 if 0 <= local_x < building.width:
    #                     building.getMouseClickPos()
    #                     print(f"{global_y} = {pos_click_mouse[1]} ")
    #                     break
    # Handle events