"""Simple Testing Script."""
import unittest
from boiler import huffman


class TestAlgorithms(unittest.TestCase):
    def test_huffman_coding(self):
        inb = b"A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
        res = 0b1000011101001000110010011101100111001001000111110010011111011111100010001111110100111001001011111011101000111111001
        r = huffman(inb)
        self.assertEqual(r, res)


if __name__ == '__main__':
    unittest.main()
