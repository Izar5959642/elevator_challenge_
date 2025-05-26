import pygame
from settings import *

class Button:
    """Represents a button on a floor for requesting an elevator."""
    def __init__ (self, floor_number, y_pos, building_x_pos):
        self.x_pos = X_START_POS_BUTTON
        self.center_x = FLOOR_WIDTH / 2
        self.y_pos = y_pos + (FLOOR_HEIGHT / 2)
        self.center_y = MID_Y_POS + SPACER_HEIGHT
        self.background = WHITE
        self.color = COL_BUTTON_OFF
        self.font = pygame.font.Font('freesansbold.ttf', SIZE_BUTTON_NUM)
        self.is_pressed = False
        self.floor_label = str(floor_number)
        self.text = self.font.render(self.floor_label, True, self.color, self.background)
        self.building_x_pos = building_x_pos
        self.rect = pygame.Rect(
            self.building_x_pos + self.x_pos - SIZE_BUTTON,
            self.y_pos - SIZE_BUTTON,
            SIZE_BUTTON * 2,
            SIZE_BUTTON * 2
        )

    def check_pressed(self):
        """Check if the button is pressed by the mouse. """
        return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())
        
    
    def update(self, is_active, scroll_y, scroll_x):
        """Update button state and appearance based on activity and scroll position."""
        self.rect.y = self.y_pos - SIZE_BUTTON - scroll_y
        self.rect.x = self.building_x_pos + self.x_pos - SIZE_BUTTON - scroll_x
        self.is_pressed = self.check_pressed() or is_active
        self.color = COL_BUTTON_ON if self.is_pressed else COL_BUTTON_OFF
        self.text = self.font.render(self.floor_label, True, self.color, self.background)

    def draw(self, surface):
        """Draw the button on the given surface"""
        pygame.draw.circle(surface, WHITE, (self.center_x, self.center_y), SIZE_BUTTON)
        pygame.draw.circle(surface, BLACK, (self.center_x, self.center_y), SIZE_BUTTON, 3)
        surface.blit(self.text, self.text.get_rect(center=(self.center_x, self.center_y)))


        