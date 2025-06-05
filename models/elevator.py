# Elevator class to manage elevator movement and requests
import pygame
from models.delta_time import DeltaTime
from settings import *
from models.interface_object import IObject

class Elevator(IObject):
    """Represent an elevator with movement and request handling."""
    def __init__(self, elevator_id):
        self.elevator_id = elevator_id
        self.x_pos = START_X_POS_ELV + (DIFF_ELV * elevator_id)
        self.y_pos = ZERO_FLOOR
        self.total_time = 0
        self.requests = []
        self.current_floor = 0
        self.final_destination = 0
        self.image = pygame.transform.scale(pygame.image.load(IMG_ELV), (ELV_WIDTH, ELV_HEIGHT))
        self.sound = pygame.mixer.Sound(MP3)
        self.pause = 0

    def add_request(self, floor_number, total_time):
        """Add a floor request and update total time."""
        self.total_time = total_time + PAUSE
        self.requests.append(floor_number)
        self.final_destination = floor_number

    def calculate_time_for_request(self, floor_number):
        """Calculate the time required for a request to a specific floor."""
        if self.final_destination == floor_number:
            return 0
        dest_for_request = abs(self.final_destination - floor_number)
        time_for_request = dest_for_request * SEC_FOR_FLOOR
        return time_for_request + self.total_time

    def update(self):
        """Update elevator position and time."""
        delta_time = DeltaTime().delta_time
        self.update_total_time(delta_time)
        if self.requests:
            self.move(delta_time)

    def update_total_time(self, delta_time):
        """Update remaining time for requests."""
        if self.total_time > 0.01:
            self.total_time -= delta_time
        else:
            self.total_time = 0

    def arrived(self, delta_time, target_y):
        """Handle the elevator arriving at a floor."""
        self.y_pos = target_y
        self.pause = PAUSE - delta_time
        self.sound.play()  # Play sound when reaching the floor
            
    def move(self, delta_time):
        target_floor = self.requests[0]
        target_y = ZERO_FLOOR - (TOTAL_HEIGHT_FLOOR * target_floor)
        distance = PIX_PER_SEC * delta_time
        direction = 1 if self.current_floor > target_floor else -1
        distance *= direction

        if self.y_pos != target_y:

            self.y_pos += distance

            if (direction == 1 and self.y_pos > target_y) or (direction == -1 and self.y_pos < target_y):
                self.arrived(delta_time, target_y)
                
        else:  # arrived at the target floor and waiting 2 seconds
            self.pause -= delta_time
            if self.pause <= 0:
                self.current_floor = self.requests.pop(0)

    def draw(self, surface):
        """Draw the elevator on the given surface."""
        surface.blit(self.image, (self.x_pos, self.y_pos))
