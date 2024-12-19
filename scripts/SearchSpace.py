import os
import re
from abc import abstractmethod
from typing import Optional, List

from data_types import Line, Language
from tesslang import standardize


class SearchSpace:
    # def __init__(self, lang):
    #     self.lang = lang

    @abstractmethod
    def reset(self):
        pass


    @abstractmethod
    def get_next_line(self) -> Optional[Line]:
        pass


    @abstractmethod
    def clean_up(self):
        pass


def make_search_space(name: str, lang: Language) -> SearchSpace:
    # possibilities for name:
    # '' -> search all texts for given language
    # 'augustine' -> search all texts under this author
    # 'augustine.de_ordine' -> search all texts under this author/work
    base = os.path.join('../texts/', lang)
    all = []
    for root, dirs, files in os.walk(base):
        all.extend(sorted(sorted([os.path.join(root, file) for file in files
                           if file.startswith(name) and file.endswith('.tess')],
                          key=name_to_int)))
    return MultiSearchSpace(all, lang)
    # if name == '':
    #     return MultiSearchSpace(base, lang)
    # if os.path.isdir(pathname):
    #     return MultiSearchSpace(pathname, lang)
    # if os.path.isfile(base + '/' + name):
    #     return SingleSearchSpace(base + '/' + name, lang)
    # if os.path.isfile(base + '/' + name + '.tess'):
    #     return SingleSearchSpace(base + '/' + name + '.tess', lang)
    # raise Exception("Invalid Search Space:", name)


class FileSearchSpace(SearchSpace):
    def __init__(self, pathname: str, lang: Language):
        self.pathname = pathname
        self.lang = lang
        self.file = None
        return


    def reset(self):
        self.clean_up()
        self.file = open(self.pathname, 'r')


    def get_next_line(self) -> Optional[Line]:
        while True:
            line_candidate = Line(self.file.readline())
            if line_candidate.is_eof():
                return None
            if line_candidate.is_tess():
                line_candidate.standardize(self.lang)
                return line_candidate


    def clean_up(self):
        if self.file is not None:
            self.file.close()
            self.file = None


def name_to_int(name: str) -> int:
    result = re.search('\\d+', name)
    if result is None:
        return -1
    else:
        return int(result.group())

class MultiSearchSpace(SearchSpace):
    def __init__(self, paths: List[str], lang: Language):
        self.spaces = [FileSearchSpace(path, lang) for path in paths]
        self.current_space = -1
        return


    def reset(self):
        self.clean_up()
        if len(self.spaces) >= 1:
            self.current_space = 0
            self.spaces[self.current_space].reset()


    def get_next_line(self) -> Optional[Line]:
        while self.current_space_is_valid():
            line_candidate = self.spaces[self.current_space].get_next_line()
            if line_candidate:
                return line_candidate
            else:
                self.spaces[self.current_space].clean_up()
                self.current_space += 1
                if self.current_space_is_valid():
                    self.spaces[self.current_space].reset()
        return None


    def clean_up(self):
        if self.current_space_is_valid():
            self.spaces[self.current_space].clean_up()
        self.current_space = -1


    def current_space_is_valid(self):
        return -1 < self.current_space < len(self.spaces)