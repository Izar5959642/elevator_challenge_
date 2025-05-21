import time 

def singleton(cls):
    """Decorator to ensure a class has only one instance."""
    instance = {}
    def get_instance(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return get_instance


@singleton
class DeltaTime:
    """Manges time delta for entire system using the Singleton pattern"""

    def __init__(self):
        self.__last_time_update = time.time()
        self.__delta_time = 0.0

    @property
    def delta_time(self):
        """Return the current time delta."""
        return self.__delta_time
    
    def update_delta(self):
        """Update the time delta based on the current time."""
        current_time = time.time()
        self.__delta_time = current_time - self.__last_time_update
        self.__last_time_update = current_time