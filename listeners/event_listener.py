class EventListener:
    def __init__(self): 
        self.execution_map = {}

    def trigger(self, event):
        try:
            event_key = self.event_decode(event)
            execute_fn = self.execution_map.get(event_key)

            if not execute_fn:
                return print(f'Not registred event for {event_key}')
            
            execute_fn(event)

        except Exception as e:
            print(e)

    def on(self, button_number, fn):
        self.execution_map[button_number] = fn
        return self