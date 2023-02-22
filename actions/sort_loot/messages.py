import re
import cv2
from computer_vision.image_text_position import ImageTextPosition

def show(img):
  cv2.imshow("Image", img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def messages(image):
  bottom_bar_height = 50
  messages_panel_height = 100

  messages_height = messages_panel_height + bottom_bar_height

  hImg, wImg = image.shape

  cropY = hImg - messages_height
  cropX = 0
  
  cropped = image[cropY:cropY + messages_height, cropX:cropX + wImg].copy()
  
  image_reader = ImageTextPosition()
  image_reader.process_image(cropped)

  result = []
  for text, _ in image_reader.flush():
    
    matches = re.search(r".* You see (a )?([a-z A-Z]*)( \(.*)?.?", text)
    if matches is None: 
      continue

    item_name = matches.groups()[1]
    result.append(item_name)
  
  return result