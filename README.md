# Elevator Simulation

## Overview
This project is a Pygame-based elevator simulation that models multiple buildings, each with floors and elevators. Users can click floor buttons to request elevators, and the system assigns the fastest available elevator to each request. The project is designed with Object-Oriented Programming (OOP) principles, featuring design patterns like Singleton and Factory to ensure modularity, readability, and maintainability.

The simulation demonstrates:
- **Realistic elevator movement**: Elevators move between floors with smooth animations and play a sound (`ding.mp3`) upon arrival.
- **Dynamic building configurations**: Supports multiple buildings with varying numbers of floors and elevators.
- **User interaction**: Mouse clicks on floor buttons trigger elevator requests, with timers displayed on active floors.

This project was developed as a coding challenge for a job interview, showcasing strong OOP practices and clean code.

## Project Structure
```
project_root/
├── factories/
│   └── builder_factory.py      # Factory pattern for creating buildings, floors, and elevators
├── models/
│   ├── button.py               # Button class for floor requests
│   ├── delta_time.py           # Singleton for managing time deltas
│   ├── elevator.py             # Elevator class with movement and request handling
│   ├── floor.py                # Floor class with buttons and timers
│   ├── building.py             # Building class managing floors and elevators
│   └── delta_time.py           # delta time singleton 
├── assets/
│   ├── images/
│   │   ├── building.png        # Image for floors
│   │   └── elv.png             # Image for elevators
│   └── mp3_file/
│       └── ding.mp3            # Sound played when an elevator arrives
├── main.py                     # Main game loop and entry point
├── settings.py                 # Configuration constants (e.g., screen size, colors)
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
   - The required assets (`building.png`, `elv.png`, `ding.mp3`) are included in `assets/images/` and `assets/mp3_file/`.

2. **Run the Project**:
   ```bash
   cd /path/to/project_root
   python3 main.py
   ```

3. **Interact with the Simulation**:
   - Click floor buttons to request an elevator.
   - Scroll the mouse wheel to view different floors.
   - Close the window to exit.

## OOP Design Features
The project emphasizes Object-Oriented Programming with the following design choices:

- **Encapsulation**:
  - Classes like `Elevator`, `Floor`, and `Button` encapsulate their data (e.g., `current_floor`, `timer`) and behavior (e.g., `update`, `draw`).
  - Private attributes in `DeltaTime` (e.g., `__delta_time`) protect internal state.

- **Abstraction**:
  - The `IBuilding` abstract interface defines a clear contract for building behavior, allowing future extensions (e.g., different building types).

- **Single Responsibility Principle**:
  - Each class has a specific role:
    - `Elevator`: Manages movement and requests.
    - `Floor`: Handles button states and timers.
    - `Button`: Manages user interaction and display.
    - `Building`: Coordinates floors and elevators.

- **Singleton Pattern**:
  - The `DeltaTime` class uses the Singleton pattern to manage time deltas globally. It ensures all objects (`Elevator`, `Floor`) use the same time step per frame, calculated once in the main loop via `update_delta`. This eliminates redundant calculations and improves consistency.

- **Factory Pattern**:
  - The `BuildingFactory` class centralizes the creation of `Building`, `Floor`, and `Elevator` objects. It uses the Factory pattern to make object creation flexible and extensible (e.g., for adding new elevator types).

- **Readable Code**:
  - Clear variable names (e.g., `current_floor` instead of `where_m_i`).
  - Comprehensive docstrings for all classes and methods.
  - Organized directory structure separating models, factories, and settings.

## Notes
- **Assets**: The project includes valid `building.png`, `elv.png`, and `ding.mp3` files in the `assets/` directory, so no additional asset setup is required.
- **Performance**: The `DeltaTime` Singleton optimizes performance by calculating the time delta once per frame, reducing system calls.
- **Extensibility**: The Factory and Singleton patterns make it easy to add new features, such as different elevator types or pause functionality.

## Troubleshooting
- **Pygame Errors**:
  - If you see `ModuleNotFoundError: No module named 'pygame'`, install Pygame as shown above.
- **Simulation Issues**:
  - If elevators or timers behave unexpectedly, ensure `DeltaTime().update_delta()` is called in the main loop (in `main.py`).
  - Test with smaller building configurations (e.g., `BUILDING_CONFIGS = [(3, 5)]` in `settings.py`) to isolate issues.

For further assistance, contact the project author.

## Author
Created by Yizhar Dahan for a job interview coding challenge.