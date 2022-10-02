import pygame
from game_models.snake_model import SnakeModel, Direction, GameState

class GameWindow:
    '''
    Class which every game should inherit.
    Initialises the game window, like a stage for the game, everything happens here.
    Params
    ======
    winx,winy: size of the window
    clock: every pygame game needs a clock. Determines how many frames will happen in each second.
    my_font: declares default font
    sahred_obj: python multiprocessing.Manager().dict() object. Enables gestures. (form:{'0':''})
    '''
    def __init__(self) -> None:
        pygame.init()
        self.win=pygame.display.set_mode((500,500)) # defining the size of the game window
        pygame.display.set_caption('Snake') # window title
        self.clock=pygame.time.Clock() # init clock : this will define how many frames we are gonn have each sec
        self.my_font=pygame.font.SysFont('monospace',16) # defoault font
        self.game_over_font = pygame.font.SysFont('monospace', 25)
    
    def exit_game(self):
        '''Simply quitting from the program'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                

class SnakeGame(GameWindow):
    '''
    SnakeGame inherits GameWindow
    Params
    ======
    score: you get a score each time you eat food with the snake
    run: bool for the main loop
    up,down,right,left: indicates the direction of the snake\'s head
    bodyparts: coordinate of every bodypart
    food: the exact renderable food element
    '''    
    def __init__(self) -> None:
        super().__init__()
        self.model = SnakeModel()


    def main_loop(self):
        '''
        Main loop of the game.
        Everythin happens here.
        '''
        self.run=True
        i=0
        while self.run:
            self.clock.tick(24) # the game will display 24 frames per second
            for event in pygame.event.get(): # check if an exit event occurs
                if event.type==pygame.QUIT:
                    self.run=False

            self.store_key_events()
            self.process_keystroke()
            self.redefine_game_window()
            
            if i==2:
                i=0
                self.model.update()
            
            i+=1
            
        
        self.exit_game() # after the main loop we exit the game
        exit(0)

            
    def store_key_events(self):
        '''Storing the key-press events.'''
        self.key_events=pygame.key.get_pressed()
        
    def process_keystroke(self):
        if self.model.head.direction != Direction.UP and self.key_events[pygame.K_DOWN]:
            self.model.head.direction = Direction.DOWN
            
        elif self.model.head.direction != Direction.DOWN and self.key_events[pygame.K_UP]:
            self.model.head.direction = Direction.UP
            
        elif self.model.head.direction != Direction.RIGHT and self.key_events[pygame.K_LEFT]:
            self.model.head.direction = Direction.LEFT
            
        elif self.model.head.direction != Direction.LEFT and self.key_events[pygame.K_RIGHT]:
            self.model.head.direction = Direction.RIGHT
            
        if self.key_events[pygame.K_q]:
            self.run = False
        
    def redefine_game_window(self):
        '''
        Drawing method.
        '''
        self.win.fill((24,24,24))

        self.draw_body()
        self.draw_food()
        self.draw_head()
                    
        scoretext=self.my_font.render('Score: ' + str(self.model.score),1,(100,100,100))
        self.win.blit(scoretext,(20,20))
        pygame.display.update()
        
        if self.model.game_state == GameState.GAME_OVER:
            
            
        
    def draw_head(self):
        pygame.draw.rect(self.win, (57,255,20), (self.model.head.x_poz * 5, self.model.head.y_poz * 5, 5, 5))

    def draw_body(self):
        for body in self.model.body:
            pygame.draw.rect(self.win, (255,131,0), (body.x_poz * 5, body.y_poz * 5, 5, 5))
            
    def draw_food(self):
        pygame.draw.rect(self.win, (21,244,238), (self.model.food.x_poz * 5, self.model.food.y_poz * 5, 5, 5))


    