
import unittest

def decimal_to_binary(n):
    b = bin(n)
    if b.startswith("0b"):
        return b[2:]
    return b

def decimal_to_hex(n):
    h = hex(n)
    if h.startswith("0x"):
        return h[2:]
    return h

def binary_to_decimal(b):
    try:
        return int(b, 2)
    except:
        return "Ungültige Binärzahl"

def hex_to_decimal(h):
    try:
        return int(h, 16)
    except:
        return "Ungültige Hexzahl"

class TestConversionFunctions(unittest.TestCase):

    def test_decimal_to_binary(self):
        self.assertEqual(decimal_to_binary(0), "0")
        self.assertEqual(decimal_to_binary(1), "1")
        self.assertEqual(decimal_to_binary(2), "10")
        self.assertEqual(decimal_to_binary(10), "1010")
        self.assertEqual(decimal_to_binary(15), "1111")
        self.assertEqual(decimal_to_binary(16), "10000")
        self.assertEqual(decimal_to_binary(31), "11111")
        self.assertEqual(decimal_to_binary(64), "1000000")
        self.assertEqual(decimal_to_binary(127), "1111111")
        self.assertEqual(decimal_to_binary(255), "11111111")

    def test_decimal_to_hex(self):
        self.assertEqual(decimal_to_hex(0), "0")
        self.assertEqual(decimal_to_hex(1), "1")
        self.assertEqual(decimal_to_hex(10), "a")
        self.assertEqual(decimal_to_hex(15), "f")
        self.assertEqual(decimal_to_hex(16), "10")
        self.assertEqual(decimal_to_hex(31), "1f")
        self.assertEqual(decimal_to_hex(127), "7f")
        self.assertEqual(decimal_to_hex(255), "ff")
        self.assertEqual(decimal_to_hex(4095), "fff")
        self.assertEqual(decimal_to_hex(65535), "ffff")

    def test_binary_to_decimal(self):
        self.assertEqual(binary_to_decimal("0"), 0)
        self.assertEqual(binary_to_decimal("1"), 1)
        self.assertEqual(binary_to_decimal("10"), 2)
        self.assertEqual(binary_to_decimal("1010"), 10)
        self.assertEqual(binary_to_decimal("1111"), 15)
        self.assertEqual(binary_to_decimal("10000"), 16)
        self.assertEqual(binary_to_decimal("11111"), 31)
        self.assertEqual(binary_to_decimal("1000000"), 64)
        self.assertEqual(binary_to_decimal("1111111"), 127)
        self.assertEqual(binary_to_decimal("invalid"), "Ungültige Binärzahl")

    def test_hex_to_decimal(self):
        self.assertEqual(hex_to_decimal("0"), 0)
        self.assertEqual(hex_to_decimal("1"), 1)
        self.assertEqual(hex_to_decimal("a"), 10)
        self.assertEqual(hex_to_decimal("f"), 15)
        self.assertEqual(hex_to_decimal("10"), 16)
        self.assertEqual(hex_to_decimal("1f"), 31)
        self.assertEqual(hex_to_decimal("7f"), 127)
        self.assertEqual(hex_to_decimal("ff"), 255)
        self.assertEqual(hex_to_decimal("fff"), 4095)
        self.assertEqual(hex_to_decimal("xyz"), "Ungültige Hexzahl")

if __name__ == "__main__":
    unittest.main()
