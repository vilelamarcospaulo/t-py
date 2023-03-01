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

    def on(self, event_key, fn):
        self.execution_map[event_key] = fn
        return self

    def reset(self):
        self.execution_map.clear()
