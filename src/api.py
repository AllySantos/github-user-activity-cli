import requests

class API:
    def __init__(self):
        self._endpoint = 'https://api.github.com/events'

    @property
    def endpoint(self):
        return self._endpoint

    def fetch_events(self, filter = None):
        api_response = requests.get(self.endpoint)

        if api_response.status_code != 200:
            return False

        events = api_response.json()
        return events