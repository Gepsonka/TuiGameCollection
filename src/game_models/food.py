import random
from .snake_model import GameElement, SnakeHead, SnakeBody

class Food(GameElement):
    def __init__(self) -> None:
        super().__init__(1, 1)
        
    def reposition_food(self, head: SnakeHead, body: list[SnakeBody]) -> None:
        '''
        Reposition of food obj after got eaten.
        Cannot respawn on the poz of snake's head or any of its bodyparts.
        '''
        while 1:
            self.x_poz = random.randint(0, 100)
            self.y_poz = random.randint(0, 100)
            
            if head == self:
                continue
            
            if any(self == x for x in body):
                continue
            
            return