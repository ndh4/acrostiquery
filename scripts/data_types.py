from enum import Enum

SearchMode = Enum('Mode', ['ACROSTIC', 'TELESTICH'])

Language = Enum('Language', ['en', 'grc', 'la'])

class Hit:
    def __init__(self):
        pass


class Line:
    def __init__(self):
        pass

    def eos(self) -> bool:
        pass


class Recordings:
    def __init__(self, hits: set[int], mode: SearchMode, lang: Language, term: str, buffer_len: int):
        pass

    def update(self, j: int, line: Line):
        pass

    def get_hits(self) -> list[Hit]:
        pass


