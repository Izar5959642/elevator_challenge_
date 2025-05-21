from abc import ABC, abstractmethod
import pygame
from settings import *

class IBuilding(ABC):
    """Abstract interface for a building."""
    @abstractmethod
    def handle_request(self, floor_number):
        pass

    @abstractmethod
    def handle_mouse_click(self):
        pass

    @abstractmethod
    def update_all(self, scroll_y):
        pass

    @abstractmethod
    def draw_all(self):
        pass



class Building(IBuilding):
    """Represents a building with floors and elevators."""
    def __init__(self, num_elevators, num_floors, x_pos, max_height, floors, elevators):
        self.num_elevators = num_elevators
        self.num_floors = num_floors
        self.x_pos = x_pos
        self.width = num_elevators * ELV_WIDTH + START_X_POS_ELV + START_X_POS_FLOOR
        self.height = num_floors * FLOOR_HEIGHT
        self.max_height = max_height
        self.floors = floors
        self.elevators = elevators
        self.surface = pygame.Surface((self.width, self.max_height), pygame.SRCALPHA)

    def handle_request(self, floor_number):
        """Assign a floor request to the best elevator."""
        if self.floors[floor_number].is_active:
            return
        min_time, best_elevator_idx = float('inf'), 0
        for i, elevator in enumerate(self.elevators):
            time = elevator.calculate_time_for_request(floor_number)
            if time < min_time:
                min_time, best_elevator_idx = time, i
        if not self.floors[floor_number].is_active:
            self.elevators[best_elevator_idx].add_request(floor_number, min_time + PAUSE)
            self.floors[floor_number].set_request(min_time)

    def handle_mouse_click(self):
        """Process mouse clicks on floor buttons."""
        for floor_number, floor in enumerate(self.floors):
            if floor.button.check_pressed():
                self.handle_request(floor_number)

    def update_all(self, scroll_y):
        """Update all floors and elevators."""
        for floor in self.floors:
            floor.update(scroll_y)
        for elevator in self.elevators:
            elevator.update()

    def draw_all(self):
        """Draw all floors and elevators on the building's surface."""
        self.surface.fill((0, 0, 0, 0))
        for floor in self.floors:
            floor.draw()
            self.surface.blit(floor.surface, (floor.x_pos, floor.y_pos))
        for elevator in self.elevators:
            elevator.draw(self.surface)
