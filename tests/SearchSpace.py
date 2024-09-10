from abc import abstractmethod
from typing import TextIO


class SearchSpace:
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def get_next_line(self):
        pass


class FileSearchSpace(SearchSpace):
    def __init__(self, pathname: str):
        self.pathname = pathname
        self.file = None
        return

    def reset(self):
        if self.file is not None:
            self.file.close()
        self.file = open(self.pathname, 'r')

    def get_next_line(self):
        pass


class DirectorySearchSpace(SearchSpace):
    def __init__(self, pathname: str):
        return

    def reset(self):
        pass

    def get_next_line(self):
        pass