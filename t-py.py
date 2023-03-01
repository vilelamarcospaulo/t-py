import rumps

from Cocoa import NSEvent, NSOtherMouseDownMask
from executor import EventExecutor


class TPyStatusBarApp(rumps.App):
    def __init__(self):
        super(TPyStatusBarApp, self).__init__("T-Py")
        self.menu = ["Lootbox", "Loot Sort"]
        self.executor = EventExecutor()
        self.registered = False

    @rumps.clicked("Lootbox")
    def lootbox_mode(self, _):
        self._register_event_listener()
        self.executor.to_loot_box()

    @rumps.clicked("Loot Sort")
    def loot_sort_mode(self, _):
        self._register_event_listener()
        self.executor.to_loot_sort()

    def _register_event_listener(self):
        if self.registered:
            return

        self.registered = True
        NSEvent.addGlobalMonitorForEventsMatchingMask_handler_(
            NSOtherMouseDownMask, self.executor.process)


if __name__ == "__main__":
    TPyStatusBarApp().run()
