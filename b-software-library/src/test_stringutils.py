import unittest
import stringutils

class TestStringUtils(unittest.TestCase):

    def test_compare(self):
        self.assertEqual(stringutils.compare("1.2", "1.1"), 1)
        self.assertEqual(stringutils.compare("1.1", "1.2"), -1)
        self.assertEqual(stringutils.compare("1.1", "1.10"), -1)
        self.assertEqual(stringutils.compare("1.2", "1.10"), 1)
        self.assertEqual(stringutils.compare("2.1", "1"), 1)
        self.assertEqual(stringutils.compare("1", "2.1"), -1)
        self.assertEqual(stringutils.compare("A", "a"), -1)
        self.assertEqual(stringutils.compare("a", "A"), 1)
        self.assertEqual(stringutils.compare("Asd", "Avd"), -1)
        self.assertEqual(stringutils.compare("Ab", "A"), 1)
        self.assertEqual(stringutils.compare("", ""), 0)
        self.assertEqual(stringutils.compare("abc", "abc"), 0)
        self.assertEqual(stringutils.compare("a bc", "a bc"), 0)
        self.assertEqual(stringutils.compare("a ac", "a b"), -1)
        self.assertEqual(stringutils.compare("a b", "a "), 1)
        self.assertEqual(stringutils.compare(123, 124), -1)
        self.assertEqual(stringutils.compare(124, 123), 1)
        self.assertEqual(stringutils.compare(12, 123), -1)
        self.assertEqual(stringutils.compare(123, 12), 1)
        self.assertEqual(stringutils.compare(12, 12), 0)

        with self.assertRaises(ValueError):
            stringutils.compare(None, None)

if __name__ == "__main__":
    unittest.main()