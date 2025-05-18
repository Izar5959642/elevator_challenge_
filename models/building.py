import pygame
from my_setting import *
from models.floor import *
from models.elevator import *
from abc import ABC, abstractmethod
from pygame.locals import *
class BuilderFactory(ABC):
    @abstractmethod
    def create_elevator(self, id, img_elv):
        pass
    
    @abstractmethod
    def create_floor(self, id, img_floor, num_floors):
        pass

class ElevatorFactory(BuilderFactory):
    def create_floor(self, id, img_floor, num_floors, current_x_pos):
        return Floor(id, img_floor, num_floors, current_x_pos)
    
    def create_elevator(self, id, img_elv):
        return Elevator(id, img_elv)

class Building():
    """
    The Building class represents the entire building, containing multiple elevators and floors.

    Responsibilities:
    - Initialize the elevators and floors.
    - Handle mouse click events to register floor requests.
    - Assign the best elevator for a floor request.
    - Update the state of all elevators and floors.
    - Draw all elevators and floors on the screen.
    """

    # def __init__(self, num_elevator, num_floors, current_x_pos, factory: BuilderFactory) -> None:
        # self.img_elv = pygame.image.load(IMG_ELV)
        # self.img_floor = pygame.image.load(IMG_FLOOR)
        # self.elevators = []
        # self.floors = []
        # self.width = num_elevator * ELV_WIDTH + FLOOR_WIDTH
        # self.height = num_floors * FLOOR_HEIGHT
        # self.num_floors = num_floors
        # self.num_elevator = num_elevator

        # self.current_x_pos = current_x_pos
        # # Initialize elevators.
        # for i in range(num_elevator):
        #     self.elevators.append(factory.create_elevator(i, self.img_elv))
        # # Initialize floors.
        # for i in range(num_floors):
        #     # print("in create building ", i, self.current_x_pos)
        #     self.floors.append(factory.create_floor(i, self.img_floor, num_floors, self.current_x_pos))
    def __init__(self, num_elevator, num_floors, current_x_pos, factory: BuilderFactory) -> None:
        self.num_elevator = num_elevator
        self.num_floors = num_floors
        self.current_x_pos = current_x_pos
        self.factory = factory
        self.width = num_elevator * ELV_WIDTH + START_X_POS_ELV + START_X_POS_FLOOR 
        self.height = num_floors * FLOOR_HEIGHT
        self.floors = [factory.create_floor(i, pygame.image.load(IMG_FLOOR), num_floors, current_x_pos) for i in range(num_floors)]
        self.elevators = [factory.create_elevator(i, pygame.image.load(IMG_ELV)) for i in range(num_elevator)]
        self.surface = self.createSurface()  # Create the surface during initialization
       

    def createSurface(self):
        """
        Create and return the surface for this building.
        This surface includes all floors and elevators.
        Arguments:
            current_x_pos (int): The x position of the building in the world.
        """
        building_surface = pygame.Surface((self.width , max(self.height, SCREEN_HEIGHT)), pygame.SRCALPHA)
        return building_surface
    



    # Check if the mouse click is on any floor button, and handle the request if it is.
    def getMouseClickPos(self):
        """"
        Check if the mouse click is on a floor button and process the request.
        Arguments:
            x_pos_mouse (int): The x position of the mouse click.
            y_pos_mouse (int): The y position of the mouse click.

        Returns:
            None
        """""
        for num_floor, floor in enumerate(self.floors):
                if floor.button.isPressed():
                    self.getNewReq(num_floor)

    # Process a new floor request and assign it to the best elevator.
    def getNewReq(self, num_floor):
        """
        Process a new floor request and assign it to the best available elevator.
        Arguments:
            num_floor (int): The floor number where the request originated.

        Returns:
            None
        """
        # If the floor request is already in execution, skip it.
        if self.floors[num_floor].flag_in_execution == True:
            return
        # Find the elevator with the minimum time to fulfill the request.
        mini = [float('inf') , 0] # (min_time, num_elv)

        for i ,elv in enumerate(self.elevators):
            time_elv_get_floor = elv.calculateTimeForNewReq(num_floor)
            if mini[0] > time_elv_get_floor:
                mini[0] = time_elv_get_floor
                mini[1] = i
       
        # Assign the request to the best elevator and update the floor's state.
        if self.floors[num_floor].flag_in_execution == False :
            self.elevators[mini[1]].appendReq(num_floor,mini[0] + PAUSE)
            self.floors[num_floor].byOrder(mini[0])
        return
    
    # Update the state of all elevators and floors.
    def updateAll(self,scroll_y):
        """
        Update the state of all elevators and floors.
        Arguments:
            None
        Returns:
            None
        """
        for i in range(self.num_floors):
            self.floors[i].update(scroll_y) 
        for i in range(self.num_elevator):
            self.elevators[i].update()

    # Draw all elevators and floors on the screen.       
    def drawAll(self):
        """
        Draw all elevators and floors on the screen.
        Arguments:
            screen (pygame.Surface): The screen on which to draw the elevators and floors.
        Returns:
            None
        """
        self.surface.fill((0, 0, 0, 0)) 

        for floor in self.floors:
            floor.draw(self.surface)
        for elv in self.elevators:
            elv.draw(self.surface)
        
