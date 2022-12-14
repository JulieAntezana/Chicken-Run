from tkinter import font
from constants import *
from game.casting.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
from random import *



class Help(Actor):
    """
    A DISPLAY  at the beginig of the game that that handles game introduction and authors. Also does the job of gameover
    screen with an extra game over text added from  the add_game_over method
    
    Attributes:
        _start_game (bool): The number of points the collision is worth.
        _restart (bool): A boolean value to check the state of the user wants to restart the game after this screen is displayed
        _draw (bool): A boolean value that determines when this screen is displayed.
        _texts (list): A list if texts to be dawn on this screen
        _prepare_text (function): A function that prepares the taxts to be drawn and adds them to a list
    """
    def __init__(self):
        super().__init__()\
            
        self._start_game = False
        self._restart = False
        self._draw = True
        self._texts = []
        
        self._prepare_text()
        
        
        
    def _prepare_text(self):
        """a function that prepares the texts
        """
                
        #Header
        text = Actor()
        text.set_text("Help the Chicken cross the road")
        text.set_font_size(45)
        text.set_color(YELLOW)
        position = Point(100, 30)
        text.set_position(position)
        
        self._texts.append(text)
        
        #Authors
        author = Actor()
        author.set_text("Why: To win the game! ")
        author.set_font_size(25)
        author.set_color(RED)
       
        position = Point(200, 100)
        author.set_position(position)
        
        self._texts.append(author)
        
        author1 = Actor()
        author1.set_text("HOW: By using the Up, Down, Left and Right buttons, ")
        author1.set_font_size(20)
        author1.set_color(GREEN)

        position = Point(200, 140)
        author1.set_position(position)
        
        self._texts.append(author1)
        
        author2 = Actor()
        author2.set_text("TIP 1: Avoid cars and foxes!")
        author2.set_font_size(20)
        author2.set_color(GREEN)

        position = Point(200, 180)
        author2.set_position(position)
        
        self._texts.append(author2)
        
        author3 = Actor()
        author3.set_text("TIP 2: Jump from log to log to cross the river.")
        author3.set_font_size(20)
        author3.set_color(GREEN)

        position = Point(200, 220)
        author3.set_position(position)
        
        self._texts.append(author3)
        
        #Prompt
        prompt = Actor()
        prompt.set_text("Good luck! Press Spacebar To Begin")
        prompt.set_font_size(20)
        prompt.set_color(RED)

        position = Point(200, 280)
        prompt.set_position(position)
        
        self._texts.append(prompt)

        #Prompt
        prompt = Actor()
        prompt.set_text("Authors: Marcus Ojo-Osasere, Julie Antezana & Rune Larsen")
        prompt.set_font_size(20)
        prompt.set_color(YELLOW)
        position = Point(200, 360)
        prompt.set_position(position)

        self._texts.append(prompt)
        

    def set_draw(self, value):
        """sets the draw state of this screen

        Args:
            value (boolean): state of the screen
        """
        self._draw = value
        

    def get_draw(self):
        return self._draw
    
    
    def get_texts(self):
        return self._texts
    
    
    def add_game_over(self):
        """Adds a game over text to the list of texts beeing drawn on the screen
        """
        prompt = Actor()
        prompt.set_text("Game Over")
        prompt.set_font_size(25)
        prompt.set_color(RED)

        position = Point(250, 320)
        prompt.set_position(position)
        
        self._texts.append(prompt)
        
        self.game_over = True
        
    
    def change_game_state(self, state):
        """changes the initial state of the game

        Args:
            state (boolean): state of the game

        """
        
        self._start_game = state
        
    def get_game_state(self):
        return self._start_game
    
    def set_restart(self, state):
        """set's the restart attribute of the game screen

        Args:
            state (booleean): state of the restart
        """
        self._restart = state
        
    def restart_state(self):
        return self._restart

        

    