from AppKit import NSEvent
from Quartz import CGEventPost, CGEventCreateMouseEvent, CGDisplayPixelsHigh, kCGHIDEventTap, kCGEventMouseMoved, kCGEventLeftMouseDown, kCGEventLeftMouseUp, kCGEventRightMouseDown, kCGEventRightMouseUp

class MouseHandler:
    def __init__(self, button):
        self.button = self._button(button)
        
    def click(self, position):
        self._move(position)
        self._press(position)
        self._release(position)

    def current_position(self):
        pos = NSEvent.mouseLocation()
        return (int(pos.x), int(CGDisplayPixelsHigh(0) - pos.y))

    def _button(self, button):
        if button == 'left':
            return 0
        elif button == 'right':
            return 1

        raise Exception('invalid mouse button')

    def _button_event_order(self):
        if self.button == 0:
            return [kCGEventLeftMouseDown, kCGEventLeftMouseUp]
        else:
            return [kCGEventRightMouseDown, kCGEventRightMouseUp]
        
    def _move(self, position):
        move = CGEventCreateMouseEvent(None, kCGEventMouseMoved, position, 0)
        CGEventPost(kCGHIDEventTap, move)

    def _press(self, position):
        event = CGEventCreateMouseEvent(None, self._button_event_order()[0], position, self.button)
        CGEventPost(kCGHIDEventTap, event)
        
    def _release(self, position):
        event = CGEventCreateMouseEvent(None, self._button_event_order()[1], position, self.button)
        CGEventPost(kCGHIDEventTap, event)