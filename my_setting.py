# ! needed to keep the order of the line !
# import pygame
# from models.building import Building
# import sys


building_configs = [(3, 5), (4, 6), (2, 4)] 

WINDOW_SIZE = 1200, 1000

# 2. Screen
SCREEN_WIDTH = 1500  
SCROLL_SPEED = 20        

# 3. Floor
NUM_FLOORS = 10           # Number of floors
FLOOR_WIDTH = 250           
FLOOR_HEIGHT = 60            
SPACER_HEIGHT = 7                # Difference for line drawing
START_X_POS_FLOOR = 60      # Starting X position for floors
NUM_LINE = NUM_FLOORS - 1    # Number of lines between floors
SEC_FOR_FLOOR = 0.5          # Seconds it takes for an elevator to travel one floor
PIX_PER_SEC = FLOOR_HEIGHT / SEC_FOR_FLOOR  # Pixels per second an elevator travels
IMG_FLOOR = "./images/building.png"   # Image file for floors



# 4.1. Timer floor
X_POS_TIMER = START_X_POS_FLOOR + 5   # X position for the timer display on the floor

# 4.2. Button
SIZE_BUTTON = int(FLOOR_HEIGHT / 3)   # Size of the button
SIZE_BUTTON_NUM = SIZE_BUTTON         # Font size for the button number
X_START_POS_BUTTON = START_X_POS_FLOOR + (FLOOR_WIDTH) / 2  # X position for the button
MID_Y_POS = FLOOR_HEIGHT / 3          # Middle Y position for the button
X_END_POS_BUTTON = X_START_POS_BUTTON + SIZE_BUTTON  # End X position for button click range
X_START_POS_BUTTON_CLICK = X_START_POS_BUTTON - SIZE_BUTTON  # Start X position for button click range
            # Color of the button when not pressed


# 5. Elevator
START_X_POS_ELV = START_X_POS_FLOOR + FLOOR_WIDTH + 10  # Starting X position for elevators
ELV_WIDTH = 50                      # Elevator width
ELV_HEIGHT = FLOOR_HEIGHT - 10      # Elevator height
DIFF_ELV = ELV_WIDTH                # Difference in position between elevators
NUM_ELV = 3                # Number of elevators
IMG_ELV = "./images/elv.png" # Image file for elevators
MP3 = "./mp3_file/ding.mp3" # Sound file for elevator arrival
PAUSE = 2                            # Pause duration in seconds

#building
BUILDING_HIGHT = (NUM_FLOORS + 1  ) * (FLOOR_HEIGHT + SPACER_HEIGHT)
SCREEN_HEIGHT =    min(800, BUILDING_HIGHT)        
ZERO_FLOOR = SCREEN_HEIGHT - FLOOR_HEIGHT + SPACER_HEIGHT   # Y position of the ground floor
BUILDING_WIDTH = FLOOR_WIDTH + START_X_POS_FLOOR + (NUM_ELV * ELV_WIDTH)
NUM_BUILDINGS = 4

# 6. Roof
# UP_VERTICE = ZERO_FLOOR - (FLOOR_HEIGHT * NUM_FLOORS)  # Upper vertex of the roof
# LEFT_RUGHT_Y_VERTICE = ZERO_FLOOR - (FLOOR_HEIGHT * (NUM_FLOORS - 1))  # Left and right vertices of the roof

# # Ensure the upper vertex is not less than 0
# if UP_VERTICE < 0:
#     UP_VERTICE = 0

# # Define the vertices of the roof polygon
# roof_vertices = [
#     ((START_X_POS_FLOOR + FLOOR_WIDTH) / 2, UP_VERTICE),
#     (START_X_POS_FLOOR, LEFT_RUGHT_Y_VERTICE),
#     (START_X_POS_FLOOR + FLOOR_WIDTH, LEFT_RUGHT_Y_VERTICE)
# ]


# 1. Colors
WHITE = (255, 255, 255)     
BLACK = (0, 0, 0)            
GREEN = (0, 255, 0)          


COL_BUTTON_ON = GREEN                 # Color of the button when pressed
COL_BUTTON_OFF = BLACK    