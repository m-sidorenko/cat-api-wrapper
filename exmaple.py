from api.cat_api import CatApi
from res.config import CAT_API_KEY

if __name__ == '__main__':
    api = CatApi(CAT_API_KEY)
    api.get_random_image("random_cat")
