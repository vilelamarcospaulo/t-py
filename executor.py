
from actions.lootbox import LootBox
from actions.sort_loot.sort_loot import SortLoot
from handlers.mouse_handler import MouseHandler
from listeners.mouse_click_event_listener import MouseClickEventListener

PIXEL_OFFSET = (60, 60)

BUTTON_WHEEL = 2
BUTTON_ACTION = 4


class EventExecutor():
    def __init__(self) -> None:
        self.right_click_handler = MouseHandler('right')
        self.sort_loot = SortLoot()
        self.loot_box = LootBox(PIXEL_OFFSET, self.right_click_handler)

        self.eventHandler = MouseClickEventListener()

    def to_loot_box(self):
        self.eventHandler.reset()
        self.eventHandler.on(
            BUTTON_WHEEL, lambda event: self.loot_box.set_position())

        self.eventHandler.on(
            BUTTON_ACTION, lambda event: self.loot_box.exec())

    def to_loot_sort(self):
        self.sort_loot.reset()
        self.eventHandler.reset()
        self.eventHandler.on(
            BUTTON_WHEEL, lambda event: self.sort_loot.run())
        self.eventHandler.on(
            BUTTON_ACTION, lambda event: print(self.right_click_handler.current_position()))

    def process(self, event):
        self.eventHandler.trigger(event)
