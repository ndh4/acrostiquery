from enum import Enum
from operator import truediv

SearchMode = Enum('Mode', ['ACROSTIC', 'TELESTICH'])

Language = Enum('Language', ['en', 'grc', 'la'])

class Hit:
    def __init__(self):
        pass


class Line:
    def __init__(self, text: str):
        self.content = None
        self.loc = None
        if not text:
            self.eof_huh  = True
            self.tess_huh = False
            return

        self.eof_huh = False
        self.match_tess_string(text)
        return


    def is_eof(self) -> bool:
        return self.eof_huh


    def is_tess(self) -> bool:
        return self.tess_huh


    def match_tess_string(self, text: str):
        if text[0] == '<':
            self.tess_huh = True
            loc_and_content = text.split('>', 1)
            self.loc = loc_and_content[0]
            self.content = loc_and_content[1].strip()


    def get_relevant_char(self, mode: SearchMode) -> str:
        match mode:
            case 'ACROSTIC':
                return self.content[0]
            case 'TELESTICH':
                return self.content[-1]



class Recordings:
    def __init__(self, hits: set[int], mode: SearchMode, lang: Language, term: str, buffer_len: int):
        pass

    def update(self, j: int, line: Line):
        pass

    def get_hits(self) -> list[Hit]:
        pass


