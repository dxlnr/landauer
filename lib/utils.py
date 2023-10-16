"""Universal Utilities."""
import argparse
from typing import Union


def create_arg_parser():
    """Get arguments from command lines."""
    parser = argparse.ArgumentParser(description="Landauer's.")
    parser.add_argument("-a", type=str, help="Algorithm that should be used.")
    parser.add_argument("-d", type=str, help="Input data file (path).")
    return parser


def bitgen(x: bytes):
    """Converts bytes into bit stream.

    :params x: Iterable chars stream.
    :returns: Generator which converts chars into string of bits.
    """
    for c in x:
        for i in range(8):
            yield int((c & (0x80 >> i)) != 0)


def bytesize(bs: Union[str, int, bytes]) -> int:
    """Get size of a bit sequence in bytes."""
    if isinstance(bs, str):
        return (len(bs) + 7) // 8
    elif isinstance(bs, int):
        return (bs.bit_length() + 7) // 8
    elif isinstance(bs, bytes):
        return len(bs)
    else:
        raise TypeError("bs must be str or int")


def byterange(byte_count: int) -> str:
    """Return a string representation of the given size in bytes, KB, MB, or GB."""
    if byte_count < 1024:
        return f"{byte_count} B"
    elif byte_count < 1024 * 1024:
        return f"{byte_count / 10**3:.2f} KB"
    elif byte_count < 1024 * 1024 * 1024:
        return f"{byte_count / (10**6):.2f} MB"
    else:
        return f"{byte_count / (10**9):.2f} GB"
