from api.pet_api import PetApi
from PIL import Image
import requests
import json


class CatApi(PetApi):
    """Class - wrapper for the cat API
    """
    _API_KEY = ""

    def __init__(self, key):
        """Get an object

        Args:
            key (str): your API key
        """
        self._API_KEY = key

    def get_random_image(self, file_name):
        """Get a random image of a cat

        Args:
            file_name (str): the name of the file .jpg that will be saved
        """
        url = 'https://api.thecatapi.com/v1/images/search'
        response = requests.get(url, stream=True)
        json_response = json.loads(response.text)
        image_link = json_response[0]["url"]
        image = requests.get(image_link).content

        file_name += '.jpg'
        with open(file_name, 'wb') as f:
            f.write(image)

        img = Image.open(file_name)
        img.show()
