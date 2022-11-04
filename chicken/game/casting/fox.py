from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from random import *



class Fox(Actor):
    """
    A Fox is a list of foxes moving in a particular direction

    Attributes:
        _foxes (list): The number of foxes in the grass.
        _level (int): The current level of the game
        _image (list): A list of fox images
        _size(int): The fox size
        _speed(int): The fox speed in the specified direction
    """
    def __init__(self, speed, y_position,image, size, level=1):
        super().__init__()
        
        self._foxes = []     
        self._level = level
        self._image = image
        self._size = size
          

        self._speed = speed
        self._prepare_foxes(y_position)
        
    def _prepare_foxes(self, y_position):
        """Begins a for loop that creates a list of foxes for the specified lane y_position

        Args:
            y_position (int): the lane on the y axis
        """
                
        for i in range(0, MAX_X, FOX_GAP * self._gap(self._level)): 
            fox = Actor()
            fox.set_image(self._image[randint(0,0)])
            fox.set_size(self._size)
            x = i
            y = y_position
            position = Point(x, y)
            fox.set_position(position)
            
            self._foxes.append(fox)
            
            
            
    def _gap(self, level):
        if level % 2 == 0:
            return int(level/2)
        else:
            return level     
        
           
    def move_next(self):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        
        for fox in self._foxes:
            x = (fox.get_position().get_x() - (self._speed * self._level)) % MAX_X
            y = fox.get_position().get_y()
            #fox.set_color(Color(randint(0,255), randint(0,255), randint(0,255)))
            
            fox.set_position(Point(x, y))
        
    def get_foxes(self):
        return self._foxes
    
    def stop_foxes(self):
        self._speed = 0
        
    def start_foxes(self, speed):
        if speed <= 0:
            speed = 1
        self._speed = speed


    