class UserNotFound(Exception):

    def __init__(self, username):
        self.message = f"{username} don't exist on GitHub"
        super().__init__(self.message)

class ResponseEmpty(Exception):
    def __init__(self):
        self.message = "API hasn't return any event"
        super().__init__(self.message)

class EventNotRegistered(Exception):
    def __init__(self, event_name):
        self.message = f"The event {event_name} isn't registered"
        super().__init__(self.message)