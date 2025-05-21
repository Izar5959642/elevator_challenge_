import pygame
from factories.builder_factory import BuildingFactory
from models.delta_time import DeltaTime
from settings import BUILDING_CONFIGS, MAX_BUILDING_HEIGHT, SCREEN_HEIGHT

# Initialize Pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(64)
pygame.display.set_caption('Elevator Challenge')

def create_buildings(factory, configs, max_height):
    """Create buildings with specified configurations."""
    buildings = []
    current_x_pos = 0
    for num_elevators, num_floors in configs:
        num_elevators = max(1, num_elevators)  # Ensure at least one elevator
        num_floors = max(2, num_floors)  # Ensure at least two floors
        building = factory.create_building(num_elevators, num_floors, current_x_pos, max_height)
        buildings.append(building)
        current_x_pos += building.width
    return buildings, current_x_pos

def handle_events(buildings, scroll_y):
    """Handle user input and scrolling events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, scroll_y
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for building in buildings:
                local_x = mouse_pos[0] - building.x_pos
                if 0 <= local_x < building.width:
                    building.handle_mouse_click()
                    break
        if event.type == pygame.MOUSEWHEEL:
            scroll_y -= event.y * 20
            scroll_y = max(0, min(scroll_y, MAX_BUILDING_HEIGHT - SCREEN_HEIGHT))
    return True, scroll_y

def draw_screen(screen, scrollable_surface, buildings, scroll_y):
    """Draw all buildings on the screen."""
    scrollable_surface.fill((255, 255, 255))
    screen.fill((255, 255, 255))
    for building in buildings:
        building.update_all(scroll_y)
        building.draw_all()
        scrollable_surface.blit(building.surface, (building.x_pos, 0))
    screen.blit(scrollable_surface, (0, -scroll_y))
    pygame.display.update()

# Main program
factory = BuildingFactory()
buildings, total_width = create_buildings(factory, BUILDING_CONFIGS, MAX_BUILDING_HEIGHT)
screen = pygame.display.set_mode((total_width, SCREEN_HEIGHT))
scrollable_surface = pygame.Surface((total_width, MAX_BUILDING_HEIGHT), pygame.SRCALPHA)
scroll_y = max(0, MAX_BUILDING_HEIGHT - SCREEN_HEIGHT)

run = True
while run:
    run, scroll_y = handle_events(buildings, scroll_y)
    DeltaTime().update_delta()
    draw_screen(screen, scrollable_surface, buildings, scroll_y)

pygame.quit()