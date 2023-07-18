import abc

class PetApi(abc.ABC):
    """Abstract class for dog API and cat API

    Args:
        abc (_type_): system abstract parent-class
    """
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