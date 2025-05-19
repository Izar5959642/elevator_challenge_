# ! needed to keep the order of the line !

# 2. Screen
SCREEN_WIDTH = 1500  
SCROLL_SPEED = 20   
SCREEN_HEIGHT =  800  #min(800, BUILDING_HIGHT) 


# 3. Floor
FLOOR_WIDTH = 250           
FLOOR_HEIGHT = 60            
SPACER_HEIGHT = 7                # Difference for line drawing
START_X_POS_FLOOR = 60      # Starting X position for floors
SEC_FOR_FLOOR = 0.5          # Seconds it takes for an elevator to travel one floor
PIX_PER_SEC = FLOOR_HEIGHT / SEC_FOR_FLOOR  # Pixels per second an elevator travels
IMG_FLOOR = "./assets/images/building.png"   # Image file for floors



# 4.1. Timer floor
X_POS_TIMER =  0   ##START_X_POS_FLOOR + 5   # X position for the timer display on the floor

# 4.2. Button
SIZE_BUTTON = int(FLOOR_HEIGHT / 3)   # Size of the button
SIZE_BUTTON_NUM = SIZE_BUTTON         # Font size for the button number
X_START_POS_BUTTON = START_X_POS_FLOOR + (FLOOR_WIDTH) / 2  # X position for the button
MID_Y_POS = FLOOR_HEIGHT / 2         # Middle Y position for the button


# 5. Elevator
START_X_POS_ELV = START_X_POS_FLOOR + FLOOR_WIDTH + 10  # Starting X position for elevators
ELV_WIDTH = 50                      # Elevator width
ELV_HEIGHT = FLOOR_HEIGHT - 10      # Elevator height
DIFF_ELV = ELV_WIDTH                # Difference in position between elevators
NUM_ELV = 3                # Number of elevators
IMG_ELV = "./assets/images/elv.png" # Image file for elevators
MP3 = "./assets/mp3_file/ding.mp3" # Sound file for elevator arrival
PAUSE = 2                            # Pause duration in seconds

#building

# Define building configurations (NUM_ELV, NUM_FLOORS)
BUILDING_CONFIGS = [(3, 15), (0, 6), (2, 0)]  # Example configurations
_MAX_BUILDING_HEIGHT = max(config[1] * FLOOR_HEIGHT for config in BUILDING_CONFIGS)
MAX_BUILDING_HEIGHT = max(_MAX_BUILDING_HEIGHT, SCREEN_HEIGHT)  # Ensure it's at least the screen height


ZERO_FLOOR = MAX_BUILDING_HEIGHT - FLOOR_HEIGHT + SPACER_HEIGHT   # Y position of the ground floor


# 1. Colors
WHITE = (255, 255, 255)     
BLACK = (0, 0, 0)            
GREEN = (0, 255, 0)  
RED = (255, 0, 0)        

COL_BUTTON_ON = GREEN                 # Color of the button when pressed
COL_BUTTON_OFF = BLACK    