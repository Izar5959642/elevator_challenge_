import pygame
import time
from settings import *

class Elevator:
    """Represent an elevator with movement and request handling. """

    def __init__(self, elevator_id):
        self.elevator_id = elevator_id
        self.x_pos = START_X_POS_ELV + (DIFF_ELV * elevator_id)
        self.y_pos = ZERO_FLOOR
        self.current_floor = 0
        self.total_time = 0
        self.last_update = time.time()
        self.requests = []
        self.final_destination = 0
        self.image = pygame.transform.scale(pygame.image.load(IMG_ELV), (ELV_WIDTH, ELV_HEIGHT))
        self.sound = pygame.mixer.Sound(MP3)       
        self.pause = 0

    def add_request(self, floor_number, total_time):
        """Add a floor request and update total time."""
        self.requests.append(floor_number)
        self.total_time = total_time
        self.final_destination = floor_number

    def calculate_time_for_request(self, floor_number):
        if self.final_destination == floor_number:
            return 0
        diff = abs(self.final_destination - floor_number) * SEC_FOR_FLOOR
        return diff + self.total_time

    def update(self):
        """Update elevator position and time."""
        diff = time.time() - self.last_update
        self.last_update = time.time()
        self.update_total_time(diff)
        if self.requests:
            self.move(diff)
        
        
    def update_total_time(self, diff):
        """Update remaining time for requests."""
        if self.total_time >= 0.01:
            self.total_time -= diff
        else:
            self.total_time = 0

    def move(self, diff):
        """Move elevator to the target floor."""
        target_floor = self.requests[0]
        target_y = ZERO_FLOOR - (FLOOR_HEIGHT * target_floor)
        distance = PIX_PER_SEC * diff
        direction = 1 if self.current_floor > target_floor else -1
        distance *= direction 

        if self.y_pos !=  target_y:
            self.y_pos += distance
            if (direction == 1 and self.y_pos > target_y) or (direction == -1 and self.y_pos < target_y):
                self.y_pos = target_y
                self.pause = PAUSE
        elif self.pause > 0:
            if self.pause == PAUSE:
                self.sound.play()
            self.pause -= diff
        else:
            self.current_floor = self.requests.pop(0)
        

    def draw(self, surface):
        """Draw the elevator on the given surface."""
        surface.blit(self.image, (self.x_pos, self.y_pos))


# dalta().get_dalta()