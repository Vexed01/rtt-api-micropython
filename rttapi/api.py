import requests
import rttapi.parser as parser
from requests.auth import HTTPBasicAuth


def _request_basic_auth(credentials, url):
    username, password = credentials

    auth = HTTPBasicAuth(username, password)

    response = requests.get(url, auth=auth)

    if response.ok:
        return response.json()
    else:
        # TODO we should throw an error
        return {}

'''
Makes network requests to the Realtime Trains API

Requests are authenticated via HTTPBasicAuth, with credentials passed in as a pair.
'''
class _Api:

    urlBase = "https://api.rtt.io/api/v1"

    def fetch_station_info(self, credentials, station):
        url = "{base}/json/search/{station}".format(base=self.urlBase, station=station)
        return _request_basic_auth(credentials, url)

    def fetch_service_info(self, credentials, service_uid, service_date):
        url = "{base}/json/service/{service_uid}/{year}/{month}/{day}".format(
            base=self.urlBase,
            service_uid=service_uid,
            year=service_date.strftime('%Y'),
            month=service_date.strftime('%m'),
            day=service_date.strftime('%d')
        )
        return _request_basic_auth(credentials, url)



class RttApi:
    def __init__(self, username: str, password: str):
        self.credentials = (username, password)
        self.__api = _Api()

    def search_station_departures(self, station_code: str):
        json = self.__api.fetch_station_info(self.credentials, station_code)
        return parser.parse_search(json)
