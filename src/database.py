from __future__ import generators
from datetime import date
import sqlite3
from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class PersonalScore:
    id: int
    nickname: str
    game: str
    score: int
    createdAt: datetime
    
    def __init__(self, id, nickname, game, score, created_at) -> None:
        self.id = id
        self.nickname = nickname
        self.game = game
        self.score = score
        self.createdAt = created_at

class Database:
    def __init__(self, db_path) -> None:
        self.conn = sqlite3.connect(db_path) # .game_collection/game_data.db
        self.cur = self.conn.cursor()
        
    def add_new_result(self, nickname: str, game: str, score: int) -> None:
        self.cur.execute(f'''
                         INSERT INTO Leaderboard (nickname, game_type, score)
                         VALUES (\'{nickname}\', \'{game}\', {score})
                         ''')
        
        self.conn.commit()
        
    def query_snake_top(self, top: int):
        result = self.cur.execute(f'''
                                  SELECT * from Leaderboard
                                  WHERE game_type='snake'
                                  ORDER BY score DESC
                                  LIMIT {top}
                                  ''')
        
        for row in result:
            yield PersonalScore(row[0], row[1], row[2], row[3], row[4])
            
    def query_box_top(self, top: int):
        result = self.cur.execute(f'''
                                  SELECT * from Leaderboard
                                  WHERE game_type='box'
                                  ORDER BY score DESC
                                  LIMIT {top}
                                  ''')
        
        for row in result:
            yield PersonalScore(row[0], row[1], row[2], row[3], row[4])
        
    def query_leaderboard(self, game: str, top: int):
        result = self.cur.execute(f'''
                                  SELECT * from Leaderboard
                                  WHERE game_type='{game}'
                                  ORDER BY score DESC
                                  LIMIT {top}
                                  ''')
        
        for row in result:
            yield PersonalScore(row[0], row[1], row[2], row[3], row[4])
            
            
    