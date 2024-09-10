import os
import re
from abc import abstractmethod
from data_types import Line


class SearchSpace:
    @abstractmethod
    def reset(self):
        pass


    @abstractmethod
    def get_next_line(self) -> Line | None:
        pass


    @abstractmethod
    def clean_up(self):
        pass


def make_search_space(pathname: str) -> SearchSpace:
    if os.path.isdir(pathname):
        return DirectorySearchSpace(pathname)
    if os.path.isfile(pathname):
        return FileSearchSpace(pathname)


class FileSearchSpace(SearchSpace):
    def __init__(self, pathname: str):
        self.pathname = pathname
        self.file = None
        return


    def reset(self):
        self.clean_up()
        self.file = open(self.pathname, 'r')


    def get_next_line(self) -> Line | None:
        while True:
            line_candidate = Line(self.file.readline())
            if line_candidate.is_eof():
                return None
            if line_candidate.is_tess():
                return line_candidate


    def clean_up(self):
        if self.file is not None:
            self.file.close()
            self.file = None

def name_to_int(name: str) -> int:
    result = re.search('\d+', name)
    if result is None:
        return -1
    else:
        return int(result.group())

class DirectorySearchSpace(SearchSpace):
    def __init__(self, dirpath: str):
        self.spaces = [make_search_space(os.path.join(dirpath, subpath))
                       for subpath in
                       sorted(os.listdir(dirpath), key=name_to_int)]
        self.current_space = -1
        return


    def reset(self):
        self.clean_up()


    def get_next_line(self) -> Line | None:
        while -1 < self.current_space < len(self.spaces):
            line_candidate = self.spaces[self.current_space].get_next_line()
            if line_candidate:
                return line_candidate
            else:
                self.spaces[self.current_space].clean_up()
                self.current_space += 1
                self.spaces[self.current_space].reset()
        return None


    def clean_up(self):
        self.spaces[self.current_space].clean_up()
        self.current_space = -1