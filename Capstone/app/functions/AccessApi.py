# boiler plate code:

# objects for  abstracted communication
# does the HTTP interaction returns the JSON
import requests
import json


class AccessApi:
    """
    Class AccessApi is used to abstract lower level access to course required API

    Attributes
    ----------
    url : str
        A valid website used to hold the courses json filesS

    Methods
    -------
    url_active()
        returns True if the url is currently responding without errors, and False if not.

    get_end_point(endpoint)
        returns the json output of the GET request

    """
    def __init__(self, url):
        """
        Parameters
        ----------
        url: str
           a valid website forexample: http://google.com
        """
        self.url: str = url

    @property
    def url(self) -> str:
        return self.__url

    @url.setter
    def url(self, url: str):
        self.__url: str = url

    def url_active(self) -> bool:
        response: requests.models.Response = requests.get(self.__url)
        if response:
            return True
        else:
            return False

    def get_end_point(self, end_point:str) -> dict:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """
        response: requests.models.Response = requests.get(self.__url + end_point)
        content: dict = json.loads(response.text)[0]
        return content

    def get_status_code(self, end_point:str) -> int:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """
        response: requests.models.Response = requests.get(self.__url +  end_point)
        status_code: int = response.status_code
        return status_code

    def get_elapsed_time(self, end_point:str) -> float:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """
        response: requests.models.Response = requests.get(self.__url + end_point)
        elapsed_time: float = response.elapsed.total_seconds()
        return elapsed_time


