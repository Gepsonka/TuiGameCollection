from ctypes.wintypes import tagMSG
import time
from turtle import title
import pytermgui as ptg
from pytermgui.window_manager.manager import WindowManager
from database import Database
from time import sleep
import multiprocessing
from game_views.snake_view import SnakeGame


SNAKE_MATRIX = [
    ['black', 'black', 'black', 'black', 'black', 'white', 'white', 'black', 'black', 'black',],
    ['black', 'black', 'black', 'black', 'white', 'black', 'black', 'white', 'black', 'black',],
    ['white', 'white', 'white', 'white', 'black', 'black', 'black', 'black', 'white', 'black',],
    ['black', 'black', 'black', 'black', 'black', 'white', 'black', 'black', 'black', 'white',],
    ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'white', 'white', 'white',],
    ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'white', 'white', 'white',],
    ['black', 'black', 'black', 'black', 'black', 'white', 'black', 'black', 'black', 'white',],
    ['white', 'white', 'white', 'white', 'black', 'black', 'black', 'black', 'white', 'black',],
    ['black', 'black', 'black', 'black', 'white', 'black', 'black', 'white', 'black', 'black',],
    ['black', 'black', 'black', 'black', 'black', 'white', 'white', 'black', 'black', 'black',],
]


BOX_MATRIX = [
    ['black', 'lightblue', 'lightblue', 'black', 'lightblue', 'lightblue', 'black', 'lightblue', 'lightblue', 'black',],
    ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',],
    ['black', 'white', 'white', 'black', 'white', 'white', 'black', 'white', 'white', 'black',],
    ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',],
    ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',],
    ['black', 'black', 'black', 'black', 'black', 'green', 'black', 'black', 'black', 'black',],
    ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',],
    ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',],
    ['black', 'white', 'white', 'white', 'black', 'black', 'black', 'black', 'black', 'black',],
    ['black', 'white', 'white', 'white', 'black', 'black', 'black', 'black', 'black', 'black',],
]


class MainMenu:
    def __init__(self) -> None:
        self.config_manager = ptg.YamlLoader()
        self.manager = ptg.WindowManager()
        self.build_window()
        self.db = Database('.game_collection/game_data.db')
        self.manager.run()
        
    def build_window(self):
            self.header = ptg.Window(
                '[bold 200]Game Collection',
                width=100,
            )   
            self.header.is_noresize = True
            
            self.snake_pixel_matrix = ptg.DensePixelMatrix.from_matrix(SNAKE_MATRIX)
            
            self.snake_btn = ptg.Button(
                label="[bold italic 255]Snake",
                onclick= lambda *_: self.start_snake_game()
            )
            
            self.box_pixel_matrix = ptg.DensePixelMatrix.from_matrix(BOX_MATRIX)
            
            self.box_btn = ptg.Button(
                label="[bold italic 255]Box"
            )
            
            self.snake_container = ptg.Container(
                        self.snake_pixel_matrix,
                        self.snake_btn,
                    )
            
            self.box_container = ptg.Container(
                        self.box_pixel_matrix,
                        self.box_btn,
                    )
                        
            self.body = ptg.Window(
                (
                    self.snake_container,
                    self.box_container
                ),
                title="[255]Games"
            )
            self.body.is_noresize = True
            
            self.leader_board_btn = ptg.Button(
                label='[230]Leaderboard',
                onclick=lambda *_: self.show_leaderboard(self.manager)
            )
            
            self.menu_body = ptg.Window(
                self.header,
                self.body,
                self.leader_board_btn,
                width=100,
            ).center()
            self.menu_body.is_noresize = True
            
            self.manager.add(self.menu_body) 
                                    
    def show_leaderboard(self, manager):
        self.leaderboard = ptg.Window(
            (
                ptg.Window(
                    (
                        ptg.Window(
                            *[str(x.nickname) for x in Database('.game_collection/game_data.db').query_snake_top(10)],
                            width=20,
                            title='Nickname'
                            
                        ),
                        ptg.Window(
                            *[str(x.score) for x in Database('.game_collection/game_data.db').query_snake_top(10)],
                            width=4,
                            title='Score'
                        ),
                    ),
                    title='[120]Snake'
                ),
                
                ptg.Window(
                    (
                        ptg.Window(
                            *[str(x.nickname) for x in Database('.game_collection/game_data.db').query_box_top(10)],
                            width=20,
                            title='Nickname'
                        ),
                        ptg.Container(
                            *[str(x.score) for x in Database('.game_collection/game_data.db').query_box_top(10)],
                            width=4,
                            title='Score'
                        ),
                    ),
                    title='[80]Box'
                ),
            ),
            ptg.Button(
                label='Close',
                onclick=lambda *_: self.leaderboard.close()
            ),
            
            title='[50]Leaderboard',
            width=150
        ).center()
        
        manager.add(self.leaderboard)
        
    def start_snake_game(self):
        self.game = SnakeGame()
        self.game.main_loop()
        
        
