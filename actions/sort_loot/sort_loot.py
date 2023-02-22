import time
from actions.sort_loot.messages import messages
from actions.sort_loot.containers import find_containers
from computer_vision.image_text_position import ImageTextPosition
from computer_vision.screen_capture import ScreenCapture
from handlers.keyboard_hanler import KeyboardHandler
from handlers.mouse_handler import MouseHandler

LOOT_BAG = 'shopping bag'
RASHID = 'red backpack'
GREEN_DJIN = 'green backpa'
BLUE_DJIN = 'blue backpack'

class SortLoot:
  def __init__(self) -> None:
    self.screen_capture = ScreenCapture()
    self.mouse_handler = MouseHandler('left')
    self.keyboard_handler = KeyboardHandler()

  def run(self, screen_image):
    screen_image = self.screen_capture.capture()
    container_positions = find_containers(screen_image, [
      LOOT_BAG, RASHID, GREEN_DJIN, BLUE_DJIN,
    ])

    loot_bag = container_positions.get(LOOT_BAG)
    if loot_bag is None:
      return print('check if loot bag is opened')

    self._look_item(loot_bag)
    
    screen_image = self.screen_capture.capture()
    item_name = messages(screen_image)[-1]
    item_destination = sort_items.get(item_name)

    if item_destination is None:
        print(f'not configured to item {item_name}')
        return

    item_destination_pos = container_positions.get(item_destination)
    if item_destination_pos is None:
      return print(f'unable to detect {item_destination}')

    self.mouse_handler.drag(item_destination_pos)

  def _look_item(self, position): 
    self.keyboard_handler.press('shift')
    self.mouse_handler.click(position)
    self.keyboard_handler.release('shift')

## TODO :: Extract to a .dat file
sort_items = {}
sort_items['warrior helmet'] = GREEN_DJIN
sort_items['ruby necklace'] = RASHID