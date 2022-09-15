import sqlite3
import os
from turtle import color, width
import pytermgui as ptg
from main_menu import MainMenu


global playerName

def init_env():
    # Will contain scoreboard and basic config files
    if not ".game_collection" in os.listdir():
        os.mkdir(".game_collection")
        open(".game_collection/.gitignore", 'a').close()
        conn = sqlite3.connect(".game_collection/game_data.db")
        cursor = conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS Leaderboard (
                id INTEGER primary key autoincrement,
                game_type VARCAHR(20) NOT NULL,
                score INTEGER NOT NULL DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            );
            '''
        )
        conn.close()
        
        
        
if __name__=="__main__":
    init_env()
    mm = MainMenu()
    
    