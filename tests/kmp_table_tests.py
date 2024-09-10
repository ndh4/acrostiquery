import unittest

from scripts.do_search import generate_kmp_table

class KmpTableTests(unittest.TestCase):
    """
    Test cases from https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
    """

    def test_abcdabd(self):
        table = generate_kmp_table('abcdabd')
        self.assertEqual(table, [-1, 0, 0, 0, -1, 0, 2, 0])

    def test_abacababc(self):
        table = generate_kmp_table('ABACABABC')
        self.assertEqual(table, [-1, 0, -1, 1, -1, 0, -1, 3, 2, 0])

    def test_abacababa(self):
        table = generate_kmp_table('ABACABABA')
        self.assertEqual(table, [-1, 0, -1, 1, -1, 0, -1, 3, -1, 3])

    def test_participate_in_parachute(self):
        table = generate_kmp_table('PARTICIPATE IN PARACHUTE')
        self.assertEqual(table, [-1, 0, 0, 0, 0, 0, 0, -1, 0, 2, 0, 0, 0, 0, 0, -1, 0, 0, 3, 0, 0, 0, 0, 0, 0])