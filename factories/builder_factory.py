from abc import ABC, abstractmethod
from models.building import Building
from models.floor import Floor
from models.elevator import Elevator

class AbstractBuildingFactory(ABC):
    """Abstract factory for creating building components."""
    @abstractmethod
    def create_floor(self, floor_id, total_floors, x_pos, max_height):
        pass

    @abstractmethod
    def create_elevator(self, elevator_id):
        pass

    @abstractmethod
    def create_building(self, num_elevators, num_floors, x_pos, max_height):
        pass

class BuildingFactory(AbstractBuildingFactory):
    """Concrete factory for creating standard building components."""
    def create_floor(self, floor_id, total_floors, x_pos, max_height):
        return Floor(floor_id, total_floors, x_pos, max_height)

    def create_elevator(self, elevator_id):
        return Elevator(elevator_id)

    def create_building(self, num_elevators, num_floors, x_pos, max_height):
        floors = [self.create_floor(i, num_floors, x_pos, max_height) for i in range(num_floors)]
        elevators = [self.create_elevator(i) for i in range(num_elevators)]
        return Building(num_elevators, num_floors, x_pos, max_height, floors, elevators)