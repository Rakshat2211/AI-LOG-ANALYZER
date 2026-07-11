from abc import ABC
from abc import abstractmethod


class BaseCollector(ABC):

    @abstractmethod
    def collect(self):
        """
        Collect logs from the source.

        Returns:
            list[dict]
        """
        pass