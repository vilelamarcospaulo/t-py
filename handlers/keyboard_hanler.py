import time
from Quartz import CGEventPost, CGEventCreateKeyboardEvent, kCGHIDEventTap

class KeyboardHandler:
    def __init__(self):
        self._keyboard_map = {
            'shift': 0x00
        }
        
    def press(self, key):
        key = self._keyboard_map[key]
        
        event = CGEventCreateKeyboardEvent(None, 0x38, True)
        CGEventPost(kCGHIDEventTap, event)
        time.sleep(0.1)

    def release(self, key):
        key = self._keyboard_map[key]
        
        event = CGEventCreateKeyboardEvent(None, 0x38, False)
        CGEventPost(kCGHIDEventTap, event)
        time.sleep(0.1)