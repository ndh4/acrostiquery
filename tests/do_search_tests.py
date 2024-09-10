import unittest

from SearchSpace import SearchSpace, FileSearchSpace
from do_search import do_search, get_hit_indices


class SearchTests(unittest.TestCase):

    def test_do_search(self):
        path = '../texts/la/lucan.bellum_civile/lucan.bellum_civile.part.1.tess'
        search_space = FileSearchSpace(path)
        rich_hits = do_search('ACROSTIC', 'la', search_space, 'HUQ', 2)
        for hit in rich_hits:
            hit.print()

    def test_get_hit_indices(self):
        path = '../texts/la/lucan.bellum_civile/lucan.bellum_civile.part.1.tess'
        search_space = FileSearchSpace(path)
        hits = get_hit_indices('ACROSTIC', 'la', search_space, 'HUQ')
        self.assertEqual(hits, {13})