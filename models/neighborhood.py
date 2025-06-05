import pygame
from factories.builder_factory import BuildingFactory
from models.delta_time import DeltaTime
from settings import  MAX_BUILDING_HEIGHT, SCREEN_HEIGHT, SCREEN_WIDTH, SCROLL_SPEED


class Neighborhood:
    """A placeholder class for future neighborhood-related features."""
    def __init__(self,configs, max_height): 
        pygame.mixer.init()
        pygame.mixer.set_num_channels(64)
        pygame.display.set_caption('Elevator Challenge')

        self.create_buildings(configs, max_height ) 
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.scrollable_surface = pygame.Surface((self.total_width, MAX_BUILDING_HEIGHT), pygame.SRCALPHA)
        self.scroll_y = max(0, MAX_BUILDING_HEIGHT - SCREEN_HEIGHT)
        self.scroll_x = 0

    def go_live(self):
        """Run the main loop for the neighborhood."""
        run = True
        while run:
            run = self.handle_events()
            DeltaTime().update_delta()
            self.draw_screen()


    def create_buildings(self, configs, max_height):
        """Create buildings with specified configurations."""
        factory = BuildingFactory()
        self.buildings = []
        current_x_pos = 0
        for num_elevators, num_floors in configs:
            num_elevators = max(1, num_elevators)  # Ensure at least one elevator
            num_floors = max(2, num_floors)  # Ensure at least two floors
            building = factory.create_building(num_elevators, num_floors, current_x_pos, max_height)
            self.buildings.append(building)
            current_x_pos += building.width
            self.total_width = current_x_pos
        

    def handle_events(self):
        """Handle user input and scrolling events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:

                mouse_pos = pygame.mouse.get_pos()
                for building in self.buildings:
                    local_x = mouse_pos[0] - building.x_pos + self.scroll_x
                    if 0 <= local_x < building.width:
                        building.handle_mouse_click()
                        break
                    
            if event.type == pygame.MOUSEWHEEL:
                self.scroll_y -= event.y * SCROLL_SPEED
                self.scroll_y = max(0, min(self.scroll_y, MAX_BUILDING_HEIGHT - SCREEN_HEIGHT))
                self.scroll_x -= event.x * SCROLL_SPEED
                self.scroll_x = max(0, min(self.scroll_x, self.total_width - SCREEN_WIDTH))

        return True

    def draw_screen(self):
        """Draw all buildings on the screen."""
        self.scrollable_surface.fill((255, 255, 255))
        self.screen.fill((255, 255, 255))
        for building in self.buildings:
            building.update_all(self.scroll_y, self.scroll_x)
            building.draw_all()
            self.scrollable_surface.blit(building.surface, (building.x_pos, 0))
        self.screen.blit(self.scrollable_surface, (-self.scroll_x, -self.scroll_y))
        pygame.display.update()
