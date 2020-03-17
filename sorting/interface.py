import abc

class Sort(abc.ABC):
    @abc.abstractmethod
    def __init__(self, input):
        pass

    @abc.abstractmethod
    def sort(self):
        pass