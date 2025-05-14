import pygame
from my_setting import *
import time
from pygame.locals import *


class Button:
    """
    The Button class represents a button in the elevator system.

    Responsibilities:
    - Manage the button's state (pressed or not pressed).
    - Check if the button has been pressed based on mouse position.
    - Update the button's appearance and draw it on the screen.
    """

    def __init__(self, num_button, y_pos, current_x_pos) -> None:
        self.x_pos = X_START_POS_BUTTON
        self.y_pos = y_pos + (FLOOR_HEIGHT / 2)
        self.background = WHITE
        self.col_button = COL_BUTTON_OFF
        self.font = pygame.font.Font('freesansbold.ttf', SIZE_BUTTON_NUM)
        self.button_press = False
        self.str_num_floor = str(num_button)
        self.text_button = self.font.render( self.str_num_floor, True, self.col_button, self.background)
        

        self.rect = pygame.Rect(
            current_x_pos  + self.x_pos - SIZE_BUTTON ,  # x-coordinate
            self.y_pos - SIZE_BUTTON,  # y-coordinate
            SIZE_BUTTON * 2,           # width
            SIZE_BUTTON * 2            # height
        )
        # print("in button ", current_x_pos, self.rect)
        # print ("self.x_pos ", self.x_pos)

    def handleEvent(self, event):
        """
        Handle mouse events for the button.
        Arguments:
            event (pygame.event.Event): The mouse event to handle.

        Returns:
            bool: True if the button was pressed, False otherwise.
        """
        
        print ("event.ppos", event.pos)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button
            if self.rect.collidepoint(event.pos):  # Check if the click is within the button's rect
                self.button_press = True
                return True
        return False

    def isPressed(self):
        """
        Check if the button was pressed.
        Returns:
            bool: True if the button is pressed, False otherwise.
        """
        # Use the pygame mouse method to directly check collision
        # print("pygame.mouse.get_pos() ", pygame.mouse.get_pos())
        
        if pygame.mouse.get_pressed()[0]:  # Check if the left mouse button is pressed
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False
    
    # Check if the x, y position of the mouse is in the range of the button.
    def checkPress(self):
        ''''
        Check if the mouse is over the button.
        Arguments:
            x_mouse (int): The x position of the mouse.
            y_mouse (int): The y position of the mouse.

        Returns:
            bool: True if the mouse is over the button, False otherwise.
        '''''
        return self.isPressed()
    

        # if  not x_mouse in range(int(X_START_POS_BUTTON_CLICK), int(X_END_POS_BUTTON)) :
        #     return False
        # if y_mouse in range(int(self.y_pos - SIZE_BUTTON),int( self.y_pos + SIZE_BUTTON)):
        #     return True
        # else:
        #     return False
        

   
    # # Update the button state based on whether it is pressed.
    # def update(self , button_press ):
    #     ''''
    #     Update the button's state and coller button.
    #     Arguments:
    #         button_press (bool): True if the button is pressed, False otherwise.

    #     Returns:
    #         None
    #     '''''
    #     if button_press == True:
    #         self.button_press = True
    #         self.col_button = COL_BUTTON_ON
    #     else:
    #         self.button_press = False
    #         self.col_button = COL_BUTTON_OFF
    #     self.text_button = self.font.render( self.str_num_floor, True, self.col_button, self.background)

    def update(self, button_press):
        """
        Update the button's state and color.
        """
        if self.isPressed():
            
            self.button_press = True
            self.col_button = COL_BUTTON_ON
        else:
            self.button_press = False
            self.col_button = COL_BUTTON_OFF

        self.text_button = self.font.render(self.str_num_floor, True, self.col_button, self.background)


    # Draw the button on the screen.
    def draw(self, screen):
        '''''
        Draw the button on the screen.
        Arguments:
            screen (pygame.Surface): The screen on which to draw the button.

        Returns:
            None
        '''''
        pygame.draw.circle(screen, (WHITE), ( self.x_pos,self.y_pos), SIZE_BUTTON )
        pygame.draw.circle(screen, (BLACK), ( self.x_pos,self.y_pos), SIZE_BUTTON , 3)
        screen.blit(self.text_button, self.text_button.get_rect(center=(self.x_pos, self.y_pos)))


# --------------------------------------
class Floor:
    """
    The Floor class represents a floor in the elevator system.

    Responsibilities:
    - Manage the floor's properties, such as position and timer.
    - Update the floor's state, including its timer and button state.
    - Draw the floor and its components on the screen.
    """

    def __init__(self , num_floor,floor_img, num_floors, current_x_pos) -> None:
        self.num_floor = num_floor
        self.x_pos = START_X_POS_FLOOR
        self.y_pos = ZERO_FLOOR - (FLOOR_HEIGHT * num_floor) 
        self.timer = 0
        self.timer_str = ''
        self.img = pygame.transform.scale(floor_img, (FLOOR_WIDTH, FLOOR_HEIGHT - SPACER_HEIGHT))
        self.col_num = BLACK
        self.last_update = time.time()
        self.flag_in_execution= False
        self.font = pygame.font.Font('freesansbold.ttf', SIZE_BUTTON)
        # self.rect = self.img.get_rect(center=(self.x_pos, self.y_pos))

        self.current_x_pos = current_x_pos
        self.end_floor = num_floors - 1
        self.button = Button(self.num_floor, self.y_pos, self.current_x_pos)



    def handleEvent(self, event):
        """
        Handle mouse events for the floor.
        Arguments:
            event (pygame.event.Event): The mouse event to handle.

        Returns:
            bool: True if the button on this floor was pressed, False otherwise.
        """
        return self.button.handleEvent(event)
    
    # Set the floor timer and update its state.
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
    def update(self):
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
        self.button.update(self.flag_in_execution)
 
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
  
    # Draw the floor and its components on the screen.
    def draw(self, screen):
        """
        Draw the floor, its dividing line, and its timer (if active) on the screen.
        Arguments:
            screen (pygame.Surface): The screen on which to draw the floor.

        Returns:
            None
        """
        # Print block image.
        screen.blit(self.img, (self.x_pos ,self.y_pos) )   
        # Draw black line between the floors; on the last floor, draw a roof.
        if self.num_floor < self.end_floor:
            pygame.draw.rect(screen, (BLACK), (self.x_pos  ,self.y_pos - SPACER_HEIGHT , FLOOR_WIDTH, SPACER_HEIGHT))
        else:
            pygame.draw.rect(screen, (GREEN), (self.x_pos  ,self.y_pos - SPACER_HEIGHT , FLOOR_WIDTH, SPACER_HEIGHT + 10))

        #     pygame.draw.polygon(screen, BLACK, roof_vertices)

        # If the floor has an active timer, draw the timer on the screen.
        if self.flag_in_execution:
            timer_print = self.timer_str
            text_timer = self.font.render(timer_print , True, WHITE, BLACK)
            screen.blit(text_timer, (X_POS_TIMER, self.y_pos  + 15))
        self.button.draw(screen)