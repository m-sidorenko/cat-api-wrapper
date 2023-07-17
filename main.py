from cat_api import CatApi
from config import API_KEY

if __name__ == '__main__':
    api = CatApi(API_KEY)
    api.get_random_image("random_cat")