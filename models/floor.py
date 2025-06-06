import pygame
from settings import *
from models.delta_time import DeltaTime
from models.button import Button
from models.interface_object import IObject

class Floor(IObject):
    """Represents a floor with a button and timer."""
    def __init__(self, floor_number, total_floors, building_x_pos):
        self.floor_number = floor_number
        self.x_pos = START_X_POS_FLOOR
        self.y_pos = ZERO_FLOOR - (TOTAL_HEIGHT_FLOOR * floor_number)
        self.timer = 0
        self.timer_str = ''
        self.image = pygame.transform.scale(pygame.image.load(IMG_FLOOR), (FLOOR_WIDTH, TOTAL_HEIGHT_FLOOR - SPACER_HEIGHT))
        self.is_active = False
        self.font = pygame.font.Font('freesansbold.ttf', SIZE_BUTTON)
        self.building_x_pos = building_x_pos
        self.top_floor = total_floors - 1
        self.button = Button(floor_number, self.y_pos, building_x_pos)
        self.surface = pygame.Surface((FLOOR_WIDTH, TOTAL_HEIGHT_FLOOR), pygame.SRCALPHA)

    def set_request(self, time):
        """Set the floor's timer and mark as active."""
        self.timer = time
        self.is_active = True

    def update(self, scroll_y, scroll_x):
        """Update timer and button state."""
        if self.timer > 0.01:
            self.timer -= DeltaTime().delta_time
        else:
            self.timer = 0
            self.is_active = False
        self.update_timer_str()
        self.button.update(self.is_active, scroll_y, scroll_x)

    def update_timer_str(self):
        """Convert timer to string format for display."""
        int_timer = int(self.timer)
        decimal_timer = str(self.timer - int_timer)[2:4]
        self.timer_str = f"{int_timer}.{decimal_timer}"

    def draw(self):
        """Draw the floor and its components on its surface."""
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(self.image, (0, SPACER_HEIGHT))
        if self.floor_number < self.top_floor:
            pygame.draw.rect(self.surface, BLACK, (0, 0, FLOOR_WIDTH, SPACER_HEIGHT))
        else:
            pygame.draw.rect(self.surface, RED, (0, 0, FLOOR_WIDTH, SPACER_HEIGHT))
        if self.is_active:
            text_timer = self.font.render(self.timer_str, True, WHITE, BLACK)
            self.surface.blit(text_timer, (X_POS_TIMER, FLOOR_HEIGHT // 2))
        self.button.draw(self.surface)
        