from api.impl.cat_api_wrapper import CatApiWrapper
from api.config import CAT_API_KEY

if __name__ == '__main__':
    wrapper = CatApiWrapper(CAT_API_KEY)

    # wrapper.get_random_image("random_cat")

    breed_dict = wrapper.get_breed_dict()
    for elements in breed_dict:
        print(elements)

