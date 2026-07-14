from abc import ABC
from abc import abstractmethod


class BaseParser(ABC):

    @abstractmethod
    def parse(self, raw_log):
        """
        Convert a raw log into our application's standard format.
        """
        pass