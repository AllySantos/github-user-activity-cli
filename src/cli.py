import argparse

from api import API
from parser import EventParser

class CLI:

    def __init__(self):
        self.args = self.parse_arguments()

    @staticmethod
    def parse_arguments():
        parser = argparse.ArgumentParser(
            prog='GitHub CLI',
            description='Get activities'
        )

        parser.add_argument('username')
        parser.add_argument('filter', nargs='?',default=None)

        args = parser.parse_args()

        return args


class Main():

    @staticmethod
    def execute():
        cli = CLI()
        parser = EventParser()
        api = API()

        args = cli.args

        username = args.username
        filter = args.filter

        try:
            response = api.fetch_events(username)
            list_events = parser.parse_events(response, filter)
            print('Output:', *list_events, sep="\n")
        except Exception as e:
            print(f'Error: [{type(e).__name__}] {e}')



if __name__ == '__main__':
    main = Main()
    main.execute()
