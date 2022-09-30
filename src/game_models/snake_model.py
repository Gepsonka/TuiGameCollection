from enum import Enum
from re import I
import keyboard

class State(Enum):
    EMPTY = 0
    HEAD = 1
    BODY = 2
    FOOD = 3

map = [[State.EMPTY for j in range(100)] for i in range(100)]
keys = keyboard.parse_hotkey('up')

class Snake:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.snakebody = [[State.HEAD for i in range(0, 1)],[State.BODY for j in range(0, size)]]
        Ymax = len(map) / 2
        Xmax = len(map) / 2
        self.head_position = [Ymax, Xmax]

    def movement(self):
        while True:
            keyboard.wait('right')
            if keyboard.is_pressed('up'):
                self.head_position[1] += 1
                print("Head position", self.head_position)
            elif keyboard.is_pressed('down'):
                self.head_position[1] -= 1
                print("Head position", self.head_position)
            elif keyboard.is_pressed('left'):
                self.head_position[0] -= 1
                print("Head position", self.head_position)
            elif keyboard.is_pressed('right'):
                self.head_position[0] += 1
                print("Head position", self.head_position)
            elif keyboard.is_pressed('esc'):
                break

    def eatsFood(self):
        for i in map:
            for j in i:
                if map[i][j] == State.FOOD and self.head_position == map[i][j]:
                    self.size +=1
        return self.size

    def eatsSelf(self):
        if self.snakebody == self.head_position:
            return 0, print("Játék vége")

    def update(self):
        self.movement()


def main():
   snek = Snake("joe", 1)
   print(snek.head_position)
   snek.update()

if __name__ == "__main__":
    main()