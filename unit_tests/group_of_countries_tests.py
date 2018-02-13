import unittest

from server import groups_of_countries
class Group_of_countries(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual([], groups_of_countries([],0))
        self.assertEqual([], groups_of_countries([],1))
        self.assertEqual([], groups_of_countries([],2))
        self.assertEqual([], groups_of_countries([],3))
        self.assertEqual([], groups_of_countries([],4))
        self.assertEqual([], groups_of_countries([],100500))

    def test_full_list (self):
        self.assertEqual([(1,2)], groups_of_countries([1,2], 2))
        self.assertEqual([(1,2),(3,4)], groups_of_countries([1,2,3,4], 2))

    def test_none_in_the_end(self):
        self.assertEqual([(1, None)], groups_of_countries([1], 2))
        self.assertEqual([(1, 2), (3, None)], groups_of_countries([1, 2, 3], 2))


if __name__ == '__main__':
    unittest.main()
