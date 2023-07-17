from abc import ABCMeta, abstractmethod, abstractproperty

class PetApi(ABCMeta):

    @abstractmethod
    def get_random_image(file_name):
        pass

    @abstractmethod
    def printT():
        pass