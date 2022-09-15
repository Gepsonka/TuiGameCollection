from tkinter import Button
from turtle import color, title, width
import pytermgui as ptg


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
        
        
        self.build_window()
        
    def build_window(self):
        with ptg.WindowManager() as self.manager:
            self.header = ptg.Window(
                '[bold 200]Game Collection',
                width=100,
            )
            self.header.is_noresize = True
            
            self.snake_pixel_matrix = ptg.DensePixelMatrix.from_matrix(SNAKE_MATRIX)
            
            self.snake_btn = ptg.Button(
                label="[bold italic 255]Snake"
            )
            
            self.box_pixel_matrix = ptg.DensePixelMatrix.from_matrix(BOX_MATRIX)
            
            self.box_btn = ptg.Button(
                label="[bold italic 255]Box"
            )
                        
            self.body = ptg.Window(
                (
                    ptg.Container(
                        self.snake_pixel_matrix,
                        self.snake_btn,
                    ),
                    ptg.Container(
                        self.box_pixel_matrix,
                        self.box_btn,
                    )
                ),
                title="[255]Games"
            )
            self.body.is_noresize = True
            
            self.leader_board_btn = ptg.Button(
                label='[230]Leaderboard',
            )
            
            self.menu_body = ptg.Window(
                self.header,
                self.body,
                self.leader_board_btn,
                width=100,
            ).center()
            self.menu_body.is_noresize = True
            
            self.manager.add(self.menu_body)