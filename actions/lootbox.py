import time
import random

class LootBox:
    def __init__(self, charScreenPosition, offSet, mouseHandler):
        self.charX, self.charY = charScreenPosition
        self.offsetX, self.offsetY = offSet
        self.mouseHandler = mouseHandler

    def set_position(self, charScreenPosition):
        self.charX, self.charY = charScreenPosition

    def exec(self):
        positions = self._calc_box_positions()
        random.shuffle(positions)
        
        for pos in positions:
            self.mouseHandler.click(pos)
            rand_delay = random.uniform(0.09, 0.12)
            time.sleep(rand_delay)
        
    def _calc_box_positions(self): 
        return [
            (self.charX, self.charY),                               ## CENTER
            (self.charX + self.offsetX, self.charY),                ## EAST
            (self.charX + self.offsetX, self.charY + self.offsetY), ## SOUTH-EAST 
            (self.charX, self.charY + self.offsetY),                ## SOUTH
            (self.charX - self.offsetX, self.charY + self.offsetY), ## SOUTH-WEST
            (self.charX - self.offsetX, self.charY),                ## WEST
            (self.charX - self.offsetX, self.charY - self.offsetY), ## NORTH-WEST
            (self.charX, self.charY - self.offsetY),                ## NORTH
            (self.charX + self.offsetX, self.charY - self.offsetY), ## NORTH-EAST
        ]