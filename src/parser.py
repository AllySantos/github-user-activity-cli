from pyexpat.errors import messages

from api import API
from event import Event
from type import Type

class EventParser:

    def __init__(self):
        self.types = self.load_types()

    @staticmethod
    def load_types():
        push  = Type('PushEvent', 'Pushed')
        watch = Type('WatchEvent', 'Watched')
        fork = Type('ForkEvent', 'Forked')
        create = Type('CreateEvent', 'Created')

        return [push, watch, fork, create]

    def get_type(self, api_name):
        type = next((t for t in self.types if t._api_name == api_name))
        return type

    def parse_events(self, api_response):
        events = []
        for event in api_response:
            try:
                type = self.get_type(event['type'])
                message = ''
                match type._api_name:
                    case 'PushEvent':
                        repo = event['repo']['name']
                        commits = len(event['payload']['commits']) if 'commits' in event['payload'] else 0
                        message = f'{commits} commit(s) to {repo}'

                obj_event = Event(type, message)
                events.append(obj_event)
            except:
                print(event)
        return events




