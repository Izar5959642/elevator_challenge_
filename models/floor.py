import pygame
from my_setting import *
import time
from pygame.locals import *


from models.button import Button

class Floor:
    """
    The Floor class represents a floor in the elevator system.

    Responsibilities:
    - Manage the floor's properties, such as position and timer.
    - Update the floor's state, including its timer and button state.
    - Draw the floor and its components on the screen.
    """

    def __init__(self , num_floor, num_floors, current_x_pos, max_building_height) -> None:
        self.num_floor = num_floor
        self.x_pos = START_X_POS_FLOOR
        self.y_pos = ZERO_FLOOR - (FLOOR_HEIGHT * num_floor) 
        self.timer = 0
        self.timer_str = ''
        self.img  = pygame.image.load(IMG_FLOOR) 
        self.img = pygame.transform.scale(self.img, (FLOOR_WIDTH, FLOOR_HEIGHT - SPACER_HEIGHT))
        self.col_num = BLACK
        self.last_update = time.time()
        self.flag_in_execution= False
        self.font = pygame.font.Font('freesansbold.ttf', SIZE_BUTTON)
        self.current_x_pos = current_x_pos
        self.end_floor = num_floors - 1
        self.button = Button(self.num_floor, self.y_pos, self.current_x_pos)
        self.surface = pygame.Surface((FLOOR_WIDTH, FLOOR_HEIGHT + SPACER_HEIGHT), pygame.SRCALPHA) 

    def byOrder(self, time):
        """
        Set the floor's timer and mark it as active.
        Arguments:
            time (float): The time to set for the floor's timer.

        Returns:
            None
        """
        self.timer = time
        self.col_num = GREEN
        self.flag_in_execution = True
        

    # Update the floor's state, including the timer and button state.
    def update(self,scroll_y):
        """
        Update the floor's timer and button state.
        Arguments:
            None

        Returns:
            None
        """             
        diff = time.time() - self.last_update
        self.last_update = time.time()

        if self.timer > 0:
            self.timer -= diff
        else:
            self.col_num = BLACK
            self.flag_in_execution = False
        self.convertTimeStr()
        self.button.update(self.flag_in_execution, scroll_y)

    # Convert the timer to a string format.
    def convertTimeStr(self):
        """
        Convert the timer to a string format for display.
        Arguments:
            None

        Returns:
            None
        """
        int_timer = int(self.timer)
        decimal_timer = (self.timer - int_timer)
        int_timer = str(int_timer)
        decimal_timer = str(decimal_timer)
        self.timer_str = int_timer + '.' + decimal_timer[2:4]

    def draw(self):
        """
        Draw the floor, its dividing line, and its timer (if active) on its own surface.
        """
        # Clear the surface
        self.surface.fill((0, 0, 0, 0))  # Transparent background

        # Draw the floor image
        self.surface.blit(self.img, (0, SPACER_HEIGHT))

        # Draw black line between the floors; on the last floor, draw a roof
        if self.num_floor < self.end_floor:
            pygame.draw.rect(self.surface, BLACK, (0, 0, FLOOR_WIDTH, SPACER_HEIGHT))
        else:
            pygame.draw.rect(self.surface, RED, (0, 0, FLOOR_WIDTH, SPACER_HEIGHT))

        # If the floor has an active timer, draw the timer
        if self.flag_in_execution:
            timer_print = self.timer_str
            text_timer = self.font.render(timer_print, True, WHITE, BLACK)
            self.surface.blit(text_timer, (X_POS_TIMER, FLOOR_HEIGHT // 2 ))

        # Draw the button
        self.button.draw(self.surface)




  
    # # Draw the floor and its components on the screen.
    # def draw(self, screen):
    #     """
    #     Draw the floor, its dividing line, and its timer (if active) on the screen.
    #     Arguments:
    #         screen (pygame.Surface): The screen on which to draw the floor.

    #     Returns:
    #         None
    #     """
    #     # Print block image.
    #     screen.blit(self.img, (self.x_pos ,self.y_pos) )   
    #     # Draw black line between the floors; on the last floor, draw a roof.
    #     if self.num_floor < self.end_floor:
    #         pygame.draw.rect(screen, (BLACK), (self.x_pos  ,self.y_pos - SPACER_HEIGHT , FLOOR_WIDTH, SPACER_HEIGHT))
    #     else:
    #         pygame.draw.rect(screen, (GREEN), (self.x_pos  ,self.y_pos - SPACER_HEIGHT , FLOOR_WIDTH, SPACER_HEIGHT + 10))
    #     # If the floor has an active timer, draw the timer on the screen.
    #     if self.flag_in_execution:
    #         timer_print = self.timer_str
    #         text_timer = self.font.render(timer_print , True, WHITE, BLACK)
    #         screen.blit(text_timer, (X_POS_TIMER, self.y_pos  + 15))
    #     self.button.draw(screen)

        # Draw the floor and its components on the screen.