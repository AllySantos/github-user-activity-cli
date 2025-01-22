from api import API
from parser import EventParser

class CLI:

    @staticmethod
    def main():

        parser = EventParser()
        api = API()
        response = api.fetch_events()

        list_events = parser.parse_events(response)

        for event in list_events:
            print(event.parse())


if __name__ == '__main__':
    CLI.main()
