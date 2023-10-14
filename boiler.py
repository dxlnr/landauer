"""Compression"""
import math
from collections import defaultdict

from lib.utils import bitgen


class Node:
    def __init__(self, w, v=None, childs=[None, None]):
        self.w = w
        self.v = v
        self.childs = childs
        self.enc = 0
        self.depth = 0

    def __repr__(self):
        return f"({self.v}) {self.w} : {bin(self.enc)}"

    def __str__(self, level=0):
        ret = "\t" * level + self.v + "\n"
        for c in self.childs:
            if c is not None:
                ret += c.__str__(level + 1)
        return ret


def enc(n):
    if n is None:
        return

    for idx, c in enumerate(n.childs):
        if c is not None:
            c.enc = (n.enc << 1) | idx

    for c in n.childs:
        enc(c)


def _final(n: Node):
    if n is None:
        return
    if n.v is not None:
        print("(dfs)", repr(n))
    for c in n.childs:
        _final(c)


def huffman(enw=b'A_DEAD_DAD_CEDED_A_BAD_BABE_A_BEADED_ABACA_BED'):
    """Huffman coding"""
    # enw = open("data/enwik4", 'rb').read()
    print(len(enw))

    lt = defaultdict(lambda: 0)
    for c in enw:
        lt[c] += 1

    lt = dict(sorted(lt.items(), key=lambda kv: kv[1]))

    ns = [Node(v, chr(k)) for k, v in lt.items()]

    while ns:
        if len(ns) <= 1:
            break

        left = ns.pop(0) if ns else None
        right = ns.pop(0) if ns else None

        nn = Node(w=((left.w + right.w)), childs=[left, right])
        idx = len(ns)
        for i in range(len(ns)):
            if nn.w <= ns[i].w:
                idx = i
                break

        ns.insert(idx, nn)

    root = ns[0]
    enc(root)

    _final(root)


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
    huffman()
