import unittest
from main import remove_punctuation, map_function, shuffle_function, reduce_function

class TestMapReduce(unittest.TestCase):
    def test_remove_punctuation(self):
        text = "Hello, World! This is a test."
        expected = "Hello World This is a test"
        self.assertEqual(remove_punctuation(text), expected)

    def test_map_function(self):
        words = ["hello", "world", "hello"]
        expected = [("hello", 1), ("world", 1), ("hello", 1)]
        self.assertEqual(map_function(words), expected)

    def test_shuffle_function(self):
        mapped_values = [("hello", 1), ("world", 1), ("hello", 1)]
        shuffled = list(shuffle_function(mapped_values))
        shuffled_dict = {k: v for k, v in shuffled}
        self.assertEqual(shuffled_dict["hello"], [1, 1])
        self.assertEqual(shuffled_dict["world"], [1])

    def test_reduce_function(self):
        key_values = ("hello", [1, 1, 1])
        expected = ("hello", 3)
        self.assertEqual(reduce_function(key_values), expected)

if __name__ == '__main__':
    unittest.main()
