from api.pet_api_wrapper import PetApiWrapper
from api.config import CAT_API_KEY
from PIL import Image
import requests
import json
import os


class CatApiWrapper(PetApiWrapper):
    """Class - wrapper for the cat API"""
    _API_KEY = ""

    def __init__(self, key):
        """Class - wrapper for the cat API

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

    def get_random_images(self, files_name, amount=2):
        """Get a several random pet images

        Args:
            amount (int): the number of images (min = 2, max =  10)
            files_name (str): the name of the file .jpg that will be saved
        """
        url = f'https://api.thecatapi.com/v1/images/search?'

        # check amount
        if amount > 10:
            number = 10
        elif amount < 2:
            number = 2
        else:
            number = amount
        url += f'limit={number}'

        # add the api key
        url += f'&api_key={CAT_API_KEY}'

        # send request
        response = requests.get(url, stream=True)
        json_response = json.loads(response.text)

        for element in json_response:
            image_link = element["url"]
            image = requests.get(image_link).content

            files_name += '_0.jpg'
            with open(files_name, 'wb') as f:
                f.write(image)

        # img = Image.open(file_name)
        # img.show()

    def get_breed_dict(self) -> dict:
        """Get a breed dictionary

        Returns:
            dict: the breed dictionary that includes pairs of `name` and `id`
        """
        result = dict()
        url = 'https://api.thecatapi.com/v1/breeds?limit=100&page=0'
        response = requests.get(url, stream=True)
        list_response = json.loads(response.text)
        for element in list_response:
            result[element['name']] = element['id']
        return result
