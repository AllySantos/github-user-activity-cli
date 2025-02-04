from api import API
from parser import EventParser


class CLI:

    username = None
    @classmethod
    def set_username(cls, username):
        cls.username = username

    @staticmethod
    def main(filter = None):

        parser = EventParser()
        api = API()
        response = api.fetch_events(CLI.username)

        list_events = parser.parse_events(response, filter)

        print('Output:', *list_events, sep="\n")



if __name__ == '__main__':
    username = 'allysantos'
    CLI.set_username(username)

    CLI.main()
