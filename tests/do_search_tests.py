import unittest

from SearchSpace import SearchSpace, FileSearchSpace, make_search_space
from do_search import do_search, get_hit_indices


class SearchTests(unittest.TestCase):

    def test_do_search(self):
        path = '../texts/la/lucan.bellum_civile/lucan.bellum_civile.part.1.tess'
        search_space = make_search_space(path)
        rich_hits = do_search('ACROSTIC', 'la', search_space, 'HUQ', 2)
        for hit in rich_hits:
            hit.print()

    def test_get_hit_indices(self):
        path = '../texts/la/lucan.bellum_civile/lucan.bellum_civile.part.1.tess'
        search_space = make_search_space(path)
        hits = get_hit_indices('ACROSTIC', 'la', search_space, 'HUQ')
        self.assertEqual(hits, {13})

    def test_do_search_dir(self):
        path = '../texts/la/lucan.bellum_civile'
        search_space = make_search_space(path)
        rich_hits = do_search('ACROSTIC', 'la', search_space, 'HUQ', 2)
        for hit in rich_hits:
            hit.print()

    def test_get_hit_indices_dir(self):
        path = '../texts/la/lucan.bellum_civile'
        search_space = make_search_space(path)
        hits = get_hit_indices('ACROSTIC', 'la', search_space, 'HUQ')
        self.assertEqual(len(hits), 1)