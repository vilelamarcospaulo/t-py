import cv2
import numpy as np
from computer_vision.image_text_position import ImageTextPosition

def find_containers(image, container_names):
  panels = 2
  panel_width = 175
  panel_start = 500
  off_set = 25
  container_fixed_x = 22
  hImg, wImg = image.shape

  cv2.imwrite(f'f.png', image)

  containers = { }
  for index in range(1, panels + 1):
    line = 0
    line_height = 30

    while True:
      cropY = panel_start + (line * line_height)
      if cropY > hImg:
        break

      cropX = wImg - (panel_width * index)
    
      cropped = image[cropY:cropY + line_height, cropX:cropX + panel_width].copy()
  
      image_reader = ImageTextPosition()
      image_reader.process_image(cropped)

      result = image_reader.detect_text_position(container_names)

      for text, loc in result:
        x, y, width, heigh = loc

        click_point = (container_fixed_x + cropX, y + cropY + off_set)
        containers[text] = click_point
      
      line += 1
  
  return containers
      