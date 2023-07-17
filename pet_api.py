import abc

class PetApi(abc.ABC):

    @abc.abstractmethod
    def __init__(self, key):
        pass

    @abc.abstractmethod
    def get_random_image(self, file_name):
        pass