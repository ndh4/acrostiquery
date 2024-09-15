import unittest

from SearchSpace import make_search_space
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

    def test_qed_search(self):
        path = '../texts/la/lucan.bellum_civile/lucan.bellum_civile.part.1.tess'
        search_space = make_search_space(path)
        rich_hits = do_search('ACROSTIC', 'la', search_space, 'QED', 0)
        self.assertEqual(rich_hits.to_string(),
                         """<luc. 1.136> Qualis frugifero quercus sublimis in agro,
<luc. 1.137> Exuvias veteres populi sacrataque gestans
<luc. 1.138> Dona ducum, nec iam validis radicibus haerens,""")

    def test_tt_search(self):
        path = '../texts/la/lucan.bellum_civile/lucan.bellum_civile.part.1.tess'
        search_space = make_search_space(path)
        rich_hits = do_search('ACROSTIC', 'la', search_space, 'TT', 1)
        self.assertEqual(rich_hits.to_string(),
                         """<luc. 1.20> Et gens si qua iacet nascenti conscia Nilo.
<luc. 1.21> Tunc, si tantus amor belli tibi, Roma, nefandi,
<luc. 1.22> Totum sub Latias leges cum miseris orbem,
<luc. 1.23> In te verte manus: nondum tibi defuit hostis.

<luc. 1.58> Orbe tene medio: pars aetheris illa sereni
<luc. 1.59> Tota vacet, nullaeque obstent a Caesare nubes.
<luc. 1.60> Tunc genus humanum positis sibi consulat armis,
<luc. 1.61> Inque vicem gens omnis amet: Pax missa per orbem

<luc. 1.96> Nec pretium tanti tellus pontusque furoris
<luc. 1.97> Tunc erat: exiguum dominos commisit asylum.
<luc. 1.98> Temporis augusti mansit concordia discors;
<luc. 1.99> Paxque fuit non sponte ducum. Nam sola futuri

<luc. 1.216> Limes ab Ausoniis disterminat arva colonis.
<luc. 1.217> Tum vires praebebat hiems, atque auxerat undas
<luc. 1.218> Tertia iam gravido pluvialis Cynthia cornu,
<luc. 1.219> Et madidis Euri resolutae flatibus Alpes.

<luc. 1.580> Edidit. Et medio visi consurgere Campo
<luc. 1.581> Tristia Sullani cecinere oracula manes:
<luc. 1.582> Tollentemque caput gelidas Anienis ad undas
<luc. 1.583> Agricolae fracto Marium fugere sepulchro.

<luc. 1.597> Vestalemque chorum ducit vittata sacerdos,
<luc. 1.598> Troianam soli cui fas vidisse Minervam.
<luc. 1.599> Tunc qui fata deum secretaque carmina servant,
<luc. 1.600> Et lotam parvo revocant Almone Cybellen:""")