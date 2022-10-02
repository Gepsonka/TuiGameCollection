import unittest
import sqlite3
from src.database import Database
import os


class TestLeaderboard(unittest.TestCase):
    
    def setUp(self) -> None:
        self.conn = sqlite3.connect(".game_collection/game_data_test.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS Leaderboard (
                id INTEGER primary key autoincrement,
                nickname VARCHAR(16) NOT NULL,
                game_type VARCAHR(20) NOT NULL,
                score INTEGER NOT NULL DEFAULT 0,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            '''
        )
        
        self.cursor.execute('''
                            INSERT INTO Leaderboard (nickname, game_type, score)
                            VALUES ('pista98', 'snake', 12)
                            ''')
        self.cursor.execute('''
                            INSERT INTO Leaderboard (nickname, game_type, score)
                            VALUES ('gepsonka', 'box', 120)
                            ''')
        self.cursor.execute('''
                            INSERT INTO Leaderboard (nickname, game_type, score)
                            VALUES ('sqookie', 'snake', 200)
                            ''')
        self.cursor.execute('''
                            INSERT INTO Leaderboard (nickname, game_type, score)
                            VALUES ('pista98', 'box', 32)
                            ''')
        
        self.conn.commit()
        
        self.db = Database(".game_collection/game_data_test.db")
        
        
    def tearDown(self) -> None:
        self.conn.close()
        os.remove(".game_collection/game_data_test.db")
        
    def test_query_snake(self):
        result = list(self.db.query_snake_top(10))
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0].score, 200)
        self.assertAlmostEqual(result[0].nickname, 'sqookie')
        
    def test_query_box(self):
        result = list(self.db.query_box_top(10))
        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0].score, 120)
        self.assertAlmostEqual(result[0].nickname, 'gepsonka')
        
    def test_add_new_score(self):
        self.db.add_new_result('csoki', 'snake', 123)
        query_back = self.cursor.execute('''
                                         select * from Leaderboard
                                         where nickname = \'csoki\' and game_type = \'snake\' and score = 23
                                         ''')
                
        for row in query_back:
            self.assertEqual(row[0], 'csoki')
            self.assertEqual(row[1], 'snake')
            self.assertEqual(row[2], 123)
            break
        
        
            
        
        
        
        
        
# if __name__=="__main__":
#     unittest.main()