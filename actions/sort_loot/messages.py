import re
import cv2
from computer_vision.image_text_position import ImageTextPosition, TextMatcher

def show(img):
  cv2.imshow("Image", img)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def messages(image, possible_names):
  bottom_bar_height = 50
  messages_panel_height = 110

  messages_height = messages_panel_height + bottom_bar_height

  hImg, wImg = image.shape

  cropY = hImg - messages_height
  cropX = 0
  
  cropped = image[cropY:cropY + messages_height, cropX:cropX + wImg].copy()
  
  image_reader = ImageTextPosition()
  image_reader.process_image(cropped)

  result = []
  text_matcher = TextMatcher(possible_names)

  for text, _ in image_reader.flush():
    matches = re.search(r"You see (a|an) (((?!that|\()([a-zA-Z]+)| )*)", text)
    print(f'regex fail {text}')
    if matches is None: 
      continue

    text = matches.groups()[2]
    item_name = text_matcher.check_text(text)
    print(f'register item fail {text}')
    if item_name is None:
        continue

    result.append(item_name)
  
  return result