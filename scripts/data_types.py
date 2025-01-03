import re
from enum import Enum

from tesslang import standardize

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
        else:
            self.tess_huh = False


    def get_relevant_char(self, mode: SearchMode) -> str:
        # print(self.to_string())
        if mode == 'ACROSTIC':
                for char in self.content:
                    if char.isalpha():
                        return char
                return '*'
        else:
                for char in reversed(self.content):
                    if char.isalpha():
                        return char
                return '*'


    def print(self):
        print(self.to_string())

    def to_string(self):
        return '<' + self.loc + '> ' + self.content

    def standardize(self, lang: Language):
        self.content = standardize(lang, self.content)


class Hit:
    def __init__(self, buffer_len: int, term_len: int):
        self.buffer_len : int = buffer_len
        self.term_len : int = term_len
        self.lines : list[Line] = []


    def add_line(self, l: Line):
        self.lines.append(l)


    def print(self):
        for l in self.lines:
            l.print()

    def to_string(self):
        return '\n'.join(line.to_string() for line in self.lines)


class Hits:
    def __init__(self):
        self.hits : list[Hit] = []


    def add_hit(self, h: Hit):
        self.hits.append(h)

    def len(self):
        return len(self.hits)

    def to_string(self):
        return '\n\n'.join([hit.to_string() for hit in self.hits])

    def iter(self):
        return self.hits

    def remove_duplicates(self):
        d = {}
        for h in self.hits:
            d[h.to_string()] = h
        self.hits = list(d.values())


class Recordings:
    def __init__(self, hits: set[int], mode: SearchMode, lang: Language, term: str, buffer_len: int):
        self.raw_hits = hits
        self.mode = mode
        self.lang = lang
        self.buffer_len = buffer_len
        self.term_len = len(term)
        self.result_len = self.term_len + (2 * self.buffer_len)
        self.rich_hits : Hits = Hits()


    def update(self, j: int, line: Line):
        if j < self.buffer_len and j in self.raw_hits:
            new_hit = Hit(self.buffer_len, self.term_len)
            for i in range(j, self.buffer_len):
                new_hit.add_line(Line('<' + re.sub(r"\d", ' ', line.loc) + '>'))
            self.rich_hits.add_hit(new_hit)

        if j + self.buffer_len in self.raw_hits:
            self.rich_hits.add_hit(Hit(self.buffer_len, self.term_len))

        for hit in self.rich_hits.iter():
            if len(hit.lines) < self.result_len:
                hit.lines.append(line)


    def get_hits(self) -> Hits:
        return self.rich_hits