
# img_background = pygame.image.load('./images/background.jpeg')


# import pygame
# from my_setting import *
# from models.building import Building, ElevatorFactory

# # Initialize Pygame
# pygame.init()
# pygame.display.set_caption('Elevator Challenge')

# # === CREATE MULTIPLE BUILDINGS ===
# class BuildingFactory:
#     def __init__(self, factory):
#         self.factory = factory

#     def create_building(self, num_elevators, num_floors, current_x_pos):
        
#         return Building(num_elevators, num_floors, current_x_pos, self.factory)

# factory = ElevatorFactory()
# building_factory = BuildingFactory(factory)

# buildings = []
# screen_width_world = START_X_POS_FLOOR
# current_x_pos = 0
# i = 0
# for config in building_configs:
#     num_elevators, num_floors = config
#     print("number bulding =====", i)
#     i += 1
#     building = building_factory.create_building(num_elevators, num_floors, current_x_pos)
#     buildings.append(building)
#     screen_width_world += building.width + START_X_POS_FLOOR
#     current_x_pos += building.width

# # Precompute building positions
# x_building_list = []
# x_building_pos = 0
# for building in buildings:
#     x_building_list.append(x_building_pos)
#     x_building_pos += building.width + START_X_POS_FLOOR
# # for i in range(NUM_BUILDINGS):
# #     building = Building(NUM_ELV, NUM_FLOORS, factory)
# #     buildings.append(building)
# #     screen_width_world += building.width + START_X_POS_FLOOR 


# img_background = pygame.Surface((screen_width_world, SCREEN_HEIGHT))
# img_background.fill((255, 255, 255))  # Fill the surface with white color
# img_background = pygame.transform.scale(img_background, (screen_width_world, SCREEN_HEIGHT))
# screen = pygame.display.set_mode((screen_width_world, SCREEN_HEIGHT))
# # BUILDING_WIDTH = [building.width for building in building] #screen_width_world // NUM_BUILDINGS




# run = True
# while run:
#     screen.blit(img_background, (0, 0))

#     # Update and draw each building dynamically
#     x_building_pos = 0
#     for building in buildings:
#         # Update the state of the building
#         building.updateAll()

#         # Create a surface for the building
#         building_surface = pygame.Surface((building.width + START_X_POS_FLOOR, SCREEN_HEIGHT), pygame.SRCALPHA)

#         # Draw the updated building state onto its surface
#         building.drawAll(building_surface)

#         # Draw the building surface onto the main screen
#         screen.blit(building_surface, (x_building_pos, 0))
#         x_building_pos += building.width + START_X_POS_FLOOR

#     # Handle floor button presses
#     # for building in buildings:
#     #     for floor in building.floors:
#     #         if floor.button.button_press:
#     #             building.getNewReq(floor.num_floor)

#     # for i, building in enumerate(buildings):
#     #     x_building_list.append(x_building_pos)
#     #     # Create a surface for each building
#     #     building_surface = pygame.Surface((building.width + START_X_POS_FLOOR , SCREEN_HEIGHT), pygame.SRCALPHA)
#     #     building.updateAll()
#     #     building.drawAll(building_surface)

#     #     # Draw each building surface side by side
#     #     screen.blit(building_surface, (x_building_pos , 0))
#     #     x_building_pos += building.width + START_X_POS_FLOOR 
    
#     # Handle floor button presses
#     for building in buildings:
#         for floor in building.floors:
#                 if floor.button.button_press:
#                     building.getNewReq(floor.num_floor)


    

#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#         # if event.type == pygame.MOUSEBUTTONDOWN:
#         #     pos_click_mouse = pygame.mouse.get_pos()
#         #     for i, x_pos in enumerate(x_building_list):
#         #         if x_pos <= pos_click_mouse[0] < x_pos + buildings[i].width:
#         #             local_x = pos_click_mouse[0] - x_pos 
#         #             buildings[i].getMouseClickPos(local_x, pos_click_mouse[1])
#         #             break




#         # pos_click_mouse = pygame.mouse.get_pos()
#         # if event.type == pygame.MOUSEBUTTONDOWN:
#         #     # Detect which building was clicked
#         #     clicked_building_index = pos_click_mouse[0] // BUILDING_WIDTH
            
#         #     if 0 <= clicked_building_index < len(buildings):
#         #         # Translate mouse x to local building x
#         #         local_x = pos_click_mouse[0] - x_building_list[clicked_building_index]     
#         #         buildings[clicked_building_index].getMouseClickPos(local_x, pos_click_mouse[1])


        
#     pygame.display.update()

# pygame.quit()

###-----22222222222-------- WITHOUT THE SCROLLING WORK 
# import pygame
# from my_setting import *
# from models.building import Building, ElevatorFactory

# # Initialize Pygame
# pygame.init()
# pygame.display.set_caption('Elevator Challenge')

# # === CREATE MULTIPLE BUILDINGS ===
# class BuildingFactory:
#     def __init__(self, factory):
#         self.factory = factory

#     def create_building(self, num_elevators, num_floors, current_x_pos):
#         return Building(num_elevators, num_floors, current_x_pos, self.factory)

# # Define building configurations (NUM_ELV, NUM_FLOORS)
# building_configs = [(3, 5), (4, 6), (2, 4)]  # Example configurations

# factory = ElevatorFactory()
# building_factory = BuildingFactory(factory)

# buildings = []
# screen_width_world = START_X_POS_FLOOR
# current_x_pos = 0
# i = 0
# # Create buildings with different configurations
# for config in building_configs:
#     num_elevators, num_floors = config
#     building = building_factory.create_building(num_elevators, num_floors, current_x_pos)
#     buildings.append(building)
#     screen_width_world += building.width + START_X_POS_FLOOR
#     current_x_pos += building.width

# # Set up the screen and background
# img_background = pygame.Surface((screen_width_world, SCREEN_HEIGHT))
# img_background.fill((255, 255, 255))  # Fill the surface with white color
# img_background = pygame.transform.scale(img_background, (screen_width_world, SCREEN_HEIGHT))
# screen = pygame.display.set_mode((screen_width_world, SCREEN_HEIGHT))

# # Main loop
# run = True
# while run:
#     screen.blit(img_background, (0, 0))

#     # Update and draw each building dynamically
#     for building in buildings:
#         building.updateAll()
#         building_surface = pygame.Surface((building.width + START_X_POS_FLOOR, SCREEN_HEIGHT), pygame.SRCALPHA)
#         building.drawAll(building_surface)
#         screen.blit(building_surface, (building.current_x_pos, 0))  # Use current_x_pos

#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             pos_click_mouse = pygame.mouse.get_pos()
#             for building in buildings:
#                 local_x = pos_click_mouse[0] - building.current_x_pos
#                 local_y = pos_click_mouse[1]
#                 if 0 <= local_x < building.width:
#                     building.getMouseClickPos()
#                     break

#     pygame.display.update()

# pygame.quit()


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
building_configs = [(3, 25), (4, 6), (2, 4)]  # Example configurations

factory = ElevatorFactory()
building_factory = BuildingFactory(factory)

buildings = []
screen_width_world = START_X_POS_FLOOR
current_x_pos = 0

# Create buildings with different configurations
for config in building_configs:
    num_elevators, num_floors = config
    building = building_factory.create_building(num_elevators, num_floors, current_x_pos)
    buildings.append(building)
    screen_width_world += building.width + START_X_POS_FLOOR
    current_x_pos += building.width

# Set up the screen and background
img_background = pygame.Surface((screen_width_world, SCREEN_HEIGHT))
img_background.fill((255, 255, 255))  # Fill the surface with white color
img_background = pygame.transform.scale(img_background, (screen_width_world, SCREEN_HEIGHT))
screen = pygame.display.set_mode((screen_width_world, SCREEN_HEIGHT))

# Camera offset
camera_x = 0
camera_y = 0
scroll_speed = 10  # Speed of scrolling

# Main loop
run = True
while run:
    screen.blit(img_background, (0, 0))

    # Update and draw each building dynamically
    for building in buildings:
        building.updateAll()
        building_surface = pygame.Surface((building.width + START_X_POS_FLOOR, SCREEN_HEIGHT), pygame.SRCALPHA)
        building.drawAll()
        screen.blit(building_surface, (building.current_x_pos, 0))  # Use current_x_pos

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos_click_mouse = pygame.mouse.get_pos()
            for building in buildings:
                local_x = pos_click_mouse[0] - building.current_x_pos
                local_y = pos_click_mouse[1]
                if 0 <= local_x < building.width:
                    building.getMouseClickPos()
                    break

    pygame.display.update()

pygame.quit()