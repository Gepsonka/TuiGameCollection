from enum import Enum
import random
from tkinter.tix import DirTree
from xxlimited import foo

class MapState(Enum):
    EMPTY = 0
    HEAD = 1
    BODY = 2
    FOOD = 3
    
class GameState(Enum):
    GAME_OVER = 1
    ONGOING = 0
    
    
class Direction(Enum):
    UP = 'Up'
    DOWN = 'Down'
    LEFT = 'Left'
    RIGHT = 'Right'



class GameElement:
    '''
    Represents a game object, contains all the basic functionality.
    '''
    def __init__(self, x_poz: int, y_poz: int) -> None:
        self.x_poz = x_poz
        self.y_poz = y_poz
        
    def change_position(self, x: int, y: int) -> None:
        '''
        Change position of block on the map
        '''
        self.x_poz = x
        self.y_poz = y
    
    def __eq__(self, __o: object) -> bool:
        return self.x_poz == __o.x_poz and self.y_poz == __o.y_poz
    
    

class SnakeBody(GameElement):
    pass


class SnakeHead(GameElement):
    def __init__(self, x_poz: int, y_poz: int, direction: Direction) -> None:
        self.direction = direction
        super().__init__(x_poz, y_poz)
        
    def update(self) -> None:
        match self.direction:
            case Direction.UP:
                self.y_poz = (self.y_poz - 1)%99
            
            case Direction.DOWN:
                self.y_poz = (self.y_poz + 1)%99

            case Direction.RIGHT:
                self.x_poz = (self.x_poz + 1)%99
                
            case Direction.LEFT:
                self.x_poz = (self.x_poz - 1)%99
        
    def is_collided_with_bodypart(self, body: list[SnakeBody]) -> bool:
        return any(self == x for x in body)
        
    def is_food_eaten(self, food) -> bool:
        return self == food
        
        
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


class SnakeModel:
    def __init__(self):
        self.map = [[MapState.EMPTY for j in range(100)] for i in range(100)]
        self.food = Food()
        self.head = SnakeHead(10, 10, Direction.RIGHT)
        self.body = []
        
        self.map[self.head.y_poz][self.head.x_poz] = MapState.HEAD
        self.map[self.food.y_poz][self.food.x_poz] = MapState.FOOD
        
        self.game_state = GameState.ONGOING
        self.score = 0
        
    def update(self):
        if self.game_state == GameState.GAME_OVER:
            return
        
        self.move_body()
        self.head.update()
        
        self.game_conditions()
        
    def game_conditions(self):
        self.food_eaten()
        self.bodypart_collided()
    
    def food_eaten(self):
        if self.head.is_food_eaten(self.food):
            self.append_bodypart()
            self.food.reposition_food(self.head, self.body)
            self.score += 1
        
    def bodypart_collided(self):
        if self.head.is_collided_with_bodypart(self.body):
            self.game_state = GameState.GAME_OVER
            
    def move_body(self):
        for i in range(len(self.body)-1, 0, -1):
            if i == 0:
                break
            self.body[i].x_poz = self.body[i-1].x_poz
            self.body[i].y_poz = self.body[i-1].y_poz
        
        if self.body:
            self.body[0].x_poz = self.head.x_poz
            self.body[0].y_poz = self.head.y_poz
            
    
    def append_bodypart(self):
        if len(self.body) >= 2:
            if self.body[len(self.body)-2].x_poz-1 == self.body[len(self.body)-1].x_poz and self.body[len(self.body)-2].y_poz == self.body[len(self.body)-1].y_poz:
                self.body.append(SnakeBody(self.body[len(self.body)-1].x_poz + 1, self.body[len(self.body)-1].y_poz))
            elif self.body[len(self.body)-2].x_poz+1 == self.body[len(self.body)-1].x_poz and self.body[len(self.body)-2].y_poz == self.body[len(self.body)-1].y_poz:
                self.body.append(SnakeBody(self.body[len(self.body)-1].x_poz - 1, self.body[len(self.body)-1].y_poz))
            elif self.body[len(self.body)-2].y_poz-1 == self.body[len(self.body)-1].y_poz and self.body[len(self.body)-2].x_poz == self.body[len(self.body)-1].x_poz:
                self.body.append(SnakeBody(self.body[len(self.body)-1].x_poz, self.body[len(self.body)-1].y_poz + 1))
            elif self.body[len(self.body)-2].y_poz+1 == self.body[len(self.body)-1].y_poz and self.body[len(self.body)-2].x_poz == self.body[len(self.body)-1].x_poz:
                self.body.append(SnakeBody(self.body[len(self.body)-1].x_poz, self.body[len(self.body)-1].y_poz - 1))
        else:
            match self.head.direction:
                case Direction.UP:
                    self.body.append(SnakeBody(self.head.x_poz, self.head.y_poz + 1))
                case Direction.DOWN:
                    self.body.append(SnakeBody(self.head.x_poz, self.head.y_poz - 1))
                case Direction.RIGHT:
                    self.body.append(SnakeBody(self.head.x_poz - 1, self.head.y_poz))
                case Direction.LEFT:
                    self.body.append(SnakeBody(self.head.x_poz + 1, self.head.y_poz))
            
    
            
        

