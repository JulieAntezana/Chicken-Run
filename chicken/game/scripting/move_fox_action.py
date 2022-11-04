from game.scripting.action import Action

class MoveFoxAction(Action):
    def execute(self, cast, script):
        """Executes the move_next on the fox action.


        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """        
        self._move_fox(cast)

    def _move_fox(self, cast):
        """calls the move.next() method that handles the movement of the fox
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        foxs = cast.get_actors("fox")
        for fox in foxs:
            fox.move_next()
