API_ENDPOINT = "https://api.npoint.io/c790b4d5cab58020d391/"
import requests


class Post:

    def __init__(self, id):
        self.endpoint = API_ENDPOINT + f"{id - 1}"
        response = requests.get(self.endpoint)
        response.raise_for_status()
        self.json = response.json()


