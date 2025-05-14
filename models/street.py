
from my_setting import *

import json

def parse_building_settings(json_data):
    try:
        # Parse JSON string into a dictionary
        building_data = json.loads(json_data)
        
        # Create a list of tuples (num_of_floors, num_of_elevators) directly from values
        building_list = [
            (info["num_of_floors"], info["num_of_elevators"]) 
            for info in building_data.values()
        ]
        
        return building_list
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        print(f"Error parsing building settings: {e}")
        return []



class Street:

    def __init__(self, num_of_buildings, settings_json):

        settings = parse_building_settings(settings_json)
        max_floors = max(settings)[0]
        max_elevators = max(settings, key=lambda element: element[1])[1]

        surface_height = (max_floors + SPACER_HEIGHT) * FLOOR_HEIGHT
        surface_width = FLOOR_WIDTH + ELV_MARGIN + max_elevators * (ELV_WIDTH + ELV_MARGIN)

        self.buildings = []

        for building_num in range(num_of_buildings):
            
            building_surface = pygame.Surface((surface_width, surface_height))
            self.buildings.append[Building(building_surface)]
            

    def draw(self):
        for building in self.buildings:
            building.draw()