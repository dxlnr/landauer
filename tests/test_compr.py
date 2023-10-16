"""Simple Testing Script."""
import unittest

from boiler import decode_huffman, huffman


class TestAlgorithms(unittest.TestCase):
    def test_huffman_coding(self):
        """Test Huffman Coding."""
        inb = b"A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED"
        res = 0b1000011101001000110010011101100111001001000111110010011111011111100010001111110100111001001011111011101000111111001
        # encode
        r, encs = huffman(inb)
        self.assertEqual(r, res)
        # decode
        dec = decode_huffman(r, encs)
        self.assertEqual(inb, dec)


if __name__ == "__main__":
    unittest.main()
