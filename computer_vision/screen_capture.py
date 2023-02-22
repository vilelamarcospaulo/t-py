import numpy as np
import cv2
from PIL import ImageGrab

class ScreenCapture():
  def capture(self):
    img = ImageGrab.grab()
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    ret, frame = cv2.threshold(frame, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    return frame