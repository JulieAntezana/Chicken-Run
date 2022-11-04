from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from random import *



class Grass(Actor):
    """The grass is where the the fox hangs out
        Attributes:
            start position Point(int, int): The start x and y position of the banner.
            start position Point(int, int): The end x and y position of the banner.
            color: The color of the banner."""
        
    def __init__(self):
        super().__init__()
  
        #grass
        start = Point(0, MAX_Y-370)
        end = Point(MAX_X, 50)
        self.set_position(start)
        self.set_end_position(end)
        self.set_color(GREEN)
        




    