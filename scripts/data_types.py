from enum import Enum
from typing import List

SearchMode = Enum('Mode', ['ACROSTIC', 'TELESTICH'])

Language = Enum('Language', ['en', 'grc', 'la'])


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
            self.loc = loc_and_content[0][1:]
            self.content = loc_and_content[1].strip()


    def get_relevant_char(self, mode: SearchMode) -> str:
        match mode:
            case 'ACROSTIC':
                return self.content[0]
            case 'TELESTICH':
                return self.content[-1]


    def print(self):
        print('<' + self.loc + '> ' + self.content)


class Hit:
    def __init__(self, buffer_len: int, term_len: int):
        self.buffer_len = buffer_len
        self.term_len = term_len
        self.lines = []


    def add_line(self, l: Line):
        self.lines.append(l)


    def print(self):
        for l in self.lines:
            l.print()


class Recordings:
    def __init__(self, hits: set[int], mode: SearchMode, lang: Language, term: str, buffer_len: int):
        self.raw_hits = hits
        self.mode = mode
        self.lang = lang
        self.buffer_len = buffer_len
        self.term_len = len(term)
        self.result_len = self.term_len + (2 * self.buffer_len)
        self.rich_hits : List[Hit] = []


    def update(self, j: int, line: Line):
        if j + self.buffer_len in self.raw_hits:
            self.rich_hits.append(Hit(self.buffer_len, self.term_len))

        for hit in self.rich_hits:
            if len(hit.lines) < self.result_len:
                hit.lines.append(line)


    def get_hits(self) -> list[Hit]:
        return self.rich_hits