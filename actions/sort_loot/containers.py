from computer_vision.image_text_position import ImageTextPosition

def find_containers(image, container_names):
  panels = 2
  panel_width = 175
  off_set = 25
  container_fixed_x = 22
  hImg, wImg = image.shape

  containers = { }
  for index in range(1, panels + 1):
    cropY = 0
    cropX = wImg - (panel_width * index)
    
    cropped = image[cropY:cropY + hImg, cropX:cropX + panel_width].copy()

    image_reader = ImageTextPosition()
    image_reader.process_image(cropped)

    result = image_reader.detect_text_position(container_names)

    for text, loc in result:
      x, y, width, heigh = loc
      click_point = (container_fixed_x + cropX, y + cropY + off_set)
      containers[text] = click_point

  return containers
      