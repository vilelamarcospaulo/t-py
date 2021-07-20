from .event_listener import EventListener

class MouseClickEventListener(EventListener):
    def event_decode(self, event):
        return event.buttonNumber()