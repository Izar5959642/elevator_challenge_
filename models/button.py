import pygame
from my_setting import *



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
        self.is_x_pos = FLOOR_WIDTH / 2 
        self.y_pos = y_pos + (FLOOR_HEIGHT / 2)
        self.is_y_pos = MID_Y_POS + SPACER_HEIGHT
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

    def isPressed(self):
        """
        Check if the button was pressed.
        Returns:
            bool: True if the button is pressed, False otherwise.
        """
        if pygame.mouse.get_pressed()[0]:  # Check if the left mouse button is pressed
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                return True
        return False
    
    def update(self, button_press, scroll_y):
        """
        Update the button's state and color.
        """
        self.rect.y = self.y_pos - SIZE_BUTTON - scroll_y

        if self.isPressed() or button_press:   
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
        pygame.draw.circle(screen, (WHITE), ( self.is_x_pos, self.is_y_pos), SIZE_BUTTON )
        pygame.draw.circle(screen, (BLACK), ( self.is_x_pos, self.is_y_pos), SIZE_BUTTON , 3)
        screen.blit(self.text_button, self.text_button.get_rect(center=(self.is_x_pos, self.is_y_pos)))

