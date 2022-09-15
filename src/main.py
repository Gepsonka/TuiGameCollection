import sqlite3
import os
from turtle import width
import pytermgui as ptg

CONFIG = """
            config:
                InputField:
                    styles:
                        prompt: dim italic
                        cursor: '@72'
                Label:
                    styles:
                        value: dim bold

                Window:
                    styles:
                        border: '60'
                        corner: '60'

                Container:
                    styles:
                        border: '96'
                        corner: '96'
            """


def main():
    # Will contain scoreboard and basic config files
    if not ".game_collection" in os.listdir():
        os.mkdir(".game_collection")
        open(".game_collection/.gitignore", 'a').close()
        conn = sqlite3.connect(".game_collection/game_data.db")
        conn.close()
        
        

    with ptg.YamlLoader() as loader:
        loader.load(CONFIG)
        
    with ptg.WindowManager() as manager:
        window = (
            ptg.Window(
                '',
                ptg.InputField("Brotond", prompt="Name:"),
                ptg.Container(
                    "Additional notes:",
                    ptg.InputField(
                        "A whole bunch of nggrs",
                        multiline=True
                    ),
                    ptg.PixelMatrix(20,20, default='white'),
                    box="EMPTY_VERTICAL",
                ),
                ptg.WindowManager.alert(
                    ptg.InputField(
                        "",
                        prompt="Pick a nickname: "
                    ),
                    ptg.Button(
                        label="Ok",
                        onclick= lambda 
                    )
                ),
                
                "",
                ["Submit", lambda *_: submit(manager, window)],
                width=70,
                box="DOUBLE"
            )
            .set_title("Love U").center()
        )
        
        manager.add(window)
        
    
if __name__=="__main__":
    main()