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
    self._containers = None

  def run(self, screen_image = None):
    self._load_containers()
    self._look_item(self._containers.get(LOOT_BAG))
    
    screen_image = self.screen_capture.capture()
    item_name = messages(screen_image)[-1]
    item_destination = sort_items.get(item_name.strip())

    if item_destination is None:
        print(f'not configured to item {item_name}')
        return

    item_destination_pos = self._containers.get(item_destination)
    if item_destination_pos is None:
      return print(f'unable to detect {item_destination}')

    print(f'moving {item_name} to {item_destination}')
    self.mouse_handler.drag(item_destination_pos)

  def _load_containers(self):
    if not self._containers is None:
      return

    screen_image = self.screen_capture.capture()
    container_positions = find_containers(screen_image, [
      LOOT_BAG, RASHID, GREEN_DJIN, BLUE_DJIN,
    ])
    
    if len(container_positions.keys()) != 4:
      raise Exception('unable to check all containers')

    self._containers = container_positions


  def _look_item(self, position): 
    self.keyboard_handler.press('shift')
    self.mouse_handler.click(position)
    self.keyboard_handler.release('shift')

## TODO :: Extract to a .dat file
sort_items = {}
sort_items['ruby necklace'] = RASHID
sort_items['spiked squelcher'] = RASHID
sort_items['assassin dagger'] = RASHID
sort_items['oriental shoes'] = RASHID
sort_items['skullcracker armor'] = RASHID
sort_items['knight legs'] = RASHID
sort_items['shockwave amulet'] = RASHID
sort_items['glacier amulet'] = RASHID
sort_items['lightning pendant'] = RASHID
sort_items['terra mantle'] = RASHID
sort_items['terra amulet'] = RASHID

sort_items['warrior helmet'] = GREEN_DJIN

sort_items['blue robe'] = BLUE_DJIN
sort_items['ice rapier'] = BLUE_DJIN
sort_items['wand of voodoo'] = BLUE_DJIN
sort_items['glorious axe'] = BLUE_DJIN
sort_items['wand of starstorm'] = BLUE_DJIN
sort_items['terra rod'] = BLUE_DJIN