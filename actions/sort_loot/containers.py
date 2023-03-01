import cv2
import numpy as np
from computer_vision.image_text_position import ImageTextPosition

LOOT_BAG = 'shopping bag'
RASHID = 'red backpack'
GREEN_DJIN = 'green backpa'
BLUE_DJIN = 'blue backpack'

# TODO :: MAKE AUTO DECTION BASED ON SCREEN_SHOT
# RIGHT NOW IT'S FAILING TO DETECT TEXTS


def find_containers(image, container_names):
    container_positions = {}

    container_positions[LOOT_BAG] = (1884, 94)
    container_positions[RASHID] = (1882, 305)
    container_positions[GREEN_DJIN] = (1884, 515)
    container_positions[BLUE_DJIN] = (1888, 730)

    return container_positions
