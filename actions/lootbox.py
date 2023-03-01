import time
import random


class LootBox:
    def __init__(self, offSet, mouse_handler, charScreenPosition=(0, 0)):
        self.charX, self.charY = charScreenPosition
        self.offsetX, self.offsetY = offSet
        self.mouse_handler = mouse_handler

    def set_position(self, char_screen_position=None):
        if char_screen_position is None:
            self.set_position(self.mouse_handler.current_position())

        self.charX, self.charY = char_screen_position

    def exec(self):
        positions = self._calc_box_positions()
        random.shuffle(positions)

        for pos in positions:
            self.mouse_handler.click(pos)

            # PREVENT "PERFECT" MOUSE MOVEMENT
            rand_delay = random.uniform(0.09, 0.12)
            time.sleep(rand_delay)

    def _calc_box_positions(self):
        return [
            (self.charX, self.charY),  # CENTER
            (self.charX + self.offsetX, self.charY),  # EAST
            (self.charX + self.offsetX, self.charY + self.offsetY),  # SOUTH-EAST
            (self.charX, self.charY + self.offsetY),  # SOUTH
            (self.charX - self.offsetX, self.charY + self.offsetY),  # SOUTH-WEST
            (self.charX - self.offsetX, self.charY),  # WEST
            (self.charX - self.offsetX, self.charY - self.offsetY),  # NORTH-WEST
            (self.charX, self.charY - self.offsetY),  # NORTH
            (self.charX + self.offsetX, self.charY - self.offsetY),  # NORTH-EAST
        ]
