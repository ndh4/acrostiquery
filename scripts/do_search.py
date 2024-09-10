from data_types import SearchMode, Language, Hit, Line, Recordings

import SearchSpace

def do_search(mode: SearchMode, lang: Language, space: SearchSpace, term: str, buffer_len: int) -> list[Hit]:

    hits = get_hit_indices(mode, lang, space, term)

    rich_hits = flesh_out_hits(hits, mode, lang, space, term, buffer_len)

    return rich_hits


def get_hit_indices(mode: SearchMode, lang: Language, space: SearchSpace, term: str) -> set[int]:
    """
    KMP search algorithm from https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
    """

    hits = set()

    k = 0
    kmp_table = generate_kmp_table(term)
    j, line = first_line(space)

    while not line.eos():
        if same_letter(term[k], line.get_relevant_char(mode)):
            j, line = next_line(j, space)
            k += 1
            if k == len(term):
                hits.add(j - k)
                k = kmp_table[k]
        else:
            k = kmp_table[k]
            if k < 0:
                j, line = next_line(j, space)
                k += 1

    return hits


def generate_kmp_table(term: str) -> list[int]:
    """
    KMP table algorithm from https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
    """
    table = list(term + ' ')
    pos = 1
    cnd = 0

    table[0] = -1

    while pos < len(term):
        if term[pos] == term[cnd]:
            table[pos] = table[cnd]
        else:
            table[pos] = cnd
            while cnd >= 0 and term[pos] != term[cnd]:
                cnd = table[cnd]
        pos += 1
        cnd += 1

    table[pos] = cnd

    return table


def same_letter(a: str, b: str) -> bool:
    pass


def first_line(space: SearchSpace) -> (int, Line):
    space.reset()
    return 0, space.get_next_line()


def next_line(j: int, space: SearchSpace) -> (int, Line):
    return j + 1, space.get_next_line()


def flesh_out_hits(hits: set[int], mode: SearchMode, lang: Language, space: SearchSpace, term: str, buffer_len: int) -> list[Hit]:

    j, line = first_line(space)
    recordings_in_progress = Recordings(hits, mode, lang, term, buffer_len)
    while not line.eos():
        recordings_in_progress.update(j, line)
        j, line = next_line(j, space)

    return recordings_in_progress.get_hits()