import unittest

from SearchSpace import SearchSpace, FileSearchSpace, make_search_space
from data_types import Hit, Line
from do_search import do_search, get_hit_indices


class SearchTests(unittest.TestCase):

    def test_do_search(self):
        path = '../texts/la/lucan.bellum_civile/lucan.bellum_civile.part.1.tess'
        search_space = make_search_space(path)
        rich_hits = do_search('ACROSTIC', 'la', search_space, 'HUQ', 2)
        self.assertEqual(rich_hits.to_string(),
                         """<luc. 1.12> Bella geri placuit nullos habitura triumphos?
<luc. 1.13> Heu quantum terrae potuit pelagique parari
<luc. 1.14> Hoc, quem civiles hauserunt, sanguine, dextrae,
<luc. 1.15> Unde venit Titan, et nox ubi sidera condit,
<luc. 1.16> Quaque dies medius flagrantibus aestuat horis,
<luc. 1.17> Et qua bruma, rigens ac nescia vere remitti,
<luc. 1.18> Adstringit Scythico glacialem frigore pontum!""")


    def test_get_hit_indices(self):
        path = '../texts/la/lucan.bellum_civile/lucan.bellum_civile.part.1.tess'
        search_space = make_search_space(path)
        hits = get_hit_indices('ACROSTIC', 'la', search_space, 'HUQ')
        self.assertEqual(hits, {13})

    def test_do_search_dir(self):
        path = '../texts/la/lucan.bellum_civile'
        search_space = make_search_space(path)
        rich_hits = do_search('ACROSTIC', 'la', search_space, 'HUQ', 2)
        self.assertEqual(rich_hits.to_string(),
                         """<luc. 1.12> Bella geri placuit nullos habitura triumphos?
<luc. 1.13> Heu quantum terrae potuit pelagique parari
<luc. 1.14> Hoc, quem civiles hauserunt, sanguine, dextrae,
<luc. 1.15> Unde venit Titan, et nox ubi sidera condit,
<luc. 1.16> Quaque dies medius flagrantibus aestuat horis,
<luc. 1.17> Et qua bruma, rigens ac nescia vere remitti,
<luc. 1.18> Adstringit Scythico glacialem frigore pontum!""")

    def test_get_hit_indices_dir(self):
        path = '../texts/la/lucan.bellum_civile'
        search_space = make_search_space(path)
        hits = get_hit_indices('ACROSTIC', 'la', search_space, 'HUQ')
        self.assertEqual(len(hits), 1)