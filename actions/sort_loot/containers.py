import cv2
import numpy as np
from computer_vision.image_text_position import ImageTextPosition

LOOT_BAG = 'shopping bag'
RASHID = 'red backpack'
GREEN_DJIN = 'green backpa'
BLUE_DJIN = 'blue backpack'
ESRIK = 'expedition backpack'
EDRON = 'brocade backpack'

# TODO :: MAKE AUTO DECTION BASED ON SCREEN_SHOT
# RIGHT NOW IT'S FAILING TO DETECT TEXTS


def find_containers(image, container_names):
    container_positions = {}

    container_positions[LOOT_BAG] = (1885, 91)
    container_positions[RASHID] = (1886, 185)
    container_positions[GREEN_DJIN] = (1887, 287)
    container_positions[BLUE_DJIN] = (1886, 384)
    container_positions[ESRIK] = (1884, 491)
    container_positions[EDRON] = (1884, 596)

    return container_positions
