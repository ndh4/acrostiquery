from abc import abstractmethod
from data_types import Line


class SearchSpace:
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def get_next_line(self) -> Line | None:
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


class DirectorySearchSpace(SearchSpace):
    def __init__(self, pathname: str):
        return

    def reset(self):
        pass

    def get_next_line(self) -> Line | None:
        pass