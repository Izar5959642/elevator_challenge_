####_+_+_+_+_+_+++_+_+_+__++__+_+_+

# ---------------
# import pygame
# from my_setting import *
# from models.building import *

# # Initialize Pygame
# pygame.init()
# pygame.display.set_caption('Elevator Challenge')

# # === CREATE MULTIPLE BUILDINGS ===
# NUM_BUILDINGS = 6
# buildings = []

# # Calculate building height
# BUILDING_HEIGHT = (NUM_FLOORS + 1) * FLOOR_HEIGHT

# # Initial scroll offsets
# scroll_offset_x = 0
# scroll_offset_y = BUILDING_HEIGHT - SCREEN_HEIGHT  # Start from the bottom
# SCROLL_SPEED = 20

# # Calculate world width based on number of buildings
# screen_width_world = START_X_POS_FLOOR
# for i in range(NUM_BUILDINGS):
#     building = Building(NUM_ELV, NUM_FLOORS)
#     buildings.append(building)
#     screen_width_world += building.width + START_X_POS_FLOOR 

# # Background
# img_background = pygame.Surface((screen_width_world, BUILDING_HEIGHT))
# img_background.fill((255, 255, 255))  # White background
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# BUILDING_WIDTH = screen_width_world // NUM_BUILDINGS

# # Run the game loop
# run = True
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#         # Scroll with mouse wheel
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 4:  # Scroll up
#                 scroll_offset_y = max(0, scroll_offset_y - SCROLL_SPEED)
#             if event.button == 5:  # Scroll down
#                 scroll_offset_y = min(BUILDING_HEIGHT - SCREEN_HEIGHT, scroll_offset_y + SCROLL_SPEED)

#         # Scroll with arrow keys
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 scroll_offset_y = max(0, scroll_offset_y - SCROLL_SPEED)
#             elif event.key == pygame.K_DOWN:
#                 scroll_offset_y = min(BUILDING_HEIGHT - SCREEN_HEIGHT, scroll_offset_y + SCROLL_SPEED)
#             elif event.key == pygame.K_LEFT:
#                 scroll_offset_x = max(0, scroll_offset_x - SCROLL_SPEED)
#             elif event.key == pygame.K_RIGHT:
#                 scroll_offset_x = min(screen_width_world - SCREEN_WIDTH, scroll_offset_x + SCROLL_SPEED)

#     # Blit the background with the correct offset
#     screen.fill((0, 0, 0))  # Clear screen with black
#     screen.blit(img_background, (-scroll_offset_x, -scroll_offset_y))

#     # Draw buildings with scrolling
#     x_building_pos = 0
#     for building in buildings:
#         building_y_position = SCREEN_HEIGHT - BUILDING_HEIGHT - scroll_offset_y
#         building_surface = pygame.Surface((building.width + START_X_POS_FLOOR, BUILDING_HEIGHT), pygame.SRCALPHA)
#         building.updateAll()
#         building.drawAll(building_surface)

#         # Corrected Y position to keep the zero floor at the bottom
#         screen.blit(building_surface, (x_building_pos - scroll_offset_x, building_y_position))
#         x_building_pos += building.width + START_X_POS_FLOOR

#     pygame.display.flip()

# pygame.quit()



# import pygame
# import sys

# import pygame
# from my_setting import *
# from models.building import *

# # הגדרות בסיסיות
# SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# BUILDING_WIDTH, FLOOR_HEIGHT = 100, 50
# NUM_FLOORS = 100
# NUM_BUILDINGS = 3
# buildings = []
# # הגדרות עולם
# WORLD_HEIGHT = NUM_FLOORS * FLOOR_HEIGHT  # גובה העולם
# SCROLL_SPEED = 20  # מהירות גלילה

# # אתחול Pygame
# pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("עולם ומצלמה - מבנה")

# # המצלמה תתחיל בפינה השמאלית התחתונה
# camera_x, camera_y = 0, WORLD_HEIGHT - SCREEN_HEIGHT

# dragging = False
# mouse_start_pos = (0, 0)

# # יצירת מבנה פשוט
# def draw_building(surface, x, y):
#     for floor in range(NUM_FLOORS):
#         # חישוב מיקום הקומה מהתחתית למעלה
#         floor_y = y - (floor + 1) * FLOOR_HEIGHT
#         pygame.draw.rect(surface, (100, 100, 255), (x, floor_y, BUILDING_WIDTH, FLOOR_HEIGHT), 2)

# # לולאת המשחק
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_UP]:
#             camera_y = max(0, camera_y - SCROLL_SPEED)
#         if keys[pygame.K_DOWN]:
#             camera_y = min(WORLD_HEIGHT - SCREEN_HEIGHT, camera_y + SCROLL_SPEED)
#         if keys[pygame.K_LEFT]:
#             camera_x = max(0, camera_x - SCROLL_SPEED)
#         if keys[pygame.K_RIGHT]:
#             camera_x = min(2000 - SCREEN_WIDTH, camera_x + SCROLL_SPEED)

#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 4:
#                 camera_y = max(0, camera_y- SCROLL_SPEED)
#             elif event.button == 5:
#                 camera_y = min (WORLD_HEIGHT - SCREEN_HEIGHT, camera_y + SCROLL_SPEED)
#             elif event.button == 2:
#                 dragging = True
#                 mouse_start_pos = event.pos

#         if event.type == pygame.MOUSEBUTTONUP:
#             if event.button == 2:
#                 dragging = False

#         if event.type == pygame.MOUSEMOTION and dragging:
#             dx, dy = event.pos[0] - mouse_start_pos[0], event.pos[1] - mouse_start_pos[1]
#             camera_x = max(0, min(camera_x - dx, 200 - SCREEN_HEIGHT))
#             camera_y = max(0, min(camera_y - dy, WORLD_HEIGHT - SCREEN_HEIGHT))
#             mouse_start_pos = event.pos




#     # ניקוי המסך
#     screen.fill((30, 30, 30))

#     # יצירת עולם
#     world_surface = pygame.Surface((2000, WORLD_HEIGHT))
#     world_surface.fill((50, 50, 50))

#     # ציור מבנים בעולם
#     for i in range(5):
#         draw_building(world_surface, 200 * i, WORLD_HEIGHT)

#     # הצגת החלק הרלוונטי של העולם על המסך
#     screen.blit(world_surface, (0, 0), (camera_x, camera_y, SCREEN_WIDTH, SCREEN_HEIGHT))

#     pygame.display.flip()



# import pygame
# from my_setting import *
# from models.building import *


# pygame.init()
# pygame.display.set_caption("Elevator Challenge")

# NUM_BUILDINGS = 3
# SCROLL_SPEED = 20
# buildings = []

# scroll_offset_x = 0
# scroll_offset_y = 0

# screen_width_world = START_X_POS_FLOOR
# for i in range(NUM_BUILDINGS):
#     building = Building(NUM_ELV, NUM_FLOORS)
#     buildings.append(building)
#     screen_width_world += building.width + START_X_POS_FLOOR 

# # img_background = pygame.image.load('./images/background.jpeg')

# img_background = pygame.Surface((screen_width_world, SCREEN_HEIGHT))
# img_background.fill((255, 255, 255))  # Fill the surface with white color
# img_background = pygame.transform.scale(img_background, (screen_width_world, SCREEN_HEIGHT))
# screen = pygame.display.set_mode((screen_width_world, SCREEN_HEIGHT))
# BUILDING_WIDTH = screen_width_world // NUM_BUILDINGS




# run = True
# while run:
#     # 1. Event Handling and Input Management
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False

#         pos_click_mouse = pygame.mouse.get_pos()
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             # Detect which building was clicked
#             clicked_building_index = (pos_click_mouse[0] + scroll_offset_x) // BUILDING_WIDTH

#             if 0 <= clicked_building_index < len(buildings):
#                 # Translate mouse x to local building x
#                 local_x = (pos_click_mouse[0] + scroll_offset_x) - x_building_list[clicked_building_index]
#                 buildings[clicked_building_index].getMouseClickPos(local_x, pos_click_mouse[1])

#     # 2. Handle Scrolling (Keyboard Input)
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         scroll_offset_x = max(0, scroll_offset_x - SCROLL_SPEED)
#     if keys[pygame.K_RIGHT]:
#         scroll_offset_x = min(screen_width_world - SCREEN_WIDTH, scroll_offset_x + SCROLL_SPEED)

#     # 3. Clear Screen and Draw Background
#     screen.blit(img_background, (0, 0))

#     # 4. Render Buildings (with scrolling offset)
#     x_building_pos = 0
#     x_building_list = []

#     for i, building in enumerate(buildings):
#         # Store the x position of each building for click detection
#         x_building_list.append(x_building_pos)

#         # Create a surface for each building
#         building_surface = pygame.Surface((building.width + START_X_POS_FLOOR, SCREEN_HEIGHT), pygame.SRCALPHA)
#         building.updateAll()
#         building.drawAll(building_surface)

#         # Position building at the bottom left of the screen
#         building_y = SCREEN_HEIGHT - building.height
#         screen.blit(building_surface, (x_building_pos - scroll_offset_x, building_y))

#         # Move to the next building position
#         x_building_pos += building.width + START_X_POS_FLOOR

#     # 5. Update the Display (Final Step)
#     pygame.display.update()


# pygame.quit()







# import pygame
# import sys
# from my_setting import *
# from models.building import *

# NUM_BUILDING = 4

# SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
# BUILDING_WIDTH, FLOOR_HEIGHT = 100, 60
# NUM_FLOORS = 20

# WORLD_HEIGHT = max(SCREEN_HEIGHT, NUM_FLOORS * (FLOOR_HEIGHT + 7)) # גובה העולם
# SCROLL_SPEED = 20  # מהירות גלילה
 
# pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# pygame.display.set_caption("Elevator Challenge")

# camera_x, camera_y = 0, WORLD_HEIGHT - SCREEN_HEIGHT

# # משתנים לתפיסת גרירת עכבר
# dragging = False
# mouse_start_pos = (0, 0)

# # יצירת מבנה פשוט
# def draw_building(surface, x, y):
#     for floor in range(NUM_FLOORS):
#         # חישוב מיקום הקומה מהתחתית למעלה
#         floor_y = y - (floor + 1) * FLOOR_HEIGHT
#         pygame.draw.rect(surface, (100, 100, 255), (x, floor_y, BUILDING_WIDTH, FLOOR_HEIGHT), 2)
# buildings = []


# screen_width_world = START_X_POS_FLOOR
# for i in range(NUM_BUILDING):
#     building = Building(NUM_ELV, NUM_FLOORS)
#     buildings.append(building)
#     screen_width_world += building.width + START_X_POS_FLOOR 

# img_background = pygame.Surface((screen_width_world, SCREEN_HEIGHT))
# img_background = pygame.image.load('./images/background.jpeg').convert()




# # לולאת המשחק
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             pygame.quit() 
#             sys.exit()

#         # קלטי מקשים להזזת המצלמה
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_UP]:
#             camera_y = max(0, camera_y - SCROLL_SPEED)
#         if keys[pygame.K_DOWN]:
#             camera_y = min(WORLD_HEIGHT - SCREEN_HEIGHT, camera_y + SCROLL_SPEED)
#         if keys[pygame.K_LEFT]:
#             camera_x = max(0, camera_x - SCROLL_SPEED)
#         if keys[pygame.K_RIGHT]:
#             camera_x = min(2000 - SCREEN_WIDTH, camera_x + SCROLL_SPEED)

#         # גלילת עכבר
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if event.button == 4: 
#                 camera_y = max(0, camera_y - SCROLL_SPEED)
#             elif event.button == 5: 
#                 camera_y = min(WORLD_HEIGHT - SCREEN_HEIGHT, camera_y + SCROLL_SPEED)
#             elif event.button == 2:  
#                 dragging = True
#                 mouse_start_pos = event.pos

#         if event.type == pygame.MOUSEBUTTONUP:
#             if event.button == 2: 
#                 dragging = False

#         if event.type == pygame.MOUSEMOTION and dragging:
#             dx, dy = event.pos[0] - mouse_start_pos[0], event.pos[1] - mouse_start_pos[1]
#             camera_x = max(0, min(camera_x - dx, 2000 - SCREEN_WIDTH))
#             camera_y = max(0, min(camera_y - dy, WORLD_HEIGHT - SCREEN_HEIGHT))
#             mouse_start_pos = event.pos

#     # ניקוי המסך
#     screen.blit(img_background, (0, 0))

#     # יצירת עולם
#     # world_surface = pygame.Surface((2000, WORLD_HEIGHT))
#     # world_surface.fill((0, 0, 0))

#     # ציור מבנים בעולם
#     # for i in range(5):
#     #     draw_building(world_surface, 200 * i, WORLD_HEIGHT)
   
#     x_building_pos = 0
#     x_building_list = []
#     for i, building in enumerate(buildings):
#         x_building_list.append(x_building_pos)
#         building_surface = pygame.Surface((building.width + START_X_POS_FLOOR ,WORLD_HEIGHT))

#         building.updateAll()
#         building.drawAll(building_surface)


#     # הצגת החלק הרלוונטי של העולם על המסך
#     screen.blit(building_surface, (0, 100))


#     pygame.display.flip()





# # # import pygame
# # # from my_setting import *
# # # from models.building import *

# # # # Initialize Pygame and set up the screen and window title.
# # # pygame.init()
# # # screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
# # # pygame.display.set_caption('Elevator Challenge')

# # # # Load and scale the background image.
# # # img_background = pygame.image.load('./imegs/blackground.jpeg')
# # # img_background = pygame.transform.scale(img_background, (SCREEN_WIDTH,SCREEN_HEIGHT))

# # # # Create an instance of the Building class.
# # # my_building = Building(NUM_ELV,NUM_FLOORS)



# # # run = True
# # # while run:
# # #     # Draw the background image.
# # #     screen.blit(img_background, (0,0))
# # #     # Update and draw all elevators and floors in the building.
# # #     my_building.updateAll()
# # #     my_building.drawAll(screen)

# # #     # Get the current mouse position.
# # #     pos_click_mouse = pygame.mouse.get_pos()
# # #     # Event handling loop.
# # #     for event in pygame.event.get():
# # #         # Handle the quit event to exit the program.
# # #         if event.type == pygame.QUIT:
# # #             run = False
     
# # #         # Handle mouse button down event to register new requests.
# # #         if event.type == pygame.MOUSEBUTTONDOWN:
# # #             my_building.getMouseClickPos(pos_click_mouse[0], pos_click_mouse[1])
# # #     # Update the display.
  
# # #     pygame.display.update()
# # # # Quit Pygame.
# # # pygame.quit()


####_+_+_+_+_+_+++_+_+_+__++__+_+_+
# This is my code 