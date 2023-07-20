import abc


class PetApiWrapper(abc.ABC):
    """Abstract class for dog API and cat API"""

    @abc.abstractmethod
    def __init__(self, key):
        pass

    @abc.abstractmethod
    def get_random_image(self, file_name):
        """Get a random pet image

        Args:
            file_name (str): the name of the file .jpg that will be saved
        """
        pass

    @abc.abstractmethod
    def get_random_images(self, files_name, amount=2):
        """Get a several random pet images

        Args:
            amount (int): the number of images (min = 2, max =  10)
            files_name (str): the name of the file .jpg that will be saved
        """
        pass

    @abc.abstractmethod
    def get_breed_dict(self) -> dict:
        """Get a breed dictionary

        Returns:
            dict: the breed dictionary that includes pairs of `name` and `id`
        """
        pass
