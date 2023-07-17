from pet_api import PetApi
from PIL import Image
import requests
import json

class CatApi(PetApi):

    _API_KEY = ""

    def __init__(self, key):
        self._API_KEY = key

    def get_random_image(self, file_name):
        url = 'https://api.thecatapi.com/v1/images/search'
        response = requests.get(url, stream= True)
        json_respose = json.loads(response.text)
        image_link = json_respose[0]["url"]
        image = requests.get(image_link).content

        file_name+='.jpg'
        with open(file_name, 'wb') as f:
            f.write(image)

        img = Image.open(file_name)
        img.show()