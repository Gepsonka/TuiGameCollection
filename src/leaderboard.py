import sqlite3
from this import d



class Leaderboard:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('../.game_collection/game_data.db')
        self.cur = self.conn.cursor()
        
    