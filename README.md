# Elevator Simulation

## Overview
This project is a Pygame-based elevator simulation that models a neighborhood with multiple buildings, each containing floors and elevators. Users can interact by clicking floor buttons to request elevators, which are assigned to the fastest available elevator based on travel time. The simulation supports scrolling to view large buildings and provides visual feedback through timers and button states. The project is designed with Object-Oriented Programming (OOP) principles, utilizing design patterns like Singleton and Factory for modularity, readability, and maintainability.

The simulation demonstrates:
- **Realistic elevator movement**: Elevators move smoothly between floors, pausing briefly upon arrival and playing a `ding.mp3` sound.
- **Dynamic building configurations**: Supports multiple buildings with configurable numbers of floors and elevators, defined in `settings.py`.
- **User interaction**: Mouse clicks on floor buttons trigger elevator requests, and mouse wheel scrolling navigates the view.
- **Time management**: A `DeltaTime` Singleton ensures consistent updates across all objects.

This project was developed as a coding challenge for a job interview, showcasing strong OOP practices and clean code.

## Project Structure
```
project_root/
├── assets/
│   ├── images/
│   │   ├── building1.png       # Image for floors
│   │   ├── building.png        # Alternative building image
│   │   └── elv.png             # Image for elevators
│   └── mp3_file/
│       └── ding.mp3            # Sound played when an elevator arrives
├── factories/
│   └── builder_factory.py      # Factory pattern for creating buildings, floors, and elevators
├── models/
│   ├── building.py             # Building class managing floors and elevators
│   ├── button.py               # Button class for floor requests
│   ├── delta_time.py           # Singleton for managing time deltas
│   ├── elevator.py             # Elevator class with movement and request handling
│   ├── floor.py                # Floor class with buttons and timers
│   ├── interface_object.py     # Abstract interface for drawable objects
│   ├── neighborhood.py         # Main class managing buildings and the game loop
├── main.py                     # Main entry point for the simulation
├── settings.py                 # Configuration constants (e.g., screen size, colors)
├── .gitignore                  # Git ignore file for Python bytecode
├── README.md                   # Project documentation
```

## Prerequisites
- **Python 3.8+**: The project uses Python for scripting.
- **Pygame 2.5.2**: A Python library for graphics and sound.

To check if Pygame is installed:
```bash
python3 -c "import pygame; print(pygame.__version__)"
```
If Pygame is not installed, install it:
```bash
pip3 install pygame==2.5.2 --break-system-packages
```

**Note**: The `--break-system-packages` flag is used on Debian/Ubuntu systems to bypass PEP 668 restrictions. Use with caution, as it modifies the system Python environment.

## Setup and Running
1. **Clone or Download the Project**:
   - Ensure all files are in the `project_root/` directory as shown above.
   - The required assets (`building1.png`, `building.png`, `elv.png`, `ding.mp3`) are included in `assets/images/` and `assets/mp3_file/` in the Git repository.

2. **Run the Project**:
   ```bash
   cd /path/to/project_root
   python3 main.py
   ```

3. **Interact with the Simulation**:
   - Click floor buttons to request an elevator.
   - Use the mouse wheel to scroll vertically and horizontally to view different floors and buildings.
   - Close the window or press the close button to exit.

## OOP Design Features
The project emphasizes Object-Oriented Programming with the following design choices:

- **Encapsulation**:
  - Classes like `Elevator`, `Floor`, and `Button` encapsulate their data (e.g., `current_floor`, `timer`, `is_pressed`) and behavior (e.g., `update`, `draw`).
  - Private attributes in `DeltaTime` (e.g., `__delta_time`) protect internal state.

- **Abstraction**:
  - Interfaces like `IObject` (for drawable objects) and `IBuilding` (for building behavior) define clear contracts, enabling extensibility (e.g., new elevator or building types).

- **Single Responsibility Principle**:
  - Each class has a specific role:
    - `Elevator`: Manages movement and request handling.
    - `Floor`: Handles button states and timers.
    - `Button`: Manages user interaction and visual feedback.
    - `Building`: Coordinates floors and elevators.
    - `Neighborhood`: Manages the main loop and rendering.
    - `BuildingFactory`: Creates building components.

- **Singleton Pattern**:
  - The `DeltaTime` class uses the Singleton pattern to manage time deltas globally, ensuring all objects (`Elevator`, `Floor`) use the same time step per frame. This is calculated once per frame via `DeltaTime().update_delta()` in the main loop, improving consistency and performance.

- **Factory Pattern**:
  - The `BuildingFactory` class centralizes the creation of `Building`, `Floor`, and `Elevator` objects, making it easy to extend the system (e.g., adding new elevator types or floor styles).

- **Readable Code**:
  - Clear variable names (e.g., `current_floor`, `scroll_y`) improve readability.
  - Comprehensive docstrings for classes and methods document functionality.
  - Organized directory structure separates models, factories, settings, and assets.

## Configuration
The `settings.py` file defines constants for:
- Screen dimensions (`SCREEN_WIDTH=1500`, `SCREEN_HEIGHT=800`).
- Building configurations (`BUILDING_CONFIGS=[(1, 35), (2, 32), (4, 34), (0, 6), (2, 10), (1, 6), (1, 30)]`).
- Floor and elevator properties (e.g., `FLOOR_WIDTH=250`, `ELV_HEIGHT=67`).
- Colors and asset paths (e.g., `IMG_FLOOR="assets/images/building1.png"`, `MP3="assets/mp3_file/ding.mp3"`).

## Notes
- **Assets**: The project includes valid `building1.png`, `building.png`, `elv.png`, and `ding.mp3` files in the `assets/` directory in the Git repository, requiring no additional setup.
- **Performance**: The `DeltaTime` Singleton optimizes performance by calculating the time delta once per frame, reducing system calls. The use of surfaces (`pygame.Surface`) for buildings and the neighborhood ensures efficient rendering.
- **Extensibility**: The Factory and Singleton patterns, along with abstract interfaces (`IObject`, `IBuilding`), make it easy to add features like new elevator types, pause functionality, or different building styles.

## Troubleshooting
- **Pygame Errors**:
  - If you see `ModuleNotFoundError: No module named 'pygame'`, install Pygame as shown above.
  - If assets fail to load (e.g., `pygame.error: Couldn't open assets/images/building1.png`), ensure the `assets/` directory is in the project root and contains the required files.
- **Simulation Issues**:
  - If elevators or timers behave unexpectedly, verify that `DeltaTime().update_delta()` is called in the main loop (`Neighborhood.go_live` in `neighborhood.py`).
  - Test with smaller building configurations (e.g., `BUILDING_CONFIGS=[(1, 5)]` in `settings.py`) to isolate issues.
  - Ensure the number of elevators and floors is valid (at least 1 elevator and 2 floors, enforced in `Neighborhood.create_buildings`).

For further assistance, contact the project author.

## Author
Created by Yizhar Dahan for a job interview coding challenge.