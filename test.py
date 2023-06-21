import unittest
from utils import Utils

class TestUtils(unittest.TestCase):

    def get_lowercase_plural_result(self, word, expected_output):
        self.assertEqual(Utils.make_lowercase_plural(word), expected_output)

    def get_delete_keys_result(self, dictionary, keys_to_delete, expected_output):
        self.assertEqual(Utils.delete_keys_from_dict(dictionary, keys_to_delete), expected_output)

    def test_make_lowercase_plural(self):
        self.get_lowercase_plural_result('dog', 'dogs')
        self.get_lowercase_plural_result('brush', 'brushes')
        self.get_lowercase_plural_result('security', 'securities')
        self.get_lowercase_plural_result('bus', 'buses')

    def test_delete_keys_from_dict(self):
        self.get_delete_keys_result(
            {'name': 'Peter', 'age': 4, 'city': 'Minnesota'}, ['age', 'city'], {'name': 'Peter'}
        )
        self.get_delete_keys_result(
            {'a': 1, 'b': 2, 'c': 3, 'd': 4}, ['b', 'd'], {'a': 1, 'c': 3}
        )
        self.get_delete_keys_result(
            {'color': 'white', 'hex': '#ffffff'}, [], {'color': 'white', 'hex': '#ffffff'}
        )
        self.get_delete_keys_result(
            {'x': 'apple', 'y': 'banana', 'b': 'pineapple', 'c': 'fish'}, ['c'], {'x': 'apple', 'y': 'banana', 'b': 'pineapple'}
        )

    def test_read_from_json(self):
        items = Utils.read_from_json('items.json')
        self.assertIn('admins', dict.keys(items))
        self.assertIsInstance(items['items'], list)
        self.assertIsInstance(items['metodos'], list)
        self.assertIsInstance(items['admins'], list)
        self.assertEqual(list(dict.keys(items['items'][0])), ['title', 'pricing', 'imagesource'])

if __name__ == '__main__':
    unittest.main()
