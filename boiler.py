"""Compression"""
from typing_extensions import Self
import math
from collections import defaultdict

from lib.utils import bitgen


class Node:
    """Node of a binary tree

    :param w: Weight of the node; frequency of appearance.
    :param v: Symbol value.
    :param childs: Children of the node.
    """

    def __init__(self, w: int, v: str = None, childs: list[Self] = [None, None]):
        self.w = w
        self.v = v
        self.childs = childs
        self.enc = 0

    def __repr__(self):
        return f"({self.v}) {self.w} : {bin(self.enc)}"

    def tree(self, level=0):
        ret = "\t" * level + self.v + "\n"
        for c in self.childs:
            if c is not None:
                ret += c.tree(level + 1)
        return ret

    @staticmethod
    def result(n: Self = None):
        if n is None:
            return
        if n.v is not None:
            print("(dfs)", repr(n))
        for c in n.childs:
            Node.result(c)


def huffman(enw: bytes) -> None:
    """Huffman coding.

    :param enw: Input bytes stream.
    """
    lt = defaultdict(lambda: 0)
    for c in enw:
        lt[c] += 1

    lt = dict(sorted(lt.items(), key=lambda kv: kv[1]))

    ns = [Node(v, chr(k)) for k, v in lt.items()]

    while len(ns) > 1:
        left = ns.pop(0) if ns else None
        right = ns.pop(0) if ns else None

        nn = Node(w=((left.w + right.w)), childs=[left, right])

        idx = next((i for i, x in enumerate(ns) if nn.w <= x.w), len(ns))
        ns.insert(idx, nn)

    def enc(n: Node):
        """Finding encodings using the depth-first search algorithm."""
        if n is None:
            return
        for idx, c in enumerate(n.childs):
            if c is not None:
                c.enc = (n.enc << 1) | idx
        for c in n.childs:
            enc(c)

    root = ns[0]
    enc(root)

    # printing the final result.
    Node.result(root)


def main():
    enw = open("data/enwik4", 'rb').read()
    bg = bitgen(enw)

    number_of_bits = 16
    lookup = defaultdict(lambda: [1, 2])
    HH = 0.0

    try:
        prevx = [-1] * number_of_bits
        while True:
            x = next(bg)

            px = tuple(prevx)

            p_1 = lookup[px][0] / lookup[px][1]
            p_x = p_1 if x == 1 else 1.0 - p_1

            H = -math.log2(p_x)
            HH += H

            lookup[px][0] += x == 1
            lookup[px][1] += 1
            prevx.append(x)
            prevx = prevx[-number_of_bits:]

    except StopIteration:
        pass

    print(f"information entropy: {HH/8.0:.1f}")


if __name__ == "__main__":
    # main()
    # enw = open("data/enwik4", 'rb').read()
    enw = b'A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED'
    huffman(enw)
