import requests
from exception import UserNotFound


class API:

    ENDPOINT = 'https://api.github.com'

    @classmethod
    def fetch_events(cls, username):

        url = f'{cls.ENDPOINT}/users/{username}/events'
        api_response = requests.get(url)

        if api_response.status_code != 200:
            raise UserNotFound(username)

        events = api_response.json()
        return events