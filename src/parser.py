from pyexpat.errors import messages

from api import API
from event import Event
from type import Type
from exception import ResponseEmpty

class EventParser:

    def __init__(self):
        self.types = self.load_types()

    @staticmethod
    def load_types():
        push  = Type('PushEvent', 'Pushed')
        issues = Type('IssuesEvent', 'Worked on issue')
        issue_comment = Type('IssueCommentEvent', 'Commented on issue')
        release = Type('ReleaseEvent', 'Created a release ')
        watch = Type('WatchEvent', 'Watched')
        fork = Type('ForkEvent', 'Forked')
        create = Type('CreateEvent', 'Created')
        pull_request = Type('PullRequestEvent', 'Created pull request')

        return [push, create, pull_request, issues, issue_comment, release]

    def get_type(self, api_name):
        type = next((t for t in self.types if t._api_name == api_name))
        return type

    def filter_events(self, events, filter = None):
        filtered_events = events

        if filter is not None:
            filter_type = self.get_type(filter)
            filtered_events = [event for event in events if event._type == filter_type]

        return filtered_events

    def parse_events(self, api_response, filter = None):
        events = []

        if len(api_response) == 0:
            raise ResponseEmpty

        for event in api_response:
            try:
                type = self.get_type(event['type'])
                message = ''
                match type._api_name:
                    case 'PushEvent':
                        repo = event['repo']['name']
                        commits = len(event['payload']['commits']) if 'commits' in event['payload'] else 0
                        message = f'{commits} commit(s) to {repo}'

                    case 'CreateEvent':
                        repo = event['repo']['name']
                        message = f'repo named {repo}'

                    case 'PullRequestEvent':
                        repo = event['repo']['name']
                        title = event['payload']['pull_request']['title']
                        message = f'to repo {repo} named "{title}"'

                    case 'IssuesEvent':
                        repo = event['repo']['name']
                        issue = event['payload']['issue']['title']
                        message = f'on issue "{issue}" on repo "{repo}"'

                    case 'IssueCommentEvent':
                        repo = event['repo']['name']
                        issue = event['payload']['issue']['title']
                        message = f'on issue "{issue}" inside repo "{repo}"'

                    case 'ReleaseEvent':
                        repo = event['repo']['name']
                        message = f' on repo {repo}'

                obj_event = Event(type, message)
                events.append(obj_event)
            except:
                print(event)


        filtered_events = self.filter_events(events, filter)

        return filtered_events




