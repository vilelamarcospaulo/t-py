from AppKit import NSApplication, NSApp, NSObject
from Cocoa import NSEvent, NSScrollWheelMask, NSOtherMouseDownMask
from Foundation import NSBundle
from PyObjCTools import AppHelper

from actions.lootbox import LootBox
from actions.sort_loot.sort_loot import SortLoot
from handlers.mouse_handler import MouseHandler
from listeners.mouse_click_event_listener import MouseClickEventListener

CHARACTER_POSITION = (2671, 545)
PIXEL_OFFSET = (60, 60)

BUTTON_WHELL = 2
BUTTON_SORT_LOOT = 5
BUTTON_LEFT_FIRE = 4

mouseHandler = MouseHandler('right')
lootBox = LootBox(CHARACTER_POSITION, PIXEL_OFFSET, mouseHandler)

sort_loot = SortLoot()

eventHandler = MouseClickEventListener()
eventHandler.on(BUTTON_WHELL, lambda event : lootBox.set_position(mouseHandler.current_position()))
eventHandler.on(BUTTON_LEFT_FIRE, lambda event : lootBox.exec())
eventHandler.on(BUTTON_SORT_LOOT, lambda event : sort_loot.run())

class AppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, notification):
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(NSOtherMouseDownMask, eventHandler.trigger)
        print('LootBox :: RUNNING')

if __name__ == '__main__':
    app = NSApplication.sharedApplication()
    
    delegate = AppDelegate.alloc().init()
    NSApp().setDelegate_(delegate)

    AppHelper.runEventLoop()