import sqlite3
import os



def main():
    # Will contain scoreboard and basic config files
    if not ".game_collection" in os.listdir():
        os.mkdir(".game_collection")
        open(".game_collection/.gitignore", 'a').close()
        conn = sqlite3.connect(".game_collection/game_data.db")
        conn.close()
        
    
    
    
if __name__=="__main__":
    main()