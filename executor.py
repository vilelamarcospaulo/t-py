from AppKit import NSApplication, NSApp, NSObject
from Cocoa import NSEvent, NSScrollWheelMask, NSOtherMouseDownMask
from Foundation import NSBundle
from PyObjCTools import AppHelper

from actions.lootbox import LootBox
from handlers.mouse_handler import MouseHandler
from listeners.mouse_click_event_listener import MouseClickEventListener

CHARACTER_POSITION = (2671, 545)
PIXEL_OFFSET = (60, 60)

BUTTON_WHELL = 2
BUTTON_LEFT_FIRE = 4

mouseHandler = MouseHandler('right')
lootBox = LootBox(CHARACTER_POSITION, PIXEL_OFFSET, mouseHandler)

eventHandler = MouseButtonEventHandler()
eventHandler.on(BUTTON_WHELL, lambda event : print(mouseHandler.current_position()))
eventHandler.on(BUTTON_LEFT_FIRE, lambda event : lootBox.exec())

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(NSOtherMouseDownMask, eventHandler.trigger_event)
        print('FaskPick :: RUNNING', self)

if __name__ == '__main__':
    app = NSApplication.sharedApplication()
    
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)

    AppHelper.runEventLoop()