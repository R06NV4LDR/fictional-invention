
import unittest

def get_unicode_value(ch):
    return ord(ch)

class TestAsciiUnicode(unittest.TestCase):

    def test_basic_ascii(self):
        self.assertEqual(get_unicode_value('A'), 65)
        self.assertEqual(get_unicode_value('a'), 97)
        self.assertEqual(get_unicode_value('0'), 48)
        self.assertEqual(get_unicode_value('9'), 57)
        self.assertEqual(get_unicode_value(' '), 32)
        self.assertEqual(get_unicode_value('!'), 33)
        self.assertEqual(get_unicode_value('@'), 64)
        self.assertEqual(get_unicode_value('Z'), 90)
        self.assertEqual(get_unicode_value('z'), 122)
        self.assertEqual(get_unicode_value('\n'), 10)

    def test_unicode_characters(self):
        self.assertEqual(get_unicode_value('€'), 8364)
        self.assertEqual(get_unicode_value('✓'), 10003)
        self.assertEqual(get_unicode_value('ß'), 223)
        self.assertEqual(get_unicode_value('ü'), 252)
        self.assertEqual(get_unicode_value('Ω'), 937)

if __name__ == "__main__":
    unittest.main()
