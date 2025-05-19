from abc import ABC, abstractmethod

import pygame
from models.building import Building, IBuilding
from models.elevator import Elevator
from models.floor import Floor
from my_setting import IMG_FLOOR , IMG_ELV 


# class BuilderFactory(ABC):
#     @abstractmethod
#     def create_elevator(self, id, img_elv):
#         pass
    
#     @abstractmethod
#     def create_floor(self, id, img_floor, num_floors):
#         pass


# class BuildingFactory(BuilderFactory):

#     def create_floor(self, id, img_floor, num_floors, current_x_pos, max_building_height):
#         return Floor(id, img_floor, num_floors, current_x_pos, max_building_height)
    
#     def create_elevator(self, id, img_elv):
#         return Elevator(id, img_elv)
    

# class BuildingFactory:
#     def __init__(self, factory):
#         self.factory = factory

#     def create_building(self, num_elevators, num_floors, current_x_pos, max_building_height):
#         return Building(num_elevators, num_floors, current_x_pos, max_building_height, self.factory)



# class BuildingFactory:
#     def __init__(self, factory):
#         self.factory = factory

#     def create_building(self, num_elevators, num_floors, current_x_pos, max_building_height):
#         return Building(num_elevators, num_floors, current_x_pos, max_building_height, self.factory)
    
#     def create_floor(self, id, img_floor, num_floors, current_x_pos, max_building_height):
#         return Floor(id, img_floor, num_floors, current_x_pos, max_building_height)
#     def create_elevator(self, id, img_elv):
#         return Elevator(id, img_elv)

class BuildingFactory:
    """
    A factory class responsible for creating buildings, floors, and elevators.
    """

    def create_building(self, num_elevators, num_floors, current_x_pos, max_building_height) -> IBuilding:
        """
        Create a Building object with the specified parameters.
        """
        floors = [Floor(i, num_floors, current_x_pos, max_building_height) for i in range(num_floors)]
        elevators = [Elevator(i) for i in range(num_elevators)]
        return Building(num_elevators, num_floors, current_x_pos, max_building_height, floors, elevators)

