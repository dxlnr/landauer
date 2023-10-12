"""Compression"""
import math
from collections import defaultdict

from lib.utils import bitgen


class Node:
    def __init__(self, w, v=None, child=None):
        self.w = w
        self.v = v
        self.child = None
        self.enc = 0

    def __repr__(self):
        return f"\n({chr(self.v)}) {self.w} : {bin(self.enc)}"


def huffman():
    """Huffman coding"""
    enw = open("data/enwik4", 'rb').read()
    print(len(enw))

    lt = defaultdict(lambda: 0)
    for c in enw:
        lt[c] += 1

    lt = dict(sorted(lt.items(), key=lambda kv: kv[1]))

    ns = [Node(v, k) for k, v in lt.items()]
    # for l, r in zip(ns):
    #     nn = Node(w=((l.w + r.w) / len(enw)), child=[l,r])

    print(ns)


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
